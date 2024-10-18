
while True: 
  nterms = int(input("Enter number of terms: "))

  result = list(map(lambda x : 2 ** x, range(nterms+1)))
  if nterms > 0:
     print(result)
  else: 
     break
  
while True: 
  num = int(input("Enter number of terms(new approach): "))
  if num > 0:
    for i in range(1,num+1):
      print(2**i)
  else:
    break
     
  

