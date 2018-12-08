import re
a = 'xxIxxosfuuxxlovexxsfffaxxpythonxxx'
infos = re.findall('xx(.*?)xx',a)
print(infos)