

score = 0 
try:
    if rep("abcd",["a"]) == " bcd" :
        score += 5
except:
    print('error 1')
try:
    if rep("abcd",["a","c"]) == " b d" :
        score += 4
except:
    print('error 2')

print(f"user-score-is:{score}")





