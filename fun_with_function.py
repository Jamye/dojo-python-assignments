"""
Odd/Even:
Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

Your program output should look like below:

Number is 1.  This is an odd number.
Number is 2.  This is an even number.
Number is 3.  This is an odd number.
...
Number is 2000.  This is an even number.
Copy

Multiply:
Create a function called 'multiply' that iterates through each value in a
list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been
multiplied by 5.

The function should multiply each value in the list by the second argument.
For example, let's say:

a = [2,4,10,16]
Copy
Then:

b = multiply(a, 5)
print b
Copy
Should print [10, 20, 50, 80 ].

Hacker Challenge:
Write a function that takes the multiply function call as an argument.
Your new function should return the multiplied list as a two-dimensional
list. Each internal list should contain as many ones as the number in the
original list. Here's an example:

def layered_multiples(arr)
  # your code here
  return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
# output
>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

"""

"""
a function that counts 1-2000
create a loop that iterates
it checks if the input is even or odd
it should print "
Number is 1.  This is an odd number.
Number is 2.  This is an even number.
Number is 3.  This is an odd number."
"""

# def odd_even():
#     for i in range(0, 2000):
#         if i % 2 != 0:
#             print "Number is " + str(i) + ". This is an odd number."
#         else
#             print "Number is " + str(i) + ". This is an even number."
# odd_even()


"""
function that iterates through each value in a list
returns list where each element has been multiplied by 5
5 should be a argment
"""
a = [2,4,3,5]
def multiply(lst, mult):
    for i in range (0, len(lst)):
        lst[i] = lst[i] * mult
    return lst

# multiply(a,5)


"""
Hacker Challenge:
Write a function that takes the multiply function call as an argument.
Your new function should return the multiplied list as a two-dimensional
list. Each internal list should contain as many ones as the number in the
original list. Here's an example:

def layered_multiples(arr)
  # your code here
  return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
# output
>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
"""

#takes previous function as argument
#return the multipled list as a two dimentional array
#create a loop that iteratees through the input
# create a list to store the value
# inner loop takes that value and puts the quantity of 1 as the previous

def hack_challenge(multipliers):

    result = []
    for num in multipliers:
        inside_lst = []
        for j in range(num):
            inside_lst.append(1)
        result.append(inside_lst)
    print result

hack_challenge(multiply(a,3))
