import timeit
def fizzbuzz(numbers):
    
    if not isinstance(numbers,list):
        raise ValueError(f'Expecting list. But {numbers} is invalid')
    # map way, map return map objct
    # temp = map(f,numbers)
    # return list(temp)
    # list comprehension way
    return [f(x) for x in numbers]
    
    
def f(x): 
    if x % 3 ==0 and x % 5 == 0:
        return 'fizzbuzz'
    if x % 3 ==0:
        return 'fizz'
    if x % 5 == 0:
        return 'buzz'
    return x

test_numbers = [45,35,33,22,100]
test_number = 45

if (__name__ == "__main__"):
    print(fizzbuzz(test_numbers))
    t = timeit.Timer(lambda : fizzbuzz(test_numbers))
    print(t.timeit(number=1000))
