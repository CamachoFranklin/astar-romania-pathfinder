# Implementación del Algoritmo A* en el Mapa de Carreteras de Rumania

## Descripción del Proyecto
Este repositorio contiene la implementación del algoritmo A* para encontrar el camino más corto entre dos ciudades en el mapa de carreteras de Rumania. El algoritmo utiliza una combinación de costos acumulados y heurísticas para realizar búsquedas eficientes en grafos ponderados.

### Características Principales
- Modelado del mapa de Rumania como un grafo utilizando un diccionario en Python.
- Uso de heurísticas admisibles para estimar distancias en línea recta a la ciudad destino.
- Visualización del grafo con la ruta óptima resaltada utilizando NetworkX y Matplotlib.

## Estructura del Proyecto

### Archivos
- **`astar_shortest_path_romania.py`**: Contiene la implementación del algoritmo A* y la visualización del grafo.
- **`Implementacion_algoritmo_A_Rumania_Franklin_Camacho.pdf`**: Documento explicativo sobre el problema, la heurística y el diseño del grafo.

### Estructura del Grafo
El mapa de Rumania se representa como un diccionario donde:
- Cada ciudad es un nodo.
- Cada carretera es una arista con un peso que representa la distancia entre ciudades.

**Ejemplo de representación:**
```python
'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)]
```

### Heurística
La heurística estima la distancia en línea recta desde cada ciudad hasta Bucarest. Por ejemplo:
- Arad: 366 km
- Sibiu: 253 km

## Resultados
- Ruta óptima de Arad a Bucarest: **Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucarest**
- Distancia total: **418 km**

La ruta se destaca visualmente en el grafo generado por la implementación.

## Requisitos

### Dependencias
Este proyecto utiliza las siguientes bibliotecas de Python:
- `heapq`: Para manejar la cola de prioridad en el algoritmo A*.
- `networkx`: Para trabajar con grafos.
- `matplotlib`: Para la visualización del grafo.

### Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/usuario/astar-romania-pathfinder.git
   ```
2. Instala las dependencias:
   ```bash
   pip install networkx matplotlib
   ```

## Ejecución
1. Ejecuta el script principal:
   ```bash
   python astar_shortest_path_romania.py
   ```
2. Observa los resultados en la terminal y la visualización del grafo.

## Visualización
El grafo generado muestra:
- Nodos (ciudades)
- Aristas (carreteras con sus distancias)
- Ruta óptima destacada en color rojo.

## Contribución
Si deseas contribuir:
1. Haz un fork del repositorio.
2. Crea una rama para tu función:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza un pull request con tus cambios.