from collections import (defaultdict, deque)


class CourseSchedule:

    def can_finish(self, num_courses: int, prerequisites: list[list[int]]) -> (list, bool):
        # first we need to compute the in_degree for all the nodes
        in_degree = [0] * num_courses
        adj_list = defaultdict(list)

        for dst, src in prerequisites:
            in_degree[dst] += 1
            adj_list[src].append(dst)


        # now we need to enqueue all nodes that have an in-degree of 0
        queue = deque([idx for idx, _ in enumerate(in_degree) if in_degree[idx] == 0])
        

        # start iteration
        order = []
        while queue:
            ele = queue.popleft()
            order.append(ele)

            for neighbour in adj_list[ele]:
                # reduce the in_degree of all neighbours of node that is being visited
                in_degree[neighbour] -= 1
                # enqueue any neighbours that have an in_degree of 0
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        return len(order) == num_courses, order


if __name__ == "__main__":
    cs = CourseSchedule()
    can_finish, order = cs.can_finish(4, [[1,0],[2,0],[3,1],[3,2]])
    assert can_finish == True
    assert order == [0, 1, 2, 3]
        
        
