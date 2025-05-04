def factorial(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


def solution(n, k):
    answer = []
    numbers = [(i + 1) for i in range(n)]
    k -= 1
    
    for i in range(n - 1, 0, -1): # (n - 1)! ~ 2!
        idc = factorial(i)
        idx = k // idc
        k %= idc
        answer.append(numbers.pop(idx))
    answer.append(numbers[0])
    
    return answer
        


if __name__ == "__main__":
    print(solution(3, 5))
    # print(solution())