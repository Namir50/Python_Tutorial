try: 
  a = int(input("Enter a number: "))
  b = str(input("Enter a string: "))
  print(a+b)
except(ValueError,TypeError) as a:
  a = "Cannot run it"
  print(a)

