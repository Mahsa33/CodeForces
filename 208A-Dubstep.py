import re
inp = input('')


s = re.sub('WUB',' ',inp)
s = s.replace("  "," ")
s = s.strip()
print(s)