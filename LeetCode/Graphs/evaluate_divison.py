from collections import defaultdict


def dfs(graph: dict, dividend: str, divisor: str) -> float:
    if dividend not in graph or divisor not in graph:
        return -1.0

    if dividend == divisor:
        return 1.0

    stack, visited = [(dividend, 1)], set()

    while stack:
        node, curr_quotient = stack.pop()
        visited.add(node)

        for neighbor, value in graph[node].items():
            if neighbor not in visited:
                if neighbor == divisor:
                    return curr_quotient * value
                else:
                    stack.append((neighbor, curr_quotient * value))
    return -1.0


class Solution:
    def calcEquation(self, equations: 'List[List[str]]', values: 'List[float]',
                     queries: 'List[List[str]]') -> 'List[float]':

        graph = defaultdict(dict)

        for operands, value in zip(equations, values):
            a, b = operands
            graph[a][b] = value  # a / b = value
            graph[b][a] = 1.0 / value  # b / a = 1 / value

        quotients = []

        for query in queries:
            quotients.append(dfs(graph, query[0], query[1]))

        return quotients
