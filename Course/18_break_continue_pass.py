#break: breaks the flow of program once the condition is hit
#continue: it skips that particular iteration
#pass: to avoid syntax error


#pass
for i in range(1,10):
    pass


#continue
for i in range(1,10):
    if i==5:
        continue
    print(i)

#break
for i in range(1,10):
    if i==5:
        break
    print(i)