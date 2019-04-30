print ("Estimate the letter grade from five scores")

score_total = 0

for i in range(5):
    user_input = int(input("Enter score from 0 to 20: "))
    score_total = score_total + user_input

if score_total >= 85:
    grade = 'A'
elif score_total >= 75:
    grade = 'B'
elif score_total >= 65:
    grade = 'C'
elif score_total >= 50:
    grade = 'D'
else:
    grade = 'F'

print ("The estimated letter grade is: ", grade)
