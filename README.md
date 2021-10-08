- 👋 Hi, I’m @Qiao12-pixel
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
Qiao12-pixel/Qiao12-pixel is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
'''
Time:2021/10/8  18:46
Author:qiaolijie-201613336
File:demo02.py
'''

import re
'''
a='123--*'
b=re.findall('123',a)
print(b)

x='a123456b'
y=re.findall('[a-z][0-9][0-9][0-9][0-9][0-9][0-9][a-z]',x)
print(y)
x='abcaacaccabc'
rule='a[a,b,c]c'
y=re.findall(rule,x)
print(y)
'''
'''(1）findall()
找到re匹配的所有字符串，返回一个列表

（2）search()
扫描字符串，找到这个re匹配的位置（仅仅是第一个查到的）

（3）match()
决定re是否在字符串刚开始的位置（匹配行首）'''
'''
s = "010-123456789"
rule = "010-\d*"
rule_compile = re.compile(rule)  # 返回一个对象
print(rule_compile)
s_compile = rule_compile.findall(s)
print(s_compile)  # 打印compile()返回的对象是什么

s='abcabcacc'
l=re.sub('abc','***',s)#替换字符串
m=re.subn('abc','xxx',s)#替换字符串并返回替换个数
n=re.split('b',s)#分割字符串
print(l)
print(m)
print(n)
'''
