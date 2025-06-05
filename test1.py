def solution(cap, n, deliveries, pickups):
    answer = 0
    d = p = 0
    for i in range(n - 1, -1, -1):
        d += deliveries[i]
        p += pickups[i]
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (i + 1) * 2
    return answer


if __name__ == "__main__":
    print(solution(4,	5,	[1, 0, 3, 1, 2],	[0, 3, 0, 4, 0]))
    print(solution(4,	3,	[0, 0, 0],	[4, 4, 4]))
    print(solution(2,	1, [3],	[0]))