# m_str = "If monkeys like bananas, then I must be a monkey!"
#
# def findAndReplace(random_str):
#     count = 0
#     while count < len(random_str):
#         print random_str.find("monkey")
#         count +=1
# findAndReplace("If monkeys like bananas, then I must be a monkey!")



x = [2,54,-2,7,12,98]

def my_min(x):
    print min(x)
my_min(x)

def my_max(x):
    print max(x)
my_max(x)


y = ["hello",2,54,-2,7,12,98,"world"]
def first_and_last(y):
    new_list = []
    new_list.append(y[0])
    new_list.append(y[-1])
    print new_list

first_and_last(y)

"""
Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6].
Sort it, then slice out all of the values that are negative, placing
those values in a new list. Then add your new list into the original
one at position 0. The output should
be: [[-3, -2], 2, 6, 7, 10, 12, 19, 32, 54, 98]. This one is tough!

-sort out the list
-loop through the list
-if num < 0, slice it out
-put the sliced negative numbers into a new list
-add the new list back into position 0
"""



lst = [19,2,54,-2,7,12,98,32,10,-3,6]

def take_out_negs(lst):
    lst.sort()

    neg = []
    i = 0
    while i < range(len(lst)):
        if lst[i] <= 0:
            neg.append(lst[i])
            lst = lst[i+1:]
        else:
            break
    lst.insert(0,neg)

    return lst


take_out_negs(lst)
