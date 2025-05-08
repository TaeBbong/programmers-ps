import sys
limit_number = 100000
sys.setrecursionlimit(limit_number)


def can_defense(n, k, partial_enemy):
    return n >= sum(sorted(partial_enemy, reverse=True)[k:])


def binary_search(s, e, n, k, enemy):
    if s >= e:
        return s
    
    m = (s + e) // 2
    if can_defense(n, k, enemy[:m + 1]):
        return binary_search(m, e, n, k, enemy)
    else:
        return binary_search(s, m - 1, n, k, enemy)
    
    
def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    
    return binary_search(0, len(enemy) - 1, n, k, enemy) + 1


if __name__ == "__main__":
    print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))