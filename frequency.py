st = input("Enter the sting")
res = ''
for i in st:
         if i not in res:
                 print(i,st.count(i))
                 res+=i
                 
