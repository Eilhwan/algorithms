
def solution(numbers, hand):
    key_pad = [
        [3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]
    ]
    l_hand = 0
    r_hand = 0
    ans = ""

    for i in range(len(numbers)):
        number = numbers[i]
        if number == 1 or number == 4 or number == 7:
            l_hand = number
            ans += "L"
        elif number == 3 or number == 6 or number == 9:
            r_hand = number
            ans += "R"
        else:
            x1 = key_pad[l_hand][0]
            x2 = key_pad[number][0]
            y1 = key_pad[l_hand][1]
            y2 = key_pad[number][1]
            l_dist = abs(x2 - x1) + abs(y2 - y1)

            x1 = key_pad[r_hand][0]
            x2 = key_pad[number][0]
            y1 = key_pad[r_hand][1]
            y2 = key_pad[number][1]
            r_dist = abs(x2 - x1) + abs(y2 - y1)
            if l_dist > r_dist:
                r_hand = number
                ans += "R"
            elif r_dist > l_dist:
                l_hand = number
                ans += "L"
            else:
                if hand == "right":
                    r_hand = number
                    ans += "R"
                elif hand == "left":
                    l_hand = number
                    ans += "L"

    return ans

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

ans = solution(numbers, hand)
print(ans)