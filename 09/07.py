f= open("python.txt")

lines= f.readlines()

f.close()

lineno=1
for line in lines:
    if ("python" in line):
        print("Python is present on line no",lineno)
        break
    lineno+=1
else:
    print("Python is not present")

