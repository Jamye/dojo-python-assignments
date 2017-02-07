import random
"""
You're going to create a program that simulates tossing a coin 5,000 times.
 Your program should display how many times the head/tail appears.

Sample output should be like the following:
Starting the program...
Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
...
Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
Ending the program, thank you!
Hint:

Use the python built-in round function to convert that floating point number into an integer

Thoughts:
- Loop to iterate the coin flips 5000 times
- Need two counters - one for heads, one for tails
- Need to also keep track of the number of attempts
- Conditionals to separate random numbers
- Print concatenated string
"""

def coin_toss():
    head_counter = 0
    tail_counter = 0
    print "Starting the program..."
    for i in range(5000):
        rand_num = round(random.random())
        if rand_num == 1:
            head_counter += 1
            print "Attempt #" + str(i+1) + ": Throwing a coin... It's a head! ... Got " + str(head_counter) + " head(s) so far and " + str(tail_counter) + " tail(s) so far"
        elif rand_num == 0:
            tail_counter += 1
            print "Attempt #" + str(i+1) + "Throwing a coin... It's a tail! ... Got " + str(head_counter) + "head(s) so far and " + str(tail_counter) + "tail(s) so far"
    print "Ending the program, thank you!"


coin_toss()
