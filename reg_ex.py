import re

file = open("twitter_text.txt")

data = file.read()

#split data at a space
#split_data = re.split('\s+', data)
#split_data = regex.split(data)
#print(split_data)

#print every instance of cloud
#for data in split_data:
#    if(data == 'cloud' or data == 'clouds'):
#        print(data)

#find all twitter names
#foo = re.findall(r'@\w+', data)
#print(foo)

#find anything ending with clouds taste like
#foo = re.findall(r'.+clouds\staste\slike\.\s*.*', data)
foo = re.findall(r'clouds taste like', data)
print(foo)
