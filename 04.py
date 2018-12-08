import re
phone = '132-4355-4343'
new_phone = re.sub('\D','',phone)
print(new_phone)