import random

unique_numbers = random.sample(range(1, 101), 20)
x = unique_numbers[:10]
y = unique_numbers[10:20]

c1 = [sorted(x)[0], sorted(y)[0]]
c2 = [sorted(x)[1],sorted(y)[1]]
c3 = [sorted(x)[2],sorted(y)[2]]

x = [c1[0],c2[0],c3[0]]
y = [c1[1],c2[1],c3[1]]

sol_x = x[0]
sol_y = y[0]

print(sol_x, sol_y)

z = sol_x * sol_y / 2
sol_x = int(round(sol_x))
sol_y = int(round(sol_y))
z = int(round(z))
print(sol_x,"*",sol_y,"/ 2 = ",z)