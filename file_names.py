def solution(files):
    # 정렬이 된 파일명들을 저장할 리스트 변수를 선언합니다.
    answer = []
    # 파일들의 개수인 files의 길이를 저장하는 변수를 선언합니다
    files_len = len(files)

    # files에 있는 각 파일마다 반복한다.
    for idx in range(files_len):
        # 현재 파일의 Head부분을 저장할 변수를 선언한다.
        head = ''
        # 현재 파일의 number부분을 저장할 변수를 선언합니다.
        number = ''
        # 현재 파일의 이름을 한 문자씩 읽다가 숫자 부분을 읽기 시작했을 때 감지하는 변수를 선언합니다.
        is_number = False

        # 현재 파일에서 한 문자씩 반복해봅니다.
        for char in files[idx]:
            # 현재 문자가 숫자 형태의 문자라면
            if ord('0') <= ord(char) <= ord('9'):
                # is_number의 값을 True로 변경합니다.
                is_number = True
                # number에 현재 문자를 넣어줍니다.
                number += char
            # 파일명에서 아직 Number부분을 읽기 시작하지 않아 Head부분을 읽어야 한다면
            elif not is_number:
                # head에 현재 문자를 넣어준다.
                head += char
            # is_number가 True라면 파일명에서 Head와 Number부분을 변수에 다 저장한 상태이므로
            elif is_number:
                # 더 이상 파일명을 읽을 필요가 없으니 반복문을 탈출한다.
                break
        # Head는 대소문자를 가리지 않으므로 head의 값을 소문자로 변경합니다.
        head = head.lower()
        # Number 부분을 실제 숫자 기준으로 정렬해야하므로 정수형으로 변환합니다.
        number = int(number)
        # files에서의 현재 파일명 값을 (현재 파일명, Head, Number)의 튜플 형식으로 변경해줍니다.
        files[idx] = (files[idx], head, number)

    # 문제에서 제공한 기준의 우선 Head는 사전순, 다음으로 Number는 숫자순으로 정렬해준다.
    files.sort(key=lambda file: (file[1], file[2]))
    # 정렬된 상태에서 파일명들만 그대로 answer에 저장해준다.
    answer = [file[0] for file in files]
    # 정렬된 파일명 리스트 변수인 answer를 반환해준다.
    return answer

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))