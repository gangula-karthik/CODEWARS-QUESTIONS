def reverse_list(x):
    """
    >>> reverse_list([1,2])
    [2, 1]
    >>> reverse_list([4,7,10])
    [10, 7, 4]
    """
    
    return (x)[::-1]

def sum_list(x):
    """
    >>> sum_list([1,2,3])
    6
    >>> sum_list([4,5,6])
    15
    """
    if x != None:
        return sum(x)
    else:
        pass

def head_of_list(x):
    """
    >>> head_of_list([1,2])
    1
    >>> head_of_list([4,7,10])
    4
    """
    
    if x != None: 
        for i in x:
            return i
    else:
        return None
