def tribonacci(num):
    count = 0
    n1, n2, n3 = 1, 1, 2
    while count < num:
        print(n1, end=' ')
        nth = n1 + n2 + n3
        n1 = n2
        n2 = n3
        n3 = nth
        count += 1


number = int(input())
tribonacci(number)
