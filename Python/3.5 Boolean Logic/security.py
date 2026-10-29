"""
A smart home unlocks the door if either a recognized face or a valid code is detected (provided the alarm is not active)

If the alarm is active, and the face is not recognized, access is denied

Otherwise the request is on hold
"""

face_recognized = input("Face recognized (yes/no): ").strip().lower() == "yes"
valid_code = input("Valid Code (yes/no): ").strip().lower() == "yes"
alarm_active = input("Alarm Active (yes/no): ").strip().lower() == "yes"

status = ""

if (face_recognized or valid_code) and not alarm_active:
    status = "Access Granted!"

elif not face_recognized and alarm_active:
    status = "Access Denied..."

else:
    status = "Hold"

print(status)