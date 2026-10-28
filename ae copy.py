import random

unique_numbers = random.sample(range(1, 101), 30)
x = unique_numbers[:10]
y = unique_numbers[10:20]
z = unique_numbers[20:30]


print(sorted(x))
print(sorted(y))
print(sorted(z))

res1 = x[0]+y[0]+z[0]
res2 = x[1]-y[1]-z[1]
res3 = x[2]*y[2]*z[2]
res4 = x[3]/y[3]/z[3]
res5 = x[4]+y[4]+z[4]
res6 = x[5]-y[5]-z[5]
res7 = x[6]*y[6]*z[6]
res8 = x[7]/y[7]/z[7]
res9 = x[8]+y[8]+z[8]
res10 = x[9]-y[9]-z[9]
res = [res1,res2,res3,res4,res5,res6,res7,res8,res9,res10]
final_res = res
print(final_res)
index = final_res[0]
index1 = final_res[1]
index2 = final_res[2]
index3 = final_res[3]
index4 = final_res[4]
index5 = final_res[5]
index6 = final_res[6]
index7 = final_res[7]
index8 = final_res[8]
index9 = final_res[9]

x = final_res[:3]
y = final_res[3:6]
z = final_res[6:9]

print(sorted(x))
print(sorted(y))
print(sorted(z))
c1 = [sorted(x)[0], sorted(y)[0]]
c2 = [sorted(x)[1],sorted(y)[1]]
c3 = [sorted(x)[2],sorted(y)[2]]


depth0 = sorted(z)[0]
depth1 = sorted(z)[1]
depth2 = sorted(z)[2]
pro_solve = [c1,depth0]
pro_solve1 = [c2,depth1]
pro_solve2 = [c3,depth2]
print(pro_solve)
print(pro_solve1)
print(pro_solve2)

z = [depth0,depth1,depth2]
x = [c1[0],c2[0],c3[0]]
y = [c1[1],c2[1],c3[1]]

print(sorted(x))
print(sorted(y))
print(sorted(z))

sol_z = z[0]
sol_x = x[0]
sol_y = y[0]

print(sol_x, sol_y, sol_z)

z = sol_x * sol_y / 2
sol_x = int(round(sol_x))
sol_y = int(round(sol_y))
z = int(round(z))
print(sol_x,"*",sol_y,"/ 2 = ",z)