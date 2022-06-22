# question-1
'''the two values for boolean data types are
    True=1 and False=0'''
# to write this we use:
a=10
b=20
print(bool(a==b))

# question-2
''' In the python 3 boolean opeartor are:
    and, or, not'''
# question-3
''' False
    False
    True
    False
    False
    True'''
# question-4
'''Python has six comparison operators,:
Less than ( < )
Less than or equal to (<=)
Greater than (>)
Greater than or equal to (>=)
Equal to ( == )
Not equal to ( != )
'''
# question-5
'''the diffrence between equal to and assignment operator
    equal operator (==)
    this operator is used when we can check that both have same value or not.

    assignment operator (=)
    this operator is used to assign the value to a variable at the memory address inside the hardware'''
# demonstration of equal operator:
m_title='kapoor'
f_title='kapoor'
if m_title==f_title:
    print("this is my son of "+m_title+" family")
else:
    print('this is not my blood')
# demonstration of assignment operator:
f_title='kapoor'
m_title=f_title
print(m_title)

# question 7
spam = 0
if spam == 10:
    print('egg')
    if spam> 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')

# question 8
a=3
if a==1:
    print('Hello')
elif a==2:
    print('Howdy')
else:
    print("greeting")

#question-9
''' Press ctrl-C to stop a program stuck in an infinite loop.'''
# question-10
'''the diffrence between break and continue
   break keyword stop the further execution of the code inside the loop
   The continue keyword is used to end the current iteration in a for loop, and continues to the next iteration.'''
# continue
for i in range(5):
  if i == 3: # skips if i is 3
    continue
  print(i)
# break
print()
for x in range(7):
    print(x)
    if x > 3:
        break
print()
# question-11
for i in range(10):
    print(i)
print()
for i in range(0,10):
    print(i)
print()
for i in range(0,10,1):
    print(i)
print()
''' In the range function there are 3 argument are possible out there.
    range(10) here we are only give lower bound value which value are excluded inside the range
    range(0,10) here we are given the lower bound value=0 and upper bound value=10
    range(0,10,1) here it's given lower bound, upper bound and number of steps should be taken '''

# question-12
# for loop
print('for loop')
for i in range(1,11):
    print(i)
print()
# while loop
print('while loop')
i=1
while i<11:
    print(i)
    i=i+1

# question-13
'''This function can be called with spam.bacon().'''

















