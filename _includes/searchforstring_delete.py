
with open(r'./home.html', 'r') as infile, \
     open(r'./done.html', 'w') as outfile:
    data = infile.read()
    data = data.replace('href="#"', "")
    outfile.write(data)

'''
f = open('./newer.html','r')
a = ['href="#"']
lst = []
time.sleep(2)
for line in f:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open('./new2.html','w')
for line in lst:
    f.write(line)
f.close()
'''


'''
#sets the phrase to whatever
phrase = str('href="#"')
# f is the open file
f = open("home.html","r")
#lines is the open file read
lines = f.readlines()
#close the file
f.close()
# now f is a new file
f = open("new.html","w")
# iterate over the lines - if phrase is not equal to line.strip
# then write that line
for line in lines:
    if phrase == True:
        f.strip(line)
for line in lines:
    if phrase != line.strip():
        f.write(line)
f.close()
'''
