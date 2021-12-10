import re
txt='''pandikunta@gmail.com,
pandikuntamaidhili@hcl.com,
maidhili.pandikunta@hcl.com
dhairya.sree@hcl.com'''
match=re.findall("\w+\.[a-z]+@[a-z]+\.[a-z]+",txt)
print(match)


