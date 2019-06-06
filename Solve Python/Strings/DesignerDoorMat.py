'''
Problem: Designer Door Mat
Description: Print the design of a door mat
using "-" and ".|." of size NxM.
N and M must be odd.
Points: 10.


'''

p = input()
n = int(p.split()[0])
m = int(p.split()[1])

for i in range(n//2):
    patt = '.|.'*(2*i+1)
    print(patt.center(m, '-'))

print('WELCOME'.center(m, '-'))

for i in range(n//2-1, -1, -1):
    patt = '.|.'*(2*i+1)
    print(patt.center(m, '-'))
