def quicksort(lst, start, end):
    def partition(part, ps, pe): #(내가보아야할 부분, 시작부분, 마지막부분)
        pivot = part[pe] #끝에 피벗 잡아준다. 제일 마지막 녀석을 피벗으로 잡아준다.
        i = ps - 1 #i를 피벗보다 작은곳에 유기한다. 시작부터 하나 작은곳을 i로 잡아준다
        for j in range(ps, pe): # i와 j를 사용하는데 쓰임이다른데, j가 정찰병이다. 한칸씩 이동한다. 거기서 만약에 j위치에 있는 숫자가
                                #피벗보다 같거나 작을경우, i의 우치를 하나 이동시켜주고 i와j의 숫자를 바꿔준다.
            if part[j] <= pivot:
                i += 1
                part[i], part[j] = part[j], part[i]

        part[i + 1], part[pe] = part[pe], part[i + 1]
        return i + 1 # for문 완료후, 어떤위치에 피벗을 가져다 놓았는지 반환시켜준다.
    #---------------------------------------------------------------------끝내는부분
    if start >= end:
        return None

    #assert quicksort([4, 6, 2, 9, 1], 0, 4) == [1, 2, 4, 6, 9]
    p = partition(lst, start, end) # p = partion([4, 6, 2, 9, 1], start = 0, end = 4) -> 0

    quicksort(lst, start, p - 1)
    quicksort(lst, p + 1, end) # 여기서부터 다시 시작해서 들어간다.
    return lst