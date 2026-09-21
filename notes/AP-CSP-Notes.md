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

##### the layers of internet protocols are decending

`application` - HTTP → sends the **message** from point A to point B

`transport` - TCP, UDP → adds a *TCP header* to **direct** the message to the correct application

`network` - IP → adds a *IP header* to direct the message **towards point B** → this is now called a ***packet***

`link` - WiFi, Ethernet → adds a MAC header to **contain the hardware addresses of the immediate local devices**

`physical` - bits "on the wire" → **message sent to point B**

##### if you specialise in a specific layer eg. network, you can only focus on the network layer and not above nor below.

___

### Transport Protocols

`TCP` - **Transmission Control Protocol** → reliable, congestion control, flow control, is a **lossless** transfer of data

`UDP` - **User Datagram Protocol** → unreliable, unordered delivery, is a **lossy** transfer of data