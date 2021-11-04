def number(lines):
    x, lst = 0, []
    for i in lines:
        x +=1
        lst.append(("{}: {}").format(x, i))
    return lst
  

#my refactored solution with enumerate() implemented
#enumerate adds a counter to an iterable and return it
#i can specify my starting value for the counter and in this case i will set it to 1 but default is 0
def number(lines):
    return ["{}: {}".format(iterable,counter) for (iterable, counter) in enumerate(lines, 1)]

#the first problem that arises when i do return (list(enumerate(lines, 1))) is that each value in the list is a tuple
