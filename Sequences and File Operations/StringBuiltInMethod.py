str = 'rakesh'
print(str.capitalize())
print(str.count("as", 0, len(str)))
s = str.encode('utf-8', 'strict')
print(s)

str1 = 'dinesh'
print(str1.replace('e', '--E--', 1))
print(str1.upper())
print(str1.index('n'))

str2 = "Python is easy"
print(str2[::-1])
print(str2[3:10])
print(str2.find('P'))
str3 = str1+str2
print(str3)
print(str*3)