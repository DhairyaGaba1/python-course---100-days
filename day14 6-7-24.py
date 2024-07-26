#Code for video 49
# Reading a file
# f=open("myfile.txt",'r')
# text=f.read()
# print(text)
# f.close()

#WRITING IN A FILE

# f=open('myfile.txt','a')
# f.write("Hello world")
# f.close()

# with open('myfile.txt','r') as f:
#     print(f.read())

#Code for video 50

# f=open("myfile.txt","r")
# while True:
#     line=f.readline()
#     if not line:
#         print("All the data has been printed")
#         break
#     print(line)

# f = open('marks1.txt', 'r')
# i = 0
# while True:
#   i = i + 1
#   line = f.readline()
#   if not line:
#     break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"Marks of student {i} in Maths is: {m1}")
#   print(f"Marks of student {i} in English is: {m2}")
#   print(f"Marks of student {i} in SST is: {m3}")
#   print()

# f=open("myfile2.txt","w")
# lines=['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()
'''
f = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()
'''

#Code for video 51

# with open('myfile.txt','r') as f:
#     f.seek(10)
#     print(f.read(6))
#     print(f.tell())

# with open('sample.txt', 'w') as f:
#   f.write('Hello World!')
#   f.truncate(5)

# with open('sample.txt', 'r') as f:
#   print(f.read())

#Code for video 52

# double = lambda x:x*2
# print(double(6))