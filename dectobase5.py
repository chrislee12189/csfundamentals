def dec_to_base(num, base=5):

    digits = []

    quot = num // base
    digits.append(num % base)
    print (digits)
    while quot > (base - 1):
        digits.insert(0, quot % base)
        print(digits)
        quot = quot // base

    digits.insert(0, quot)
    print(digits)
    return "".join(str(e) for e in digits)


print(dec_to_base(300, 5))