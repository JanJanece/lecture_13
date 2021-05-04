def recursive_nth_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        return recursive_nth_fibo(n - 2) + recursive_nth_fibo(n - 1)

def main():
    prvek = int(input("Zadejj prvek:"))
    print(recursive_nth_fibo(prvek))
    poslupnost = [recursive_nth_fibo(n) for n in range(prvek + 1)]
    print(poslupnost)

if __name__ == '__main__':
    main()
