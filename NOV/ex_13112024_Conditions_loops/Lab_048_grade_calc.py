# Write a program that calculates and displays the letter grade for a given
# numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# If, elif, else

score = int(input("Enter the score\n"))

if score >=90 and score <=100:
    print("A grade")
elif score >=80 and score <=89:
    print("B grade")
elif score >= 70 and score <= 79:
    print("C grade")
elif score >= 60 and score <= 69:
    print("D grade")
elif score>=100 and score <=1:
    print("you are superman")
else:
    print("F")


