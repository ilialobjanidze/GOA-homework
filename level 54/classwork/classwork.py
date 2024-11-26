#8 KYU
#1
def make_negative(number):
    if number >= 0:
        return -number
    else:
        return number

#2
def positive_sum(arr):
    total_sum = 0
    for num in arr:
        if num > 0:
            total_sum += num
    return total_sum

#3
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

#4
def find_smallest_int(arr):
    return min(arr)

#5
def string_to_number(s):
    return int(s)

#6
def summation(num):
    return sum(range(1, num + 1))

#7
def stringy(size):
    return ''.join('1' if i % 2 == 0 else '0' for i in range(size))

#8
def count_sheeps(sheep_list):
    return sum(1 for sheep in sheep_list if sheep is True)

#9
def no_space(x):
    return x.replace(' ', '')

#10
def double_integer(i):
    return i * 2

#11
def greet():
    return "hello world!"

#12
def greet(name):
    return f"Hello, {name} how are you doing today?"

#13
def boolean_to_string(b):
    return str(b)

#14
def basic_op(operation, value1, value2):
    if operation == '+':
        return value1 + value2
    elif operation == '-':
        return value1 - value2
    elif operation == '*':
        return value1 * value2
    elif operation == '/':
        return value1 / value2
    else:
        raise ValueError("Invalid operation")

#15
def litres(time):
    return int(time * 0.5)

#16
def century(year):
    return (year + 99) // 100

#17
def maps(a):
    return [x * 2 for x in a]

#18
def digitize(n):
    return [int(d) for d in str(n)][::-1]

#19
def lovefunc(flower1, flower2):
    return (flower1 % 2) != (flower2 % 2)

#20
def sum_array(a):
    return sum(a)


#7 KYU
#1
def disemvowel(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char not in vowels])

#2
def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))
    return f"{max(num_list)} {min(num_list)}"

#3
def descending_order(n):
    return int(''.join(sorted(str(n), reverse=True)))

#4
def is_square(n):
    if n < 0:
        return False
    return int(n**0.5) ** 2 == n

#5
def filter_list(l):
    return [item for item in l if isinstance(item, int)]
