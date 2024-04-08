def fibonacci(n):
    a, b = 0, 1
    fibonacci_list = []
    for _ in range(n):
        fibonacci_list.append(a)
        a, b = b, a + b
    return fibonacci_list

try:
    count = int(input("How many Fibonacci numbers do you want to see? "))
    if count <= 0:
        print("Please enter a positive number greater than zero.")
    else:
        result = fibonacci(count)
        print(result)
except ValueError:
    print("Please enter a valid integer.")
