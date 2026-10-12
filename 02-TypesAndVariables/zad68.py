first = input("Enter the first letter: ")
last = input("Enter the last letter: ")
firstcode = ord(first)
lastcode = ord(last)
distance = lastcode - firstcode -1
print("The distance between the letters", first, "and", last, "is:", distance)