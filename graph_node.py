class UndirectedGraphNode:
    def __init__(self, x: int):
        self.label = int(x)
        self.neighbors = []

    def __repr__(self) -> str:
        return f"{self.label}"

    def __str__(self) -> str:
        return f"{self.label}"

    def __eq__(self, o: object) -> bool:
        return self.label == o.label if o else False

    def __hash__(self) -> int:
        return id(self)

    @classmethod
    def input_to_undirected_graph_nodes(cls, string):
        output = []
        nodes = string.split("#")
        nodes_map = {}

        for node in nodes:
            values = node.split(",")
            value = int(values.pop(0))

            undirected_graph_node = None
            if value in nodes_map:
                undirected_graph_node = nodes_map[value]
            else:
                undirected_graph_node = UndirectedGraphNode(value)
                nodes_map[value] = undirected_graph_node

            while values:
                value = int(values.pop(0))

                neighbor = None
                if value in nodes_map:
                    neighbor = nodes_map[value]
                else:
                    neighbor = UndirectedGraphNode(value)
                    nodes_map[value] = neighbor

                undirected_graph_node.neighbors.append(neighbor)

            output.append(undirected_graph_node)

        return output
