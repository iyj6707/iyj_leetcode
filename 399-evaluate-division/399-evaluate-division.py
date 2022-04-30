class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # init graph
        graph = defaultdict(lambda: defaultdict(float))
        for equation, value in zip(equations, values):
            graph[equation[0]][equation[0]] = 1.0
            graph[equation[1]][equation[1]] = 1.0
            graph[equation[0]][equation[1]] = value
            graph[equation[1]][equation[0]] = 1 / value
        
        print(graph)

        # calculate weight
        for src_node in graph.keys():
            visited = set()
            stack = [src_node]
            while stack:
                cur_node = stack.pop()
                if cur_node not in visited:
                    visited.add(cur_node)
                    for next_node in graph[cur_node]:
                        stack.append(next_node)
                        graph[src_node][next_node] = graph[src_node][cur_node] * graph[cur_node][next_node]
        
        # calculate answer
        answer = []
        for query in queries:
            src, dst = query[0], query[1]
            if not graph[src][dst]:
                answer.append(-1.0)
            else:
                answer.append(graph[src][dst])
        
        return answer
        
            