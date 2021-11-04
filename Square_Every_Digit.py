square_digits = lambda num: int(' '.join([str(a) for a in [int(i)**2 for i in str(num)]]).replace(" ", ""))
