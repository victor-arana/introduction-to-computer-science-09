g = 4
x = 25
epsilon = 0.1
while abs( x - g**2 ) <= epsilon:
    g = (g + x/g)/2
print('guess:', g)
