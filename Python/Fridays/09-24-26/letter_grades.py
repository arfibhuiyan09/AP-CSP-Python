# Problem: Given a percentage grade, provide the corresponding letter grade

grade = int(input())

if grade >= 90:
    print("A")
elif 87 <= grade <= 89:
    print("B+")
elif 83 <= grade <= 86:
    print("B")
elif 80 <= grade <= 82:
    print("B-")
elif 77 <= grade <= 79:
    print("C+")
elif 73 <= grade <= 76:
    print("C")
elif 70 <= grade <= 72:
    print("C-")
elif 67 <= grade <= 69:
    print("D+")
elif 63 <= grade <= 66:
    print("D")
elif 60 <= grade <= 62:
    print("D-")
else:
    print("F")