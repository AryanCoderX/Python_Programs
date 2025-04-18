s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(len(s))
print(s) #20==20.0 so both are considered same
