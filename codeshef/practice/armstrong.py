for i in range(1000):
    num = i
    length = len(str(i))
    result = 0
    while i != 0:
        digit = i % 10
        result = result + (digit ** length)
        i = i//10
    if result == num:
        print(result)