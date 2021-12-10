import re
txt="if you got a chance to win,you will definetly prove yourself"
match=re.compile('\w\w')
patten=match.finditer(txt)
for i in patten:
  print(i)