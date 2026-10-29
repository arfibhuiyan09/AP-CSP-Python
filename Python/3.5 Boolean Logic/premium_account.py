"""
A player can join a match if they have a premeium account or enough game credits, provided the server is available.

If the server is unavailable, the player can not join

Otherwise, if the player has a premeium account or enough credits, the player joins

Otherwise, the player is placed on hold.
"""

p_acc = input("Premium account? (yes/no): ").strip().lower() == "yes"
credits = input("Enough credits? (yes/no): ").strip().lower() == "yes"
server_avail = input("Server available? (yes/no): ").strip().lower() == "yes"

status = "Hold"

if not server_avail:
    status = "Access Denied..."

elif p_acc or credits:
    status = "Access Granted!"

print(status)