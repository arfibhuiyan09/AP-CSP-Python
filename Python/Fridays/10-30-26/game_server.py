# Problem:

# A player can join a match if they have a premium account
# or enough game credits, provided the server is available.
# If the server is unavailable, the player cannot join.
# Otherwise, if the player has a premium account or enough credits,
# the player joins. Otherwise, the player is placed on hold.

# The only valid strings for status are
# "Join", "Denied", and "Hold"

premium_account = input("Premium account: ") == "True"
enough_credits = input("Enough credits: ") == "True"
server_available = input("Server available: ") == "True"

status = ""

if not server_available:
    status = "Denied"

elif premium_account or enough_credits:
    status = "Join"

else:
    status = "Hold"

print(status)