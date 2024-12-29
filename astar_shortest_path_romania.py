# Importamos las bibliotecas necesarias
import heapq  # Biblioteca para estructuras de datos, útil para la cola de prioridad en A*
import networkx as nx  # Biblioteca para trabajar con grafos
import matplotlib.pyplot as plt  # Biblioteca para graficar

# Definimos el mapa de Rumania como un diccionario de ciudades y sus conexiones
romania_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)],
}

# Definimos las heurísticas como estimaciones de la distancia de cada ciudad a Bucarest (valores aproximados)
heuristics = {
    'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253, 'Timisoara': 329,
    'Lugoj': 244, 'Mehadia': 241, 'Drobeta': 242, 'Craiova': 160, 'Rimnicu Vilcea': 193,
    'Fagaras': 176, 'Pitesti': 100, 'Bucharest': 0, 'Giurgiu': 77, 'Urziceni': 80,
    'Hirsova': 151, 'Eforie': 161, 'Vaslui': 199, 'Iasi': 226, 'Neamt': 234
}

# Función para ejecutar el algoritmo A*
def a_star_search(graph, start, goal, heuristics):
    # Creamos una lista abierta (open_list) que usaremos como cola de prioridad
    open_list = []
    # Insertamos el nodo inicial (start) en la lista abierta con un costo f de 0
    heapq.heappush(open_list, (0, start))
    
    # Diccionario para almacenar los costos g (costo real desde el inicio)
    g_costs = {start: 0}
    # Diccionario para rastrear el nodo desde el que llegamos a cada nodo (para reconstruir la ruta)
    came_from = {start: None}
    
    # Bucle principal: mientras haya nodos en la lista abierta
    while open_list:
        # Extraemos el nodo con el menor costo f de la lista abierta
        current_f_cost, current_node = heapq.heappop(open_list)
        
        # Si hemos llegado al nodo objetivo, reconstruimos y devolvemos el camino
        if current_node == goal:
            path = [] # Inicializa una lista para la ruta
            while current_node:
                path.append(current_node) # Agrega el nodo a la ruta
                current_node = came_from[current_node] # Retrocede al nodo anterior
            return path[::-1], g_costs[goal] # Devuelve la ruta y el costo total
        
        # Recorremos los vecinos (ciudades conectadas) del nodo actual
        for neighbor, distance in graph[current_node]:
            # Calculamos el costo g tentativo hasta el vecino
            tentative_g_cost = g_costs[current_node] + distance
            # Si es un nuevo vecino o encontramos un camino más corto hacia él
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                # Actualizamos el costo g para este vecino
                g_costs[neighbor] = tentative_g_cost
                # Calculamos el costo f (g + h) usando la heurística
                f_cost = tentative_g_cost + heuristics[neighbor]
                # Añadimos el vecino a la lista abierta
                heapq.heappush(open_list, (f_cost, neighbor))
                # Registramos que llegamos a este vecino desde el nodo actual
                came_from[neighbor] = current_node
    
    # Si no encontramos un camino, devolvemos None y costo infinito
    return None, float('inf')

# Ejecutamos el algoritmo para encontrar la ruta óptima de Arad a Bucarest
optimal_path, total_cost = a_star_search(romania_map, 'Arad', 'Bucharest', heuristics)

# Imprimimos los resultados de la búsqueda
print("Ruta óptima de Fagaras a Bucarest:", " -> ".join(optimal_path))
print("Costo total de la ruta:", total_cost)

# Función para dibujar el grafo y resaltar la ruta encontrada
def draw_graph(graph, path=None):
    # Creamos un grafo vacío
    G = nx.Graph() # Crea un objeto grafo de NetworkX
    
    # Añadimos nodos y aristas al grafo según las conexiones en romania_map
    for city in graph:
        for neighbor, distance in graph[city]:
            G.add_edge(city, neighbor, weight=distance) # Agrega bordes con sus pesos al grafo
    
    # Generamos posiciones de los nodos de manera automática
    pos = nx.spring_layout(G)  # Posición de los nodos para el grafo

    # Dibujamos el grafo completo
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
    
    # Añadimos etiquetas de peso (distancia) en las aristas
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Si se proporciona un camino (ruta óptima), lo resaltamos en rojo
    if path:
        path_edges = list(zip(path, path[1:]))  # Creamos una lista de pares de ciudades consecutivas en el camino
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)  # Dibujamos el camino resaltado

    # Mostramos el grafo
    plt.show()

# Llamamos a la función para visualizar el grafo y la ruta óptima
draw_graph(romania_map, optimal_path)