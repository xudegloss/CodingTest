def solution(s):
    _input=[int(i) for i in s.split()]
    return str(min(_input))+" "+str(max(_input))