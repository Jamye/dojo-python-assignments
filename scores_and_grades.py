import random

"""
Write a function that generates ten scores between 60 and 100.
Each time a score is generated, your function should display what the
grade is for a particular score.

Output:
Scores and Grades
Score: 87; Your grade is B
Score: 67; Your grade is D
Score: 95; Your grade is A
Score: 100; Your grade is A
Score: 75; Your grade is C
Score: 90; Your grade is A
Score: 89; Your grade is B
Score: 72; Your grade is C
Score: 60; Your grade is D
Score: 98; Your grade is A
End of the program. Bye!

Thoughts:
- Iterate 10 times
- May need Math.floor()
- Going to use random.randint(a, b)
- Concatenate strings and create conditionals for the grades to ensure
  the right letters with the right numbers, that it is between 60, 100
"""
def scores_and_grades():
    print "Scores and Grades"
    for i in range(10):
        score = random.randint(60, 100)
        if score <= 69:
            grade = "D"
        elif 70 <= score <= 79:
            grade = "C"
        elif 80 <= score <= 89:
            grade = "B"
        else:
            grade = "A"
        print "Score: " + str(score) + "; Your grade is " + grade
    print "End of the program. Bye!"

scores_and_grades()
