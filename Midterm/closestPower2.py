def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    base = int(base)
    num = int(num)
    for exponent in range(0, num):
        if num == base**exponent:
            return exponent
        else:
            exponent_next = exponent + 1
            option1 = abs(num - (base**exponent))
            option2 = abs(num - (base**exponent_next))
            if option1 < option2:
                return exponent
            elif option1 == option2:
                return exponent
            else:
                exponent = exponent_next

print(closest_power(3,12))
print(closest_power(4,12))
print(closest_power(4,1))
print(closest_power(2, 192.0))
print(closest_power(20, 210.0))
