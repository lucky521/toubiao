
from sympy import *
x = symbols('x')

max = 1
max_i = 1

# v is my bid price
# x is possible base price
# y is my score
# result is the probability of score when I choose a v

for i in range(0, 100):
	v = 90 + i / 10

	y1 = 45 + (x - v) * 100 / x

	y2 = 60 - 200 * (x - v) / x

	result1 = integrate(y1, (x, 90, v/1.05))

	result2 = integrate(y2, (x, v/1.05, 100))

	result = (result1 + result2).evalf()

	print("v=",v," result=",result,"\n")
	if max < result:
		max = result
		max_i = v

print("MAX v=",max_i," result=",max,"\n")
