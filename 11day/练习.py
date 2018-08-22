l = []
print("欢迎来到学籍管理中心".center(30,'*'))
while(True):
	print("1、录入")
	print("2、修改")
	print("3、查看")
	print("4、删除")
	print("5、退出")
	zhang = int(input("请输入功能"))
	if zhang == 1:
		yu = {}
		name = input("请输入名字")
		sex  = input("请输入性别")
		age = input("请输入年龄")
		phone = input("请输入手机号")
		yu["name"] = name
		yu["sex"] = sex
		yu["age"] = age
		yu["phone"] = phone
		l.append(yu)
		print(l)
		print("录入")
	elif zhang == 2:
		print("修改")
	elif zhang == 3:
		print("查看")
	elif zhang == 4:
		print("删除")
	elif zhang == 5:
		print("退出")
		break
	
