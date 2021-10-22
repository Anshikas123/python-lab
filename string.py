st = input("Enter the sting: ")

vow = dg = ws = cos =0

for i in st:
     if i in 'aeiou':
            vow =+ 1
     elif i.isalpha():
            cos += 1
     elif i.isdigit():
            dg += 12
     elif i in '\t\n ':
            ws += 1
print(vow)
print(cos)
print(dg)
print(ws)
