# This is a program to convert a decimal number to decimal, octal, hex
# by: Nicholas Sycz

num = input("What number do you wish to convert?\n")
if num < 0:
    print "Please enter a positive number."
    exit(1)
base = input("What do you wish to convert to? binary(2), octal(8), or hexadecimal(16)\n")

def hexChars(x):
    if x < 10:
        return chr(ord('0') + x)
    else:
        return chr(ord('A') + x - 10)

def baseConversion(num, base):
    if num > 0:
        d,m = divmod(num, base)
        if d:
            return baseConversion(d, base) + hexChars(m)
        else:
            return hexChars(m)

print ''
print 'Number      Conversion'
print num,'       ', baseConversion(num, base)
