` to save codebase open source control (ctrl + shift + g) and press commit (ctrl + enter) `

## Table of Contents
- [Booleans & Truth Tables (3.5)](#booleans--truth-tables)
    - [truth table code](#truth-table-code)
- [If-Then-Else Practice (3.6)](#more-if-then-else-practice)
- [Nested If-Then-Else Practice (3.7)](#more-nested-if-then-else-practice)

---


## Booleans & Truth Tables

#### `boolean` → T/F statements

#### (10/13/26)
##### 3.5

##### `not` → negation/inversion
```py
A = 4+2

if not A > 5:
    print("a") 
else:
    print("b")

# output: since 6>5, this will be True; however, the `not` would inverse it so it would be false, negating the if block and printing "b"   
```
##### `and` → inclusion (X and Y needs to be true for the entire expression to be true)
```py
while True:

    A = int(input("enter num 1: "))
    B = int(input("enter num 2: "))
    C = B
    
    if A == B and A == C:
        print("you assigned A and B the same value")
    else:
        print("you have assigned different values to A and B")

# output: since C = B, the if statement is comparing if A is equal to B **and** if A is equal to B: if they are both equal, the if block will play; else, if they are false, the else block will play.
```
##### `or` → diversion (X or Y needs to be true to be true)
```py
while True:
    
    A = int(input("enter num 1: "))
    B = int(input("enter num 2: "))
    
    if A >= 1000 or B >= 1000:
        print("one (or both) of your numbers are greater than 1000")
    elif A >= 100 or B >= 100:
        print("one (or both) of your numbers are greater than 100")
    elif A >= 10 or B >= 10:
        print("one (or both) of your numbers are greater than 10")
    else:
        print("none of your numbers are greater than 10, 100, or 1000")
        
# output: if A **or** B is greater than 10, 100, or 1000, it will print its respective if else block.
```

## Truth Table(s)
###### AP CSP 3.5
#### not A and B
| A | B | (`not` A) `and` B |
| :--- | :--- | :--- |
| True | True | False |
| False | False | False |
| True | False | False |
| False | True | True |

---
###### (10/06/26)

#### not (A and B)
| A | B | `not` (A `and` B) |
| :--- | :--- | :--- |
| True | True | False |
| False | False | True |
| True | False | True |
| False | True | True |

---

#### (not A) or (not B)
| A | B | (`not` A) | (`not` B) | (`not` A) `or` (`not` B) |
| :--- | :--- | :--- |  :--- | :--- | 
| True | True | False | False | False |
| False | False | True | True | True |
| True | False | False | True | True | 
| False | True | True | False | True |

---
### truth table code

### `and`

```py
"""
A(6,7)
B(4,2)
C(100,1)
D(1,100)
"""

x = int(input("put a value for x"))
y = int(input("put a value for y"))

if x < 6 and y >= 7:
    print("Success!")
else:
    print("failure :(")

"""
output:

A(6,7):
    Since x = 6, and y >= 7, only one of those are True. Since it is bounded by a `and` operator, the entire would evaluate to False; as a result, trigging the else block

B(4,2):
    since x < 6, and y < 7, only one of those are True. Since it is bounded by a `and` operator, the entire would evaluate to False; as a result, trigging the else block

C(100,1):
    since x > 6, and y < 7, both of these are False. Since it is bounded by a `and` operator, the entire would evaluate to False; as a result, trigging the else block

D(1,100):
    since x < 6, and y >= 7, both of these are True. Since it is bounded by a `and` operator, the entire would evaluate to True; as a result, trigging the if block

"""
```

---
### `or`

```py
"""
A(6,7)
B(4,2)
C(100,1)
D(1,100)
"""

x = int(input("put a value for x"))
y = int(input("put a value for y"))

if x < 6 or y >= 7:
    print("Success!")
else:
    print("failure :(")

"""
output:

A(6,7):
    Since x = 6, and y >= 7, only one of those are True. Since it is bounded by a `or` operator, only one of these needs to be True to make the entire expression True. As a result, it is True and triggers the if block.

B(4,2):
    since x < 6, and y < 7, only one of those are True. Since it is bounded by a `or` operator, only one of these needs to be True to make the entire expression True. As a result, it is True and triggers the if block.

C(100,1):
    since x > 6, and y < 7, both of these are False. Since it is bounded by a `or` operator, only one of these needs to be True to make the entire expression True. As a result, it is False and triggers the else block.

D(1,100):
    since x < 6, and y >= 7, both of these are True. Since it is bounded by a `or` operator, only one of these needs to be True to make the entire expression True. As a result, it is True and triggers the if block.

"""
```

## more if-then-else practice
#### 10/27/26
###### AP CSP 3.6

### code 1:

```py
cheese = 2
peanutButter = 7

cheese = cheese + 3 # makes cheese = 5
peanutButter -= 2 # makes peanutButter = 5

if cheese > peanutButter: # 5>5 is false
    print(cheese % 2)
else:
    print(peanutButter % 3) # 5 mod 3 = 2

cheese = 1/(cheese - peanutButter) # nukes the entire code resulting in a runtime error in a zerodivision error

print(peanutButter) # supposed to print 5 but doesnt due to the error

# this code segment prints "2"
```

### code 2:

```py
#fill in the blank

if ___________:
    print("your integer is divisible by 2")

____ _________: 
    print("your integer is divisible by 3")

# ---------------------------------------------------------

# filled in code:

if number % 2 == 0: # if a number n when divided by 2 (denominator) is equal to 0, it is divisible by 2. eg 14 % 2 = 0 is 14/2 = 0 remainder. This makes 14 divisible by 0
    print("your integer is divisible by 2")

elif number % 3 == 0: # if a number n when divided by 3 (denominator) is equal to 0, it is divisible by 3. eg 33 % 3 = 0 is 33/3 = 0 remainder. This makes 33 divisible by 3
    print("your integer is divisible by 3")

```

## more nested if else practice
#### 10/28/26
###### AP CSP 3.7

### code 1:

```py
# Question: what are all of the (x,y) pairs that give each status message?

x = int(input("X: "))
y = int(input("Y: "))
status = "N/A"

if x > 10:
    if y < 15:
        if x == (y + 4):
            status = "Approved"
        else:
            status = "Review"
    else:
        status = "Rejected"
else:
    if x > 5:
        status = "Hold"
    else:
        status = "Denied"

print(status)

# Approved: (18,14)
# Review: (11,6)
# Rejected: (55,55)
# Hold: (7,10)
# Denied: (2,200)
```
### code 2:

```py
"""
A smart home unlocks the door if either a recognized face or a valid code is detected (provided the alarm is not active)

If the alarm is active, and the face is not recognized, access is denied

Otherwise the request is on hold
"""

face_recognized = input("Face recognized:  ")
valid_code = input("Valid Code:  ")
alarm_active = input("Alarm Active:  ")

status = ""

if (face_recognized or active_code) and not alarm_active:
    status = "Access Granted!"

elif not face_recognized and alarm_active:
    status = "Access Denied..."

else:
    print("Hold")

print(status)
```

`last updated: 10/28/26`