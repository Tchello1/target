if __name__ == '__main__':

    n = int(input())
    fib0=0
    fib1=1
    fib=0
    verifica = False
    for i in range(n):
        if n >= 1:
            fib = fib0 + fib1
            fib1=fib0
            fib0=fib





    print(f'O valor fibonacci de {n} é: {fib}')
    fib=0
    fib0=0
    fib1=1
    for i in range(n+1):
        if n >= 1:
            fib = fib0 + fib1
            fib1=fib0
            fib0=fib
        if fib == n:
            verifica = True
            break
    if verifica == True:
        print(f'{n} é um valor fibonacci')
    else:
        print(f'{n} Não é um valor fibonacci')
