import re
a = '''<div>指数
<div>'''

word = re.findall('<div>(.*?)<div>',a,re.S)
print(word[0].strip())