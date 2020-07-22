#backslash

#txt = "We are the so-called "Vikings" from the north."         #gives error
#print(txt)
txt = "We are the so-called \"Vikings\" from the north."
print(txt);

#Triple quotes
para_str = """this is a long string that is made up of several lines and
 non-printable characters such as TAB ( \t ) and they will show up that way when displayed.
  NEWLINEs within the string, whether explicitly given like this within the brackets [ \n ],
   or just a NEWLINE within the variable assignment will also show up.
"""
print(para_str);

double_quotes = '"abc"'
print(double_quotes);

single_quotes= "'abc'"
print(single_quotes);

both_quotes= """a'b"c"""
print(both_quotes);

#escape sequence with string
double_quotes = "\"abc\""
print(double_quotes);

single_quotes = '\'abc\''
print(single_quotes);



#formated output with python
# print integer and float value
print("Geeks : % 2d, Portal : % 5.2f" % (1, 05.333))

# print integer value
print("Total students : % 3d, Boys : % 2d" % (240, 120))


# print octal value
print("% 7.3o" % (25))

# print exponential value
print("% 10.3E" % (356.08977))

# Python variable
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print(counter)
print(miles)
print(name)

str = 'Hello World!'

print str          # Prints complete string
print str[0]       # Prints first character of the string
print str[2:5]     # Prints characters starting from 3rd to 5th
print str[2:]      # Prints string starting from 3rd character
print str * 2      # Prints string two times
print str + "TEST" # Prints concatenated string

## Python arithmatic  operator
x = 15
y = 4

# Output: x + y = 19
print('x + y =',x+y)

# Output: x - y = 11
print('x - y =',x-y)

# Output: x * y = 60
print('x * y =',x*y)

# Output: x / y = 3.75
print('x / y =',x/y)

# Output: x // y = 3
print('x // y =',x//y)

# Output: x ** y = 50625
print('x ** y =',x**y)

// comparison operator

x = 10
y = 12

# Output: x > y is False
print('x > y is',x>y)

# Output: x < y is True
print('x < y is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)

##Logical operator
x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)

## Identity operator

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)

##Membership operator
x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)



# bitwise operators

a = 10
b = 4

# Print bitwise AND operation
print("a & b =", a & b)

# Print bitwise OR operation
print("a | b =", a | b)

# Print bitwise NOT operation
print("~a =", ~a)

# print bitwise XOR operation
print("a ^ b =", a ^ b)

# Output: True
print(1 in y)

# Output: False
print('a' in y)


##### Python assignment Operator
a = 21
b = 10
c = 0

c = a + b
print "Line 1 - Value of c is ", c

c += a
print "Line 2 - Value of c is ", c

c *= a
print "Line 3 - Value of c is ", c

c /= a
print "Line 4 - Value of c is ", c

c  = 2
c %= a
print "Line 5 - Value of c is ", c

c **= a
print "Line 6 - Value of c is ", c

c //= a
print "Line 7 - Value of c is ", c


##### Operator Precedence

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d       #( 30 * 15 ) / 5
print "Value of (a + b) * c / d is ",  e

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print "Value of ((a + b) * c) / d is ",  e

e = (a + b) * (c / d);    # (30) * (15/5)
print "Value of (a + b) * (c / d) is ",  e

e = a + (b * c) / d;      #  20 + (150/5)
print "Value of a + (b * c) / d is ",  e