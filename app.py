from flask import Flask, render_template, request, jsonify
import algoritmos
import algoritmos_ponderados
import funcoes_auxiliares_ponderadas as fa
import json
import random
import re

app = Flask(__name__)

def gerar_mapa(linhas=10, colunas=10, prob_obstaculo=0.2):
    mapa = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(1 if random.random() < prob_obstaculo else 0)
        mapa.append(linha)
    return mapa

def validar_coordenada(entrada):
    return bool(re.match(r"^\d+,\d+$", entrada.strip()))

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        inicio_str = request.form.get("inicio")
        fim_str = request.form.get("objetivo")
        metodo = request.form.get("metodo")
        mapa_str = request.form.get("mapa")

        if not inicio_str or not fim_str or not mapa_str or not metodo:
            return jsonify({"erro": "Todos os campos devem ser preenchidos."}), 400

        if not validar_coordenada(inicio_str) or not validar_coordenada(fim_str):
            return jsonify({"erro": "Formato inválido. Use o padrão: coluna,linha (ex: 3,5)"}), 400

        try:
            inicio = tuple(map(int, inicio_str.split(',')))
            fim = tuple(map(int, fim_str.split(',')))
            mapa = json.loads(mapa_str)
        except:
            return jsonify({"erro": "Erro ao processar as coordenadas ou o mapa."}), 400

        linhas = len(mapa)
        colunas = len(mapa[0]) if linhas > 0 else 0
        x_ini, y_ini = inicio
        x_fim, y_fim = fim

        if not (0 <= y_ini < linhas and 0 <= x_ini < colunas):
            return jsonify({"erro": "Coordenada de início fora dos limites do mapa."}), 400
        if not (0 <= y_fim < linhas and 0 <= x_fim < colunas):
            return jsonify({"erro": "Coordenada de objetivo fora dos limites do mapa."}), 400
        if mapa[y_ini][x_ini] == 1:
            return jsonify({"erro": "A posição de início está ocupada por um obstáculo."}), 400
        if mapa[y_fim][x_fim] == 1:
            return jsonify({"erro": "A posição de objetivo está ocupada por um obstáculo."}), 400

        dx, dy = 1, 1

        if metodo == "amplitude":
            caminho = algoritmos.amplitude(inicio, fim, mapa, dx, dy)
        elif metodo == "profundidade":
            caminho = algoritmos.profundidade(inicio, fim, mapa, dx, dy)
        elif metodo == "profundidade-limitada":
            limite_str = request.form.get("limite")
            if not limite_str:
                return jsonify({"erro": "Você deve informar um limite de profundidade."}), 400
            try:
                limite = int(limite_str)
                if limite < 1:
                    return jsonify({"erro": "O limite de profundidade deve ser maior que 0."}), 400
            except ValueError:
                return jsonify({"erro": "O limite de profundidade deve ser um número inteiro."}), 400
            caminho = algoritmos.prof_limitada(inicio, fim, mapa, dx, dy, limite=limite)
            if not caminho:
                return jsonify({"erro": f"Com o limite de profundidade {limite}, não foi possível alcançar o objetivo."}), 200
        elif metodo == "aprofundamento-iterativo":
            caminho = algoritmos.aprof_iterativo(inicio, fim, mapa, dx, dy, lim_max=50)
        elif metodo == "bidirecional":
            caminho = algoritmos.bidirecional(inicio, fim, mapa, dx, dy)

        elif metodo == "custo-uniforme":
            caminho, _, _ = algoritmos_ponderados.busca().custo_uniforme(list(inicio), list(fim), mapa, linhas, colunas)
        elif metodo == "greedy":
            caminho, _, _ = algoritmos_ponderados.busca().greedy(list(inicio), list(fim), mapa, linhas, colunas)
        elif metodo == "a-estrela":
            caminho, _, _ = algoritmos_ponderados.busca().a_estrela(list(inicio), list(fim), mapa, linhas, colunas)
        elif metodo == "aia-estrela":
            limite = fa.h(list(inicio), list(fim))
            caminho, _ = algoritmos_ponderados.busca().aia_estrela(list(inicio), list(fim), mapa, linhas, colunas, limite)

        else:
            return jsonify({"erro": "Método de busca inválido."}), 400

        if not caminho:
            return jsonify({"erro": "Não há caminho disponível entre os pontos definidos. Verifique se há obstáculos bloqueando totalmente o trajeto."}), 200

        return jsonify({"caminho": caminho})

    mapa = gerar_mapa()
    return render_template("index.html", mapa=mapa)

if __name__ == "__main__":
    app.run(debug=True)
