#Binary to Decimal conversion program.a
binary = raw_input('enter a in binary: ')
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print decimal,
