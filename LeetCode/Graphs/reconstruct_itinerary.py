from collections import defaultdict
from collections import deque


def dfs(airport, graph, route):
    while graph[airport]:
        next_city = graph[airport].popleft()  # popLEFT to maintain lexical order
        dfs(next_city, graph, route)
    route.append(airport)


class Solution:
    def findItinerary(self, tickets: 'List[List[str]]') -> 'List[str]':
        # Key Idea is to build up the route backwards starting
        # from the airport with no outgoing edges.
        # We remove edges from the graph as we visit them
        # i.e we have used that ticket.
        graph = defaultdict(deque)
        for start, end in sorted(tickets):  # Sorted to resolve lexical order
            graph[start].append(end)

        route = []
        dfs('JFK', graph, route)    # Start is always JFK
        route.reverse()
        return route
