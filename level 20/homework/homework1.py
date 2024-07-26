#დავალება 1 
int1 = 92
int2 = 14
print(int1 + int2)
#დავალება 2 
str1 = "GOA"
str2 = "Academy"
print( str1 + str2 ) # We use + Symbol to merge two string together, its called concatenation
#დავალება 3 
int3 = 36
int4 = 6           #implict
print(int3 / int4) #when we divide two integers it result might be non ineteger , t
#he result is automatically promoted to a more general type that can represent both integers and float numbers

#დავალება 4 
int5 = 41
int6 = 19
print(int5 > int6)
print(int5 < int6)
print(int5 == int6)
print(int5 != int6)
print(int5 <= int6)
print(int5 >= int6)

#დავალება 5 
print(13 + 12 == 18 + 7)
print(192 + 210 != 391/ 3)
print(12 * 39 == 52 * 9)

#დავალება 6
True and False and True
False and False and False
True or False or False
False or False or False
not True 
not False

#დავალება 7
int7 = 15
int8 = 32
print(int7 < int8 or True or True)
print(int7 * int8 > 9 and True and False)
print(int7 != int8 or False or True or False)
print(int8 == int7  and True and True and False)
print(False or False or int7 < int8 or True)

#დავალება 8
for i in range(11):
    print(i)

#დავალება 9

numbers = [51, 72, 13, 91, 82]

total = 0
for number in numbers:
    total += number

print(total)

#დავალება 10
str1 = "Hello World!"
for i in str1: 
    print(i)

#დავალება 11 
num9 = 1
while num9 <= 10:
    print(num9)
    num9 += 1

#დავალება 12

number = 1
while number <= 100:
    if number >= 50 and number <= 60:
        number += 1
        continue
    print(number)
    number += 1


#დავალება 13

total1 = 0
number1 = 1

while total < 50:
    total += number
    print(number)
    number += 1

#დავალება 14

def does_it_divide_by_(num):
    if num % 3 == 0 and num % 5 == 0:
        print("იყოფა!")
    elif num % 3 == 0:
        print("იყოფა!")
    elif num % 5 == 0:
        print("იყოფა!")
    else:
        print("არ იყოფა!")

does_it_divide_by_(2)

#დავალება 15
def average_of_list(nums):
    if len(nums) == 0:
        return 0  # 
    
    total_sum = sum(nums)  
    average = total_sum / len(nums)  
    
    return average

test_list = [1, 3, 4, 5, 2]
result = average_of_list(test_list)
print(f"The average of the list {test_list} is: {result}")


#დავალება 17

def square_elements(nums):
    squared_list = [num ** 2 for num in nums]
    return squared_list


numbers = [1, 2, 3, 4, 5]
squared_numbers = square_elements(numbers)
print(f"Original list: {numbers}")
print(f"Squared list: {squared_numbers}")
