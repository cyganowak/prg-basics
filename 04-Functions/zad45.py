###
# Calculates the final grade for a test based
# on the number of points obtained
#
def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif points >= 14:
        grade = 'Good'
    elif points >= 10:
        grade = 'Satisfactory'
    elif points < 10:
        grade = 'Fail'
    return grade
input_points = int(input('Enter the number of points obtained on the test: '))
final_grade = pts_to_grade(input_points)
print(f'You scored {input_points} points on the test. Your final grade is {final_grade}')
