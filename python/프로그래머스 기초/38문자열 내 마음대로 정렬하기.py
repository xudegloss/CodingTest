# key 기준으로 정렬하는 함수가 존재한다.
# string=["abce", "abcd", "cdx"]
# n=2
# print(sorted(string, key=lambda x: x[2]))

def solution(strings, n):
    strings.sort()
    # print(strings) 미리 한번 정렬해주기. (인덱스에 같은 문자가 있음을 대비하기 위하여)
    return sorted(strings, key=lambda x: x[n])

print(solution(["abce", "abcd", "cdx"], 2))