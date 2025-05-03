def solution(board):
    start = find_start(board)
    goal = find_goal(board)
    answer = bfs(board, start, goal)
    return answer


if __name__ == "__main__":
    print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
    print(solution([".D.R", "....", ".G..", "...D"]))