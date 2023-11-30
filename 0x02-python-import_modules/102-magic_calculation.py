#!/usr/bin/python3
def magic_calculation(m, n):
    from magic_calculation_102 import add, sub
    if m < n:
        c = add(m, n)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else:
        return(sub(m, n))
