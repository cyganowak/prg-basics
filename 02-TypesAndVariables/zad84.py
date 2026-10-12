###
# A program that prints your height both in cm and in feet and inches.
#
cm = int(input('Enter your height in cm: '))
feet = cm // 30.48
inches = (cm % 30.48) // 2.54
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {int(feet)} feet and {int(inches)} inches')
