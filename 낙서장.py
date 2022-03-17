import math
def solution(progresses, speeds):

    answer = []
    due = []
    function = 0
    length = len(progresses)-1
    for i in range(length+1):
        pointer = i
        pointer2 = i + 1
        while pointer < pointer2:
        day = math.ceil((100 - progresses[i])/speeds[i])
        due.append(day)



    pointer = 0
    while pointer < length:
        pointer2 = pointer + 1
        if due[pointer] < due[length]:
            function +=1
            answer.append(function)
        elif due[pointer] > due[pointer2]:
            function += 1
            answer.append(function)
        else:
            pass
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))