import re
reggex = 'row.txt'
with open(reggex,'r',encoding='utf-8')as file:
    text = file.read()

#1
t1 = re.match(r'ab*',text)
print (t1)

#2
text1="abbb"
t2=re.match(r'ab{2,3}', text1)
print(t2)

#3
t3=re.findall(r'[a-z]+_[a-z]', text)
print(t3)

#4
t4=re.findall(r'[A-Z]+[a-z]+', text)
print(t4)

#5
text2 = "astalavista ab"
t5=re.fullmatch(r'^a.*b$', text2)
print(t5)

#6
t6=re.sub(r'[ ,.]', ':', text)
print(t6)

#7
text3 = 'hello_my_dear_friend'
w=text3.split('_')
t7=w[0]+''.join(x.capitalize() for x in w[1:])
print(t7)

#8
text4 = 'ByeByeMan'
t8 = re.findall(r'[A-Z][^A-Z]*', text4)
print(t8)

#9
text5 = 'GitGelAlAtMat'
t9 = re.sub(r'(?<!^)(?=[A-Z])', ' ', text5)
print(t9)

#10
text6 = 'camelCaseIsCool'
t10 = re.sub(r'([a-z])([A-Z])', r'\1_\2', text6).lower()
print(t10) 