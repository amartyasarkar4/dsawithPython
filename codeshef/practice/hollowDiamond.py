nu = int(input("Enter the no of lines: "))
for i in range(nu):
    for j in range(nu):
        if i+j == (nu//2) or j-i == (nu//2) or i-j == (nu//2) or i+j == (nu//2)*3:
            print("*", end="")
        else:
            print(end=" ")
    print()
