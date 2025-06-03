import copy


def dfs(play, i, k, info):
    if i == 11:
        if k:
            play[-1] += k
        return [play]
    results = []
    if k >= info[i] + 1:
        results += dfs(play + [info[i] + 1], i + 1, k - info[i] - 1, info)
        results += dfs(play + [0], i + 1, k, info)
    else:
        results += dfs(play + [0], i + 1, k, info)
    return results


def solution(n, info):
    MAX = -55
    MAX_ANSWER = []
    score = [i for i in range(10, -1, -1)]

    plays = dfs([], 0, n, info)
    for play in plays:
        ans = 0
        for i in range(10, -1, -1):
            if play[i] > info[i]:
                ans += score[i]
            else:
                if info[i]:
                    ans -= score[i]
        if ans > MAX:
            MAX_ANSWER = copy.copy(play)
            MAX = ans
        if ans == MAX:
            if ''.join(reversed([str(i) for i in play])) > ''.join(reversed([str(i) for i in MAX_ANSWER])):
                MAX_ANSWER = copy.copy(play)
    if MAX > 0:
        return MAX_ANSWER
    return [-1]


if __name__ == "__main__":
    print(solution(5, [2,1,1,1,0,0,0,0,0,0,0])) # [0,2,2,0,1,0,0,0,0,0,0]
    print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
    print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
    print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
    print(solution(9, [0, 0, 0, 0, 0, 2, 1, 0, 1, 0, 5])) # [1, 1, 1, 1, 1, 3, 0, 1, 0, 0, 0]
    print(solution(3, [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])) # [-1]
    print(solution(3, [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])) # [1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
    print(solution(3, [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1])) # [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]