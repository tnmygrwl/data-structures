#!/usr/bin/env python


def dfs(graph, start, path):
    
    ''' graph: dictionary of adjacencies in graph
        start: vertex to start from
        path: path is the traversal through the graph '''

    R = [start]
    while R:
        x = R.pop()
        if x not in path:
            path.append(x)
            R.extend(graph[x])
    return path


def main():
    G = {
        'a': ['b', 'c', 'f'],
        'b': ['d', 'f'],
        'c': [],
        'd': [],
        'e': [],
        'f': ['e', 'b']
    }
    print(dfs(G, 'a', []))




if __name__ == '__main__':
    main()



