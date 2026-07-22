li=["apple", "banana", "grape", "blueberry", "orange"]
total=0
ch=input()
for s in li:
    if s[2]==ch or s[3]==ch:
        print(s)
        total+=1
print(total)