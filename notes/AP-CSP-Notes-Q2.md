` to save codebase open source control (ctrl + shift + g) and press commit (ctrl + enter) `

## Table of Contents
- [Booleans & Truth Tables](#booleans--truth-tables)
    - [truth table code](#truth-table-code)

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

`last updated: 10/20/26 10:02AM`