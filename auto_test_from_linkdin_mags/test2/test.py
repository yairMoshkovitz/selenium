
score = 0

try:
    if a(1)==1:
        score += 3
except:
    print("error 1")

try:
    if a(1.1)== 1:
        score += 2
except:
    print("error 2")

try:
    if a(1,2,3):
        score += 4
except:
    print("error 3")


print(f"user-score-is:{score}")

