# setup
items = range(1, 5)

def sqr(x): return x**2

def cub(x): return x**3

# mapping
mylist=[]
for x in items: 
	mylist.append(sqr(x))
	
mylist=map(sqr, items)
mylist=map(lambda x: x **2, items)

funcs = [sqr, cub]
for i in items:
    value = map(lambda x: x(i), funcs)
    print value

# reducing and filtering
range(-5, 5)
filter((lambda x: x < 0), range(-5,5))

from functools import reduce
reduce( (lambda x, y: x * y), items )

L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']
reduce( (lambda x,y:x+y), L)

reduce( (lambda x,y:x+y), map(len, L))

reduce( (lambda x,y:x+y), map(sqr, items))

def make_incrementor (n): return lambda x: x + n

f = make_incrementor(2)
g = make_incrementor(6)

print f(42), g(42)

nums = range(2, 50) 
for i in range(2, 8): 
    nums = filter(lambda x: x == i or x % i, nums)

print nums

