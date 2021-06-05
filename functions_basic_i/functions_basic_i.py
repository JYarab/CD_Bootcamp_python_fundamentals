#1 - Console output: 5
def a():
    return 5
print(a())

#2 - Console output: 10
def a():
    return 5
print(a()+a())

#3 - Console output: 5
def a():
    return 5
    return 10
print(a())

#4 - Console output: 5
def a():
    return 5
    print(10)
print(a())

#5 - Console output: 5 - Wrong actual output also prints None as value of x 
def a():
    print(5)
x = a()
print(x)

#6  - Console output: 3, 5, 8 - Wrong actual output 3,5 Error since function does not return value cannont add and print
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

#7  - Console output: 25 as string
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#8  - Console output: 100, 10
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
	    return 10
    return 7
print(a())

#9  - Console output: 7, 14, 21
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#10 - Console output: 8
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#11 - Console output: 500, 500, 300, 300 - final print is 500 again b = inside function does not return so b remains 500 outside of function... I think... see num 12 nope....
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#12 - Console output: 500, 500, 300, 300 - final print is 500 again return does no set b outside of function?
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#13 - Console output: 500, 500, 300, 300 - correct now since b is redefined as function return prior to last print
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#14 - Console output: 1, 3, 2
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#15 - Console output:1, 3, 5, 10
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

