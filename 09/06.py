f= open("python.txt")

content= f.read()

f.close()

if "python" in content:
    print("Python is present")
else:
    print("Python is not present")