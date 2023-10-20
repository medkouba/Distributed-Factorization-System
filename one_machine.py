import multiprocessing
import time
start=time.time()
def factorize(number):
    factors = []
    for i in range(2, number + 1):
        while number % i == 0:
            factors.append(i)
            number = number // i
        if number == 1:
            break
    return factors

def worker_task(number):
    result = factorize(number)
    return result

if __name__ == '__main__':
    input_numbers = [995658762541,995658762541]
    a=factorize(input_numbers[0])
    b=factorize(input_numbers[1])
    print(a,b)
    print(time.time()-start)
