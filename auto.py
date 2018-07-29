import os 
li_word = []
with open("name", 'r', encoding="utf-8") as f:
	for i in f:
		li_word.append(i.strip().split(" "))
print(li_word)
dic = dict(li_word)
print(dic)
