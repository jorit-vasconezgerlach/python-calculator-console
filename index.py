while 0==0:
    first = int(input())
    sign = input()
    second = int(input())

    if sign == "+":
        final = first+second
    if sign == "/":
        final = first/second
    if sign == "-":
        final = first-second
    if sign == "*":
        final = first*second

    print(">>", final)