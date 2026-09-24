# Problem: Given a protocol, provide the name of the corresponding layer.

protocol = input().upper().strip()

if protocol == "HTTP":
    print("Application")
elif protocol == "IP":
    print("Network")
elif protocol in ("TCP", "UDP"):
    print("Transport")
