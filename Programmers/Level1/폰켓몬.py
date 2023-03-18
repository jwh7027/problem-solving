def solution(nums):
    answer = []
    get = len(nums) // 2
    for i in range(len(nums)):
        if nums[i] not in answer and len(answer) != get:
            answer.append(nums[i])

    return len(answer)

#min 함수 활용
def solution(nums):
    return min(len(nums) // 2 , len(set(nums)))