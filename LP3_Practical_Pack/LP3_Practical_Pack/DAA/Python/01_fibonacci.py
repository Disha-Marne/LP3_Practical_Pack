
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iterative(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a+b
    return result

def main():
    n = int(input("Enter number of terms: "))
    if n < 0:
        print("Enter a non-negative number")
        return
    print("Recursive:", *[fib_recursive(i) for i in range(n)])
    print("Iterative:", *fib_iterative(n))

if __name__ == "__main__":
    main()
