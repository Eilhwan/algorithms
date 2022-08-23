
def solution(n):
    global res
    arr = [-1 for _ in range(n)]
    res = 0

    def recursive(cur):
        global res
        if cur == n:
            res += 1
            return

        # check
        def check(row):
            for i in range(row):
                if arr[i] == arr[row] or row - i == (abs(arr[row] - arr[i])):
                    return False
            return True

        # recursive
        for i in range(n):
            arr[cur] = i
            if check(cur):
                recursive(cur+1)
    recursive(0)
    return res


if "__main__" == __name__:
    print(solution(8))
