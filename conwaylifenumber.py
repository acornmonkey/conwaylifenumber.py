import math
arr = []
#Conway's Game of Life number:
for i in range(512):
    if i.bit_count() == 3 or (i.bit_count() == 4 and (i >> 4) & 1 == 1):

#Simpler example (Rule 94):
#for i in range(8):
#    if i.bit_count() == 1 or (i.bit_count() == 2 and (i >> 1) & 1 == 1):

        arr.append(i)
num = 0
for i in arr:
    num += 2**i
print('Decimal:')
print(num)
print('\nBinary:')
print(bin(num))
print('\nDecimal log:')
print(math.log(num,10))
print('\nBinary log (in decimal):')
print(math.log(num,2))
