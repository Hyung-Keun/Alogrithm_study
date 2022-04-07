from collections import deque
def wallsAndGates(rooms):
    '''
    Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
    '''
    empty_room = 2**31 -1 # 2147483647
    m = len(rooms) #행 길이
    n = len(rooms[0]) #열 길이

    directions = [0, 1, 0, -1, 0] #네비게이션 준비: 위 아래 오른쪽 왼쪽 이렇게 표현하는것이 더 느낌있어보인다.
    q = deque() #BFS니까 큐 장착하고, 데크 준비합시다
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                q.append((i, j)) #예시 인풋일경우: deque([(0, 2), (3, 0)])
    while q:
        i, j = q.popleft() # q 상태: (0,2) (3,0)
        for k in range(4):
            x = i + directions[k]
            y = j + directions[k+1]
            #  (x, y) -> (0,2): (0, 3), (1, 2), (0, 1), (-1, 2)
            # (x, y) -> (3, 0): (3, 1), (4,0), (3, -1), (2, 0)
            if x < 0 or x >=m or y < 0 or y >=n:
                continue
            if rooms[x][y] != empty_room:
                continue
            rooms[x][y] = rooms[i][j] + 1 #게이트 근처에 있으면 1, 그리고 근처 1인 좌표를 저장해주고,
            q.append((x, y)) #나중에 큐를 이용해서 또 게이트와 얼마나 먼 좌표인지 계산하고 거리만큼 더하기 해준다.
    return rooms #좌표에 나와있는 빈칸에 게이트로부터 얼만틈 먼지 다 적어놓은 것을 반환해준다.

rooms = [[2147483647,-1,0,2147483647],
         [2147483647,2147483647,2147483647,-1],
         [2147483647,-1,2147483647,-1],
         [0,-1,2147483647,2147483647]]
print(wallsAndGates(rooms))