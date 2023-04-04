def solution(keymap, targets):
    answer = []
    mapping = {}

    for s in range(len(keymap)):
        for i, key in enumerate(keymap[s]):
            if key not in mapping:
                mapping[key] = mapping.get(key,i+1)
            mapping[key] = min(mapping.get(key), i + 1)

    for target in targets:
        sum_value = 0
        for c in target:
            if c not in mapping:
                answer.append(-1)
                break
            sum_value += mapping[c]
        else:
            answer.append(sum_value)
    return answer