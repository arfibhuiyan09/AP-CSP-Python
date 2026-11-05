# A smart home unlocks the door if either
# a recognized face or a valid access code is detected,
# provided the alarm is not active. If the alarm
# is active and the face is not recognized,
# access is denied. Otherwise, the request on hold.

# The only valid strings for status are
# "Unlock", "Denied", "Hold", and "Pending"

face_recognized = input("Face recognized: ") == "True"
valid_code = input("Valid code: ") == "True"
alarm_active = input("Alarm active: ") == "True"

status = "Pending"


if (face_recognized or valid_code) and not alarm_active:
    status = "Unlock"

elif not face_recognized and alarm_active:
    status = "Denied"

else:
    status = "Hold"

print(status)