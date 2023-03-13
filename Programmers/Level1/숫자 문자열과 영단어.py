def solution(s):
    alp = ["zero","one","two","three","four","five", "six", "seven","eight","nine"]
    for v,i in enumerate(alp):
        if i in s:
           s = s.replace(i,str(v))
    return int(s)