temp_c= int(input("Enter temperature in celsius: "))

def convert(t):
    cal= t*1.8 +32
    return cal

print("Temperature in Fahrenheit is:",convert(temp_c))