import heapq


def lazy_prims(graph):
    # initialize a mst
    mst = []

    # initialize a visited set
    visited = set()
    # add 0 to the visited set
    visited.add(0)

    # initialize a heap
    edges_heap = []

    # start with node 0 and add all edges to the heap
    for edge in graph[0]:
        heapq.heappush(edges_heap, (edge[1], 0, edge[0])) # weight, src, dst

    while edges_heap and len(visited) < len(graph):
        print("Heap", edges_heap)
        # pop the smallest edge
        weight, src, dst = heapq.heappop(edges_heap)

        if dst in visited: # skip visited node
            continue

        # add the dst node to the visited set
        visited.add(dst)
        # now add the edge to the mst
        mst.append((src, dst, weight))
        # now loop over edges of the dst node and add them to heap as long as dst is not visited
        for edge in graph[dst]:
            if edge[0] in visited:
                continue
            print("Adding edge", edge)
            heapq.heappush(edges_heap, (edge[1], dst, edge[0]))

    return mst

if __name__ == "__main__":
    """
    0 --> 1
    0 --> 2
    """
    graph = {
        0: [(1, 2.0), (2, 3.0)],
        1: [(0, 2.0), (2, 4.0), (3, 5.0)],
        2: [(0, 3.0), (1, 4.0), (3, 1.0)],
        3: [(1, 5.0), (2, 1.0)],
    }
    mst = lazy_prims(graph)
    print(mst)
    assert mst == [(0, 1, 2), (0, 2, 3), (2, 3, 1)]