import sys
import collections

input = sys.stdin.readline
dic = collections.defaultdict(str)

N, M = map(int,input().split()) # 사이트 수, 비밀번호를 찾을 사이트 수

for i in range(N): # 사이트와 비밀번호 저장
    site, passward = map(str, input().split())
    dic[site] = passward

for i in range(M): # dic에서 해당 사이트 비밀번호 추출
    site = str(input()).rstrip()
    print(dic[site])