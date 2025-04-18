name= input("Enter Your Name: ")
date= (input("Enter the date: "))

print(f'''
Dear <{name}>,
You are selected!
<{date}>
'''
)

# or

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("|Name|",name).replace("|Date|",date))
# replace fuction bs string ke liye use kr skte hai int use nahi kr skte hai