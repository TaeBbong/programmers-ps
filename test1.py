from collections import defaultdict


def solution(edges):
    indeg  = defaultdict(int)
    outdeg = defaultdict(int)

    # 1. 각 노드의 in-degree, out-degree 계산
    for s, e in edges:
        outdeg[s] += 1
        indeg[e]  += 1
        # 존재만 보장
        indeg.setdefault(s, 0)
        outdeg.setdefault(e, 0)

    # 2. 생성한 정점(센터) 찾기 : in = 0 & out >= 2
    center = next(v for v in outdeg if indeg[v] == 0 and outdeg[v] >= 2)

    # 3. 막대·8자 카운트 (센터는 제외)
    stick = sum(1 for v in outdeg if v != center and outdeg[v] == 0)
    eight = sum(1 for v in outdeg if v != center and outdeg[v] == 2)

    # 4. 도넛 개수 = 센터 out-degree − 막대 − 8자
    donut = outdeg[center] - stick - eight

    return [center, donut, stick, eight]