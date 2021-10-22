#Task 1
def is_palindrom(num):
    return str(num) == ''.join(reversed(str(num)))
    
print(is_palindrom(789))
print(is_palindrom(1234321))
print(is_palindrom(5665))

#Task 2 
def get_divisible(num_list):
    d2 = []
    d3 = []
    d5 = []
    for num in num_list:
        if num % 2 == 0:
            d2.append(num)
        if num % 3 == 0:
            d3.append(num)
        if num % 5 == 0:
            d5.append(num)
            
    return d2, d3, d5

test_list = range(1, 25)
print(get_divisible(test_list))

#Task 3 
def get_reversed(num):
    if num < 0:
        return int("-" + str(num)[:0:-1])
    else:
        return int(str(num)[::-1])

print(get_reversed(-123))
print(get_reversed(120))
print(get_reversed(0))
print(get_reversed(123))

#Task 4 
def get_nth_root(root, num, eps = 0.0001):
    x = 1
    def f(x):
        return x ** root - num
        
    def dif_f(x):
        return root * x ** (root - 1)
        
    temp = abs(f(x))
    while temp > eps:
        x = x - f(x) / dif_f(x)
        temp = abs(f(x))
        
    return x

print(get_nth_root(2, 1024))
print(get_nth_root(3, 27))
print(get_nth_root(4, 16))

#Task 5 
def is_prime(num):
    temp = 2
    while temp <= num / 2:
        if num % temp == 0:
            return False
            
        temp += 1
        
    return True
    
print(is_prime(7))
print(is_prime(9))
print(is_prime(2))
print(is_prime(4))

#Task 7 
def counted_cache(counter):
    def cached(func):
        cache = {}
        
        def wrapper(*args):
            if (args not in cache) or (counter == 0):
                cache[args] = func(*args)
                counter = 3 
            
            counter -= 1
            return cache[args]
        
        return wrapper
    
    return cached
    
@counted_cache(3)
def do_stuff(data):
    return data