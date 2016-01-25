foods = ['bacon', 'chicken', 'beans', 'lamb', 'beef']

# for loop
for f in foods[:2]:
    print(f)
    print(len(f))

randomNum = 34

for n in range(1001):
    if n is randomNum:
        print('randomNum is found', n + randomNum)
        break
    else:
        print(n)

for n in range(100):
    if n % 4 is 0:
        print('this number can be divided by 4 without reminder ', n)
    else:
        print(n)