def fibonacci(num_of_times):
    fib_series = [0, 1]
    for i in range(num_of_times):
        length = len(fib_series)
        new_num = fib_series[length - 1] + fib_series[length - 2]
        fib_series.append(new_num)
    return fib_series


num_of_times = input("How many fibonacci series numbers do you want?")
fib_series = fibonacci(int(num_of_times)-2)
print(fib_series)

