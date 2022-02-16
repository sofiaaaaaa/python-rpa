# 백트래킹 알고리즘

def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True
    

def DFS(N, current_row, current_candidate, final_result):
    if current_row == N: # 퀸이 모두 배치되었다면

        # 얇은 복사. 복사본을 넘김 
        final_result.append(current_candidate[:])
        return 

    for candidate_col in range(N):
        # 수직, 수평체크
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate, final_result)
            current_candidate.pop() # 후보군에서 제외하기 



def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result