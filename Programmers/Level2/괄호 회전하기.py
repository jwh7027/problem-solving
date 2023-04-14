def solution(s):
    answer = 0
    for i in range(len(s)):
        a = s[i:]+ s[:i]
        stack = []
        for j in a:
            if j == "[":
                stack.append("]")
            elif j == "(":
                stack.append(")")
            elif j == "{":
                stack.append("}")
            elif not stack or stack.pop() != j:
                stack.append(j)
        if not stack:
            answer += 1
    return answer