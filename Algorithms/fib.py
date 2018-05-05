

def fibo(n, memo_list):
    # Check for edge cases and 0
    if (n <= 0):
        return 0
    # fib (1) takes constant time no need to memoize
    elif n == 1:
        return 1
    # The memoizing. If the fib of a number is already calculated just access the list at that value then return it.
    elif memo_list[n] is not None:
        return memo_list[n]
    # This is the recursive call of fib to find the fib value of the 2 values before the value being calculated.
    else:
        # save the result in the list and return the fib value of the input
        memo_list[n] = fibo(n-1, memo_list) + fibo(n-2, memo_list)
        return memo_list[n]



if __name__ == '__main__':
    print('Fibonacci Sequence')
    while True:
        try:
            num = int(input('fib value: '))
        except:
            print('The value must be a number')

        # Create a list of size fibo value + 1. This allows the list to be the nth index to hold the n value
        # index 6 hold the value of fib(6)

        memo_list = [None] * (num + 1)
        print(fibo(num, memo_list))
        if input('Would you like to compute another? (y/n): ') != 'y':
            break