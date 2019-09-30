class GraphUtils:
    def __init__(self):
        pass

    @staticmethod
    def create_graph(item_dict):
        graph = {}
        for node, parent in item_dict.items():
            if node not in graph:
                graph[node] = {'name': node, 'children': []}
            if parent not in graph:
                graph[parent] = {'name': parent, 'children': [node]}
            elif node not in graph[parent]['children']:
                graph[parent]['children'].append(node)
        return graph
