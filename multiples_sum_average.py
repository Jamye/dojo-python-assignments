"""

This assignment has several parts. All of your code should be in one file that
is well commented to indicate what each block of code is doing and which problem
you are solving. Don't forget to test your code as you go!

Multiples:

Part I
Write code that prints all the odd numbers from 1 to 1000. Use the for loop and
don't use an array to do this exercise.

Part II
Create another program that prints all the multiples of 5 from 5 to 1,000,000.

Sum List
Create a program that prints the sum of all the values in the list:
a = [1, 2, 5, 10, 255, 3]

Assignment: Average List
Create a program that prints the average of the values in the list:
a = [1, 2, 5, 10, 255, 3]

"""

def new_loop():
    for i in range(0, 1001):
        if i % 2 != 0:
            print i
new_loop()


def multiples_of_five():
    count = 5
    while count <= 1000000:
        print count,
        count += 5
multiples_of_five()


a = [1, 2, 5, 10, 255, 3]
def sum_list(numbers):
    sum = 0
    for i in range (0, len(numbers)):
        sum = sum + numbers[i]
    print sum
sum_list(a)



a = [1, 2, 5, 10, 255, 3]
def print_avg(numbers):
    sum = 0
    for i in range (0, len(numbers)):
        sum = sum + numbers[i]
    print sum/len(numbers)
print_avg(a)
