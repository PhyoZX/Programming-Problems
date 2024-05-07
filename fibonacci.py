# def fibonacci(n) :
#     if n == 1 :
#         return 0
#     if n <= 3 :
#         return 1
    
#     return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci(n, calculated = {1:0, 2:1, 3:1}) :
    if n in calculated :
        return calculated[n]
    calculated[n] = fibonacci(n-1, calculated) + fibonacci(n-2, calculated)
    return calculated[n]

print(fibonacci(10))