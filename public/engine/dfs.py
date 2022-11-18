from dataclasses import dataclass

@dataclass
class rechercheBFS:
    graph: dict
    node: int

    def recherche(self, visited=None):
        if visited is None:
            visited = []

        if self.node not in visited:
            visited.append(self.node)

        unvisited = [n for n in self.graph[self.node] if n not in visited]
        print(unvisited)
        for self.node in unvisited:
            self.recherche(self, self.graph, self.node, visited)

        return visited