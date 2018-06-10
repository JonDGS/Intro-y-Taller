def fibonacci(num):
    if isinstance(num, int) and (num > 0):
        return fibonacci2(num)
    else:
        return "Error Capa 8"

def fibonacci2(num):
    if (num == 0):
        return 0
    elif (num == 1):
        return 1
    else:
        print ((num-1) + (num-2))
        return fibonacci2(num-1) + fibonacci2(num-2)
            
