'''Tuple
Tuples are used to store multiple items in a single variable.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.'''

t = (1,2,"dhanu")
print(t)
print(type(t))

print(len(t))
# to crate a single valued tuple use (,) at last so it will accept as a tuple

a=("apple",) # a=("apple") not a tuple
print(a)
print(type(a))

#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.
b = ((1,34,'dhanu'))
print(b)


e=('ab','sd','df','qw')
print(e)
f =list(e)

f[1] = ('apple')
f.append("banana")

 
e =tuple(f)
print(e)

g =('hi','bye')

e += g

print(e)

A = (1,2,3,4,5)
i = 0 
while i < len(A):
    print(A[i])
    i=i+1

for i in A :
    print(i)

for i in range (len(A)):
    print(A[i])




