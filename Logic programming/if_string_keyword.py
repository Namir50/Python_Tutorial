import keyword
x = ["name","hello","while","for","world"]

for i in range(len(x)):
    if keyword.iskeyword(x[i]):
        print(x[i], "is a keyword")
    else:
        print(x[i], "is not a keyword")
    