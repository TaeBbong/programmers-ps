def is_correct(w):
    count = 0
    for s in w:
        if s == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    return False


def reverse_brackets(w):
    r = ''
    for s in w:
        if s == '(':
            r += ')'
        else:
            r += '('
    return r


def divide_brackets(w):
    count = 0
    for i, s in enumerate(w):
        if s == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return (w[:i + 1], w[i + 1:])
    return (w, '')
        

def correct_brackets(w):
    # 1. Checks if `w` is empty
    if len(w) == 0:
        return w
    # 2. Divides `w` into two strings `u`, `v`
    u, v = divide_brackets(w)
    # 3. Returns `u` + `correct_brackets(v)` if `u` is correct
    if is_correct(u):
        return u + correct_brackets(v)
    # 4. Corrects `u`, and get results for `v`
    r = '('
    r += correct_brackets(v)
    r += ')'
    r += reverse_brackets(u[1:-1])
    return r


def solution(p):
    answer = correct_brackets(p)
    return answer


def solution(p):
    answer = correct_brackets(p)
    return answer
        


if __name__ == "__main__":
    print(solution("()))((()"))