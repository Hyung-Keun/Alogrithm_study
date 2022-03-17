from collections import deque
def test_problem_queue(num):
    deq = deque([i for i in range(1, num + 1)]) #1-num까지 데큐화된다
    while len(deq) > 1: #하나가 남을때까지 밑에 두과정 한다.
        deq.popleft() #앞에있는거버려
        deq.append(deq.popleft()) #그리고 그 다음 위에오는 녀석은 다시 아래로 붙여.
    return deq.popleft()


#deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.