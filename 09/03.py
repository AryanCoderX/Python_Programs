f= open("table.txt", "w")

def table():    
    for i in range(1,21):
        for j in range(1,11):
            f.write(f"{i} * {j} = {i*j}\n")

        f.write("\n")

table()
f.close()