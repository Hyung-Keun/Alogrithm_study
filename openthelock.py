from collections import deque
def openLock(deadends, target):
    deadends_list = set(deadends) #['0201', '0101', '0102', '1212', '2002']
    q = deque()
    q.append(('0000', 0))
    visited = set('0000')
    while q:
        string, step = q.popleft()
        if string in deadends_list: #만약에 deadends에 같은것이 있으면 빠져나온다.
            continue
        if string == target: #만약에 자물쇠비밀번호랑 일치하면
            return step #몇번만에 해결했는지 리턴해준다.
        for i in range(4): #4자리 이기때문에 4번 돌려준다
            num = int(string[i]) #string이기때문에 정수로 바꿔준다.
            for dx in (-1, 1): #+1로 돌릴지 -1로 돌릴지 둘다 고려해준다.
                num_new = (num + dx) % 10 # 자릿수
                new_string = string[:i] + str(num_new) + string[i + 1:]
                #시작부터특정위치까지 + str(num_new) + 특정시작위치서부터 끝까지
                # print(new_string)
                if new_string not in visited:
                    q.append((new_string, step + 1))
                    visited.add(new_string)


    return -1

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(openLock(deadends, target))