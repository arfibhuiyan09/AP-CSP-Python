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

### **Q1: Identify all errors in the following code snippet:**

```python
runLoopForever = input("0 to quit, 1 to loop")

while (runLoopForever = 1)
    print("This loop is running forever")
```

#### **Error Analysis:**

| Line | Code Segment | Error Type | Explanation |
| :--- | :--- | :--- | :--- |
| **3** | `while (runLoopForever = 1)` | **SyntaxError** | Missing a colon `:` at the end of the `while` header. |
| **3** | `runLoopForever = 1` | **SyntaxError** | Uses `=` (assignment) instead of `==` (equality comparison). |
| **1** | `input(...)` | **Logic Error** | `input()` returns a string (e.g., `"1"`). Comparing string `"1"` to integer `1` evaluates to `False`, preventing execution. |

#### **Corrected Code:**
```python
runLoopForever = int(input("0 to quit, 1 to loop"))

while runLoopForever == 1:
    print("This loop is running forever")
```

---

### **Q2: What is the output of the following code snippet?**

```python
counter = 1

while counter < 5:
    counter += 1

print(counter)
```

#### **Execution Trace:**

| Iteration | Condition (`counter < 5`) | Action (`counter += 1`) | New `counter` Value |
| :--- | :--- | :--- | :--- |
| **Start** | — | Variable initialized | `1` |
| **1** | `1 < 5` (**True**) | `1 + 1` | `2` |
| **2** | `2 < 5` (**True**) | `2 + 1` | `3` |
| **3** | `3 < 5` (**True**) | `3 + 1` | `4` |
| **4** | `4 < 5` (**True**) | `4 + 1` | `5` |
| **5** | `5 < 5` (**False**) | **Loop Terminates** | `5` |

#### **Answer:**
```text
5
```

---

### **Q3: What is the output of the following code snippet?**

```python
counter = 67

while counter > 10:
    counter /= 2

print(counter)
```

#### **Execution Trace:**

| Iteration | Condition (`counter > 10`) | Action (`counter /= 2`) | New `counter` Value |
| :--- | :--- | :--- | :--- |
| **Start** | — | Variable initialized | `67` |
| **1** | `67 > 10` (**True**) | `67 / 2` | `33.5` |
| **2** | `33.5 > 10` (**True**) | `33.5 / 2` | `16.75` |
| **3** | `16.75 > 10` (**True**) | `16.75 / 2` | `8.375` |
| **4** | `8.375 > 10` (**False**) | **Loop Terminates** | `8.375` |

#### **Answer:**
```text
8.375
```

---

### **Q4: What is the output of the following code snippet?**

```python
counter = 5

while counter < 100:
    counter += 2
    counter -= 1

print(counter)
```

#### **Explanation:**
The inner block (`counter += 2` followed by `counter -= 1`) results in a net increment of **`+1` per iteration**.

#### **Key Execution Points:**
* **Start:** `counter = 5`
* **Final Iteration Check:** When `counter = 99`, the condition `99 < 100` evaluates to **True**.
* **Body Execution:** `counter` becomes `99 + 2 - 1 = 100`.
* **Loop Exit:** Next check evaluates `100 < 100` (**False**). The loop stops.

#### **Answer:**
```text
100
```

---

### **Q5: What is the output of the following code snippet?**

```python
counter = 256

while counter > 10:
    if counter < 50:
        counter /= 2
    else:
        counter /= 4

print(counter)
```

#### **Execution Trace:**

| Iteration | `while counter > 10` | `if counter < 50` | Action Taken | New `counter` Value |
| :--- | :--- | :--- | :--- | :--- |
| **Start** | — | — | Variable initialized | `256` |
| **1** | `256 > 10` (**True**) | `256 < 50` (**False**) | `else`: `256 / 4` | `64.0` |
| **2** | `64.0 > 10` (**True**) | `64.0 < 50` (**False**) | `else`: `64 / 4` | `16.0` |
| **3** | `16.0 > 10` (**True**) | `16.0 < 50` (**True**) | `if`: `16 / 2` | `8.0` |
| **4** | `8.0 > 10` (**False**) | — | **Loop Terminates** | `8.0` |

#### **Answer:**
```text
8.0
```

---

### **Q6: What is the output of the following code snippet?**

```python
counter = 1
test_list= []

while (counter < 10):
    test_list.append(counter)
    counter += 1

print(test_list)
```

#### **Execution Trace:**

| Iteration | `while counter < 10` | Action Taken | New `counter` Value |
| :--- | :--- | :--- | :--- |
| **Start** | — | Variable initialized | `1` |
| **1** | `1 < 10` (**True**) | `test_list.append(1)`; `counter += 1` | `2` |
| **2** | `2 < 10` (**True**) | `test_list.append(2)`; `counter += 1` | `3` |
| **3** | `3 < 10` (**True**) | `test_list.append(3)`; `counter += 1` | `4` |
| **4** | `4 < 10` (**True**) | `test_list.append(4)`; `counter += 1` | `5` |
| **5** | `5 < 10` (**True**) | `test_list.append(5)`; `counter += 1` | `6` |
| **6** | `6 < 10` (**True**) | `test_list.append(6)`; `counter += 1` | `7` |
| **7** | `7 < 10` (**True**) | `test_list.append(7)`; `counter += 1` | `8` |
| **8** | `8 < 10` (**True**) | `test_list.append(8)`; `counter += 1` | `9` |
| **9** | `9 < 10` (**True**) | `test_list.append(9)`; `counter += 1` | `10` |
| **10** | `10 < 10` (**False**) | **Loop Terminates** | `10` |

#### **Answer:**
```text
[1,2,3,4,5,6,7,8,9]
```

---

### **Q7: What is the output of the following code snippet?**

```python
counter = 0
test_list = ["start"]

while (counter < 10):
    test_list.append(counter)
    counter += 2

test_list.append("end")
print(test_list)
```

#### **Execution Trace:**


| Iteration | `while counter < 10` | Action Taken | New `counter` Value |
| :--- | :--- | :--- | :--- |
| **Start** | — | Variables initialized | `0` |
| **1** | `0 < 10` (**True**) | `test_list.append(0)`; `counter += 2` | `2` |
| **2** | `2 < 10` (**True**) | `test_list.append(2)`; `counter += 2` | `4` |
| **3** | `4 < 10` (**True**) | `test_list.append(4)`; `counter += 2` | `6` |
| **4** | `6 < 10` (**True**) | `test_list.append(6)`; `counter += 2` | `8` |
| **5** | `8 < 10` (**True**) | `test_list.append(8)`; `counter += 2` | `10` |
| **6** | `10 < 10` (**False**) | **Loop Terminates** | `10` |
| **After loop** | — | `test_list.append("end")` | `10` |


#### **Answer:**
```text
[start,0,2,4,6,8,end]
```

---

### **Q8: What is the output of the following code snippet?**

```python
counter = 0
test_list = ["start"]

while (counter < 10):
    counter += 2
    test_list.append(counter)

test_list.append("end")
print(test_list)
```

#### **Execution Trace:**

| Iteration | `while counter < 10` | Action Taken | New `counter` Value |
| :--- | :--- | :--- | :--- |
| **Start** | — | Variables initialized | `0` |
| **1** | `0 < 10` (**True**) | `counter += 2`; `test_list.append(2)` | `2` |
| **2** | `2 < 10` (**True**) | `counter += 2`; `test_list.append(4)` | `4` |
| **3** | `4 < 10` (**True**) | `counter += 2`; `test_list.append(6)` | `6` |
| **4** | `6 < 10` (**True**) | `counter += 2`; `test_list.append(8)` | `8` |
| **5** | `8 < 10` (**True**) | `counter += 2`; `test_list.append(10)` | `10` |
| **6** | `10 < 10` (**False**) | **Loop Terminates** | `10` |
| **After loop** | — | `test_list.append("end")` | `10` |

#### **Answer:**
```text
[start,2,4,6,8,10,end]
```

---

### **Q9: Identify all errors in the following code snippet:**

```python
array_index = 0
grades = [0, 0, 0, 0, 0]

while (array_index < 5):
    grades[array_index] = input(f"Enter grade number {array_index}:")

print(grades)
```

#### **Execution Trace:**

N/A

#### **Answer:**
```text
1st error: This code is missing a `array_index += 1` statement; the code is just going to run `grades[array_index] = input(f"Enter grade number {array_index}:")` indefinitely --> logic error
2nd error: The `input(f"Enter grade number {array_index}:")` is missing a `{array_index + 1}`; otherwise, it's just going to display the same number indefinitely --> logic error
3rd error: the `input()` function only takes in strings, you must cast `int` or `float` over it to record integer or decimal numbers like `int(input(...))`
```