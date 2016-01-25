houseNumbers = [2, 34, 56, 78, 53, 89, 102]

print('There are available houses in the street')

for n in range(1, 102):
    if n in houseNumbers:
        # continue means if the "if" statement is true
        # the "continue" keyword allows to do the next iteration
        print('inside of the if statement just right before the continue', n)
        continue
        print('This line never to be printed')
    print('outside of the if statement', n)