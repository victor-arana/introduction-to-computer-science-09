g = 3 
x = 16 
epsilon = 0.1
print("x:", x, "g:", g, "g^2:", g**2, "diff:", abs(x - g**2))
while abs( x - g**2 ) > epsilon:
    print("x:", x, "g:", g, "g^2:", g**2, "x/g:", x/g, "(g + x/g)/2", (g + x/g)/2,"diff:", abs(x - g**2))
    g = (g + x/g)/2
print("x:", x, "g:", g, "g^2:", g**2, "x/g:", x/g, "(g + x/g)/2", (g + x/g)/2,"diff:", abs(x - g**2))
    
