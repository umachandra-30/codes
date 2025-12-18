def GrayCode(n):
    if n == 1:
        return ["0", "1"]

    prev_Code = GrayCode(n - 1)

    rev_Code = prev_Code.copy()
    rev_Code.reverse()

    for i in range(len(prev_Code)):
        prev_Code[i] = "0" + prev_Code[i]

    for i in range(len(rev_Code)):
        rev_Code[i] = "1" + rev_Code[i]

    return prev_Code + rev_Code


n = int(input())

grayCode = GrayCode(n)

for code in grayCode:
    print(code)
