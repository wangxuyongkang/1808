lisa = []
for i in range(2):
	d = {}
	name = input("请输入名字")
	sex = input("请输入性别")
	age = input("请输入年龄")
	d["name"] = name
	d["sex"] = sex
	d["age"] = age
	lisa.append(d)
print(lisa)
for i in lisa:
	for j in i.valuse():
		print(j)
