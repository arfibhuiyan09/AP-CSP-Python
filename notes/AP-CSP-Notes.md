` to save codebase open source control (ctrl + shift + g) and press commit (ctrl + enter) `


## Selection

##### 2.6
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

* an IPv4 IP Address that is 76.50.100.235 is `1001100.110010.1100100.11101011` in binary. ***notice each (group) has 8 bits***

`IPv6` - a **128bit** identifier, associated with each host or router interface

* it is written as eight groups of four hexadecimal digits (characters 0–9 and a–f) separated by colons.

    - IPv6 is exactly `2^96` times larger than IPv4 since `2^128/2^32 = 2^(128-32) = 2^96`

