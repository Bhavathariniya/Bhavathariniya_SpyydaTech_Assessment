word =  input("Enter a word: ").lower()

txt = ""
for i in word:
    if i.isalpha() or i.isspace():
        txt += i
    else:
        txt += " "

list = txt.split()
frequency = {}

for i in list:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

for key, value in frequency.items():
    print(f"{key}: {value}")
        

