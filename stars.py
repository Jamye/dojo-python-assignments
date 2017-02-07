x = [4,"hillman",10,"ow",5]

# def star(x):
#     for i in range (0, len(x)):
#         print x[i] * "*"
# star(x)



def star_p2(x):
    for i in range (0, len(x)):
        if type(x[i]) == int:
            print x[i] * "*"
        else:
            x[i] = x[i][0] * len(x[i])
            print x[i].lower()
star_p2(x)
