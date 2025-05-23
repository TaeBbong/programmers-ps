from collections import deque


def jigecar(storage, request):
    queue = deque([])
    containers = set([])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = {}
    
    for y in range(len(storage)):
        queue.append((y, 0))
        queue.append((y, len(storage[0]) - 1))
    for x in range(1, len(storage[0]) - 1):
        queue.append((0, x))
        queue.append((len(storage) - 1, x))
        
    while len(queue):
        cur = queue.popleft()
        visited[cur] = True

        if storage[cur[0]][cur[1]] == request:
            containers.add(cur)
            continue
        elif storage[cur[0]][cur[1]] == ' ':
            for d in directions:
                nex = (cur[0] + d[0], cur[1] + d[1])
                if nex not in visited:
                    if 0 <= nex[0] < len(storage) and 0 <= nex[1] < len(storage[0]):
                        queue.append(nex)
        else:
            continue
    for container in list(containers):
        storage[container[0]][container[1]] = ' '
    return storage, len(containers)
                

def crain(storage, request):
    removed = 0
    for y in range(len(storage)):
        for x in range(len(storage[0])):
            if storage[y][x] == request[0]:
                storage[y][x] = ' '
                removed += 1
    return storage, removed


def solution(storage, requests):
    answer = sum([len(s) for s in storage])
    storage = [list(s) for s in storage]
    for request in requests:
        if len(request) == 1:
            storage, removed = jigecar(storage, request)
            answer -= removed
        else:
            storage, removed = crain(storage, request)
            answer -= removed
    return answer


if __name__ == "__main__":
    print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]))