def solution(elements):
    answer = set()
    length = len(elements)

    for i in range(length):
        sums = elements[i]
        answer.add(sums)
        for j in range(i+1,i+length):
            sums += elements[j%length]
            answer.add(sums)

    # elements *= 2
    # a = 1
    # while a <= len(elements) // 2:
    #     for i in range(len(elements) // 2 + 1):
    #         answer.add(sum(elements[i:i+a]))
    #     a += 1

    return len(answer)