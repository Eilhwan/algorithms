def solution(skill, skill_trees):
    ans = 0
    for sk in skill_trees:
        is_match = True
        for i in range(len(skill)):
            index = 0
            if skill[i] in sk:
                for j in range(sk.index(skill[i])):
                    if sk[j] in skill:
                        index += 1
            else:
                continue
            if index != i:
                is_match = False
                break
        if is_match:
            ans += 1
    return ans


skill_tree = ["BACDE", "CBADF", "AECB", "BDA"]
skill = "CBD"
solution(skill, skill_tree)