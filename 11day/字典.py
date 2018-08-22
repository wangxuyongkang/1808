d = {"name":"徐永康","sex":"男","mz":"汉","age":"18","address":"北京"}
d["edu"] = "博士"
print(d)
d["sex"] = "女"
print(d)
d.pop("name")
print(d)
print(d['sex'])
print(d.get('name'))
for i in d:#遍历键
	print(d[i])
for i in d.keys():
	print(d[i])
for i in d.values():#遍历值
	print(i)
#遍历键值对
for i in d.items():
	print(i)
	print(i[0])
	print(i[1])
