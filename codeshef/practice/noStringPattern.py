str1 = "NO"
print_N = [[" "for i in range(6)] for j in range(6)]
print_O = [[" "for i in range(6)] for j in range(6)]

for i in range(6):
    for j in range(6):
        if j == 0 or j == 5 or i == j:
            print_N[i][j] = "*"
    #         print("*", end="")
    #     else:
    #         print(end=" ")
    # print()

for i in range(6):
    for j in range(6):
        if ((j == 0 or j == 5) and (i!=0 and i!=5))  or ((i == 0 or i == 5) and (j!=0 and j!=5)):
            print_O[i][j] = "*"
    #         print("*", end="")
    #     else:
    #         print(end=" ")
    # print()

for i in range(6):
    for j in range(6):
        print(print_N[i][j], end=" ")
    print(end=" ")
    for j in range(6):
        print(print_O[i][j], end=" ")
    print()