` to save codebase open source control (ctrl + shift + g) and press commit (ctrl + enter) `


## Selection

##### 3.6
#### (09/14/26)

`if` - cond X is **true**

`elif` - cond X is **false**, but cond Y is **true**

`else` - cond X is **false**, and cond Y is **false**.

## The Internet

##### 4.1
#### (09/21/26)

### Internet Protocol (IP) Layering
###### the layers of internet protocols are decending

`application` - HTTP → sends the **message** from point A to point B

`transport` - TCP, UDP → adds a *TCP header* to **direct** the message to the correct application

`network` - IP → adds a *IP header* to direct the message **towards point B** → this is now called a ***packet***

`link` - WiFi, Ethernet → adds a MAC header to **contain the hardware addresses of the immediate local devices**

`physical` - bits "on the wire" → **message sent to point B**

##### if you specialise in a specific layer eg. network, you can only focus on the network layer and not above nor below.

### Transport Protocols

`TCP` - **Transmission Control Protocol** → reliable, congestion control, flow control, is a **lossless** transfer of data

`UDP` - **User Datagram Protocol** → unreliable, unordered delivery, is a **lossy** transfer of data

* all of these are  `metadata`  

___

#### (09/22/26)
### IP Addresses

`IPv4` - a **32bit** identifier associated with each host or router interface

* an IPv4 IP Address that is 76.50.100.235 is `01001100.00110010.01100100.11101011` in binary. ***notice each (group) has 8 bits***

`IPv6` - a **128bit** identifier, associated with each host or router interface

* it is written as eight groups of four hexadecimal digits (characters 0–9 and a–f) separated by colons like `2001:0db8:85a3:0000:0000:8a2e:0370:7334`

    - IPv6 is exactly `2^96` times larger than IPv4 since `2^128/2^32 = 2^(128-32) = 2^96`

___

#### (09/30/26)
##### 3.10
### Arrays (lists)

a `list` can store multiple datatypes at once

```py
grades_array = [76, "test", 42.0000, 1, 100, 82, 59, 94]

print(grades_array[6]) # --> output: 59 
print(grades_array[2]) # --> output: 42.0
print(grades_array[1]) # --> output: test
```

___

#### (10/06/26)
##### 3.8
#### `while True:` loops:

**Q: Identify the error in the following code snippet:**

```py
runLoopForever = input("0 to quit, 1 to loop")

while (runLoopForever = 1)
    print("This loop is running forever")
```

*A<sub>1</sub>: the **`while`** loop is missing a colon at the end of **`while (runLoopForever = 1)`** → Syntax Error* <br>
*A<sub>2</sub>: the **`while (runLoopForever = 1)`** loop has `=` instead of `==` → Logic Error*
<br>
*A<sub>3</sub>: the **`runLoopForever`** variable saved `"1"` and not `1` since `input()` always stores a `string`, therefore it must be casted to an `int` → Logic Error*

**Q: What is the output of the following code snippet:**

```py
counter = 1

while (counter < 5):
    counter += 1

print(counter)
```
*A: The output would be `5` since the **`while (counter < 5)`** loop runs until **`counter == 5`** then prints it via **`print(counter)`** at the end of the code*

**Q: What is the output of the following code snippet:**

```py
counter = 67

while (counter > 10):
    counter /= 2

print(counter)
```
*Work: Check if `counter > 10`: 67 > 10, then 67/2  = 33.5, <br>
Check if `counter > 10`: 33.5 > 10, then 33.5/2  = 16.75, <br>
Check if `counter > 10`: 16.75 > 10, then 16.75/2  = 8.375 <br>
Check if `counter > 10`: 8.375 < 10, then Stop Iterating <br>*

*A: The output would be `8.375` since the 

**Q: What is the output of the following code snippet:**

```py
counter = 5

while (counter < 100):
    counter += 2
    counter -= 1

print(counter)
```

*Work: simplify the inside, `2-1 = 1` so `counter` increases by `1` per iteration (`counter += 1`) <br>
`counter = 5 + 1 = 6 + 1 = 7 + 1 = 8 + ... = counter = 100`

*A: The output will be `100` since the `while True` loop runs continously until `counter` reachers `100` as the conditional `counter < 100` so if `counter = 100`, you stop iterating.*

**Q: What is the output of the following code snippet:**

```py
counter = 256

while (counter > 10):
    if (counter < 50):
        counter /= 2
    else:
        counter =/ 4
print(counter)
```
*Work: first check the conditions `counter > 10` and then `counter < 50`, while `counter > 10`, execute the `else` block which divides `counter` by `4`. since `256 > 50` <br> <br>
`256 / 4 = 64 / 4 = 16 → STOP` <br> <br>
now since `(counter < 50)`, execute the `if (counter < 50)` block which divides `counter` by `2` since `16 < 50` <br> <br>
`16 / 2 = 8 → STOP`
now since the `while (counter > 10)` conditional is false, stop the entire loop and print the result*

