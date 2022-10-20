def prime(n):
    num = 2
    count = 0
    if n > 0:
        while count < n:
            for i in range(2, num//2):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")
                count += 1
                if count == n:
                    print()
                    print(f"{n}th prime number is: ", num)
            num += 1

    else:
        print("n should be greater than 0")


prime(5)
