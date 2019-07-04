import numpy as np
import os
os.chdir('C:/Users/Adrian/Documents/Data Journalism/Datacamp Lesson \
         Datafiles')
test_1 = np.array([92, 94, 88, 91, 87])

austintemps = np.genfromtxt('austintempsolo.csv')
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

test_3_fixed = test_3 + 2
total_grade = test_1 + test_2 + test_3_fixed
final_grade = total_grade / 3
print(final_grade)
coin_toss_again = np.array([[1, 0, 0, 1, 0], [0, 0, 1, 1, 1]])
student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])
tanya_test_3 = student_scores[2, 0]
cody_test_scores = student_scores[:, -1]

print(tanya_test_3)
print(cody_test_scores)
porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

cold = porridge[porridge < 60]
print(cold)
hot = porridge[porridge > 80]
print(hot)
just_right = porridge[(porridge > 60) & (porridge < 80)]
print(just_right)
