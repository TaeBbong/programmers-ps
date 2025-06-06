import bisect


def score_query(scores, threshold):
    idx = bisect.bisect_left(scores, threshold)
    return len(scores) - idx


def generate_possible_queries(lang, posi, care, food):
    results = []
    for l in [lang, '-']:
        for p in [posi, '-']:
            for c in [care, '-']:
                for f in [food, '-']:
                    results.append(' '.join([l, p, c, f]))
    return results


def solution(infoes, queries):
    infoes = sorted(infoes, key=lambda x: int(x.split(' ')[-1]))
    answer = []
    possible_queries = []
    for l in ['cpp', 'java', 'python', '-']:
        for p in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for f in ['chicken', 'pizza', '-']:
                    possible_queries.append(' '.join([l, p, c, f]))

    people_cases = {}
    for query in possible_queries:
        people_cases[query] = []

    for info in infoes:
        l, p, c, f, s = info.split(' ')
        person_queries = generate_possible_queries(l, p, c, f)
        for query in person_queries:
            people_cases[query].append(int(s))
    
    for query in queries:
        l, _, p, _, c, _, f, s = query.split(' ')
        q = ' '.join([l, p, c, f])
        results = people_cases[q]
        answer.append(score_query(results, int(s)))

    return answer


if __name__ == "__main__":
    print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))