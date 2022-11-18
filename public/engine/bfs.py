from collections import deque
from dataclasses import dataclass

@dataclass
class rechercheDFS:
    graph: dict
    start: int

    def recherche(self):
        visited = []
        queue = deque()
        queue.append(self.start)

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                unvisited = [n for n in self.graph[node] if n not in visited]
                queue.extend(unvisited)

        return visited