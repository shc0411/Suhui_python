grid = [[1, 2, 3], [4, 999, 6], [7, 8, 9]]

found = False   # 아직 못 찾았다는 뜻, 999를 찾았는지 저장하는 변수

for i in range(len(grid)):              # i = 0, i = 1, i = 2
    for j in range(len(grid[i])):       # 각 행 안의 숫자 검사 - i = 0 [1, 2, 3,]/ i = 1 [4, 999, 6]

        if grid[i][j] == 999:
            print(i, j)

            found = True    # 999 찾으면 found = True
            break

    if found:   # 999 ckwdmaus
        break