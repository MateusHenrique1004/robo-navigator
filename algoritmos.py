from collections import deque
import funcoes_auxiliares as fa

class Node:
    def __init__(self, state, nivel=0, parent=None):
        self.state = state      
        self.nivel = nivel      
        self.parent = parent    

    def get_path(self):
        node = self
        path = []
        while node is not None:
            path.append(node.state)
            node = node.parent
        return path[::-1]  

def amplitude(inicio, fim, mapa, dx, dy):
  
    queue = deque()
    queue.append(Node(inicio, 0, None))
    visited = {inicio: 0}

    while queue:
        current = queue.popleft()
        if current.state == fim:
            return current.get_path()

        x, y = current.state
        filhos = fa.sucessor_grid(x, y, dx, dy, mapa)
        for novo in filhos:
            new_level = current.nivel + 1
            if novo not in visited or visited[novo] > new_level:
                visited[novo] = new_level
                queue.append(Node(novo, new_level, current))
    return []  

def profundidade(inicio, fim, mapa, dx, dy):
   
    stack = []
    stack.append(Node(inicio, 0, None))
    visited = {inicio: 0}

    while stack:
        current = stack.pop()
        if current.state == fim:
            return current.get_path()

        x, y = current.state
        filhos = fa.sucessor_grid(x, y, dx, dy, mapa)
        for novo in filhos:
            new_level = current.nivel + 1
            if novo not in visited or visited[novo] > new_level:
                visited[novo] = new_level
                stack.append(Node(novo, new_level, current))
    return []

def prof_limitada(inicio, fim, mapa, dx, dy, limite):
    
    stack = []
    stack.append(Node(inicio, 0, None))
    visited = {inicio: 0}

    while stack:
        current = stack.pop()
        if current.state == fim:
            return current.get_path()

        if current.nivel < limite:
            x, y = current.state
            filhos = fa.sucessor_grid(x, y, dx, dy, mapa)
            for novo in filhos:
                new_level = current.nivel + 1
                if novo not in visited or visited[novo] > new_level:
                    visited[novo] = new_level
                    stack.append(Node(novo, new_level, current))
    return []

def aprof_iterativo(inicio, fim, mapa, dx, dy, lim_max):
   
    for limite in range(1, lim_max + 1):
        caminho = prof_limitada(inicio, fim, mapa, dx, dy, limite)
        if caminho:
            return caminho
    return []

def bidirecional(inicio, fim, mapa, dx, dy):
    
    queue_start = deque([Node(inicio, 0, None)])
    queue_goal = deque([Node(fim, 0, None)])
    visited_start = {inicio: Node(inicio, 0, None)}
    visited_goal = {fim: Node(fim, 0, None)}

    while queue_start and queue_goal:
        
        current_start = queue_start.popleft()
        x, y = current_start.state
        for novo in fa.sucessor_grid(x, y, dx, dy, mapa):
            if novo not in visited_start:
                new_node = Node(novo, current_start.nivel + 1, current_start)
                visited_start[novo] = new_node
                queue_start.append(new_node)
                if novo in visited_goal:
                    
                    path_from_start = new_node.get_path()
                    path_from_goal = visited_goal[novo].get_path()
                  
                    return path_from_start + path_from_goal[::-1][1:]
   
        current_goal = queue_goal.popleft()
        x, y = current_goal.state
        for novo in fa.sucessor_grid(x, y, dx, dy, mapa):
            if novo not in visited_goal:
                new_node = Node(novo, current_goal.nivel + 1, current_goal)
                visited_goal[novo] = new_node
                queue_goal.append(new_node)
                if novo in visited_start:
                    path_from_start = visited_start[novo].get_path()
                    path_from_goal = new_node.get_path()
                    return path_from_start + path_from_goal[::-1][1:]
    return []  