'''
录入学籍
修改学籍
删除学籍
查找学籍
'''
print("欢迎来到学籍管理系统".center(30,"*"))
box = []
while(True):
	print("1.录入")
	print("2.修改")
	print("3.查找")
	print("4.删除")
	print("5.退出")
	num = int(input("请选择功能"))
	if num == 1:
		xjb = {}
		name = input("请输入，名字:")
		if len(name)>=2 and len(name)<=4:
			print(name)
		age = int(input("请输入年龄:"))
		sex = input("请输入性别:")
		phone = input("请输入手机号")
		xjb["name"] = name
		xjb["age"] = age
		xjb['sex'] = sex
		xjb['phone'] = phone
		box.append(xjb)
		print(box)
		print("录入")
	elif num == 2:
		print("修改")
		name = input("请输入你的名字")
		for i in box:
			if i['name'] == name:
				print(i)
				print("1.修改名字")
				print("2.修改年龄")
				print("3.修改性别")
				print("4.修改手机号")
				num = int(input("请选择修改功能"))
				if num == 1:
					s_um = input("请输入你要改的名字")
					i['name'] = s_um
				elif num == 2:
					s_um = int (input("请输入你要改的年龄"))
					i['age'] = s_um
				elif num == 3:
					s_um = input("请输入你要改的性别")
					i['sex'] = s_um
				elif num == 4:
					s_um = input("请输入你的电话")
					i['phone'] = s_um
				print("修改成功")
						
	elif num == 3:
		for i in box:
			nr = input("请输入要查找的名字")
			if xjb['name'] == nr:
				print("姓名\t年龄\t性别\t手机号")
				print("%s\t%s\t%s\t%s\t"%(xjb['name'],xjb['age'],xjb['sex'],xjb['phone']))
			else:
				print("没有这个人")
		print("查找")
					
	elif num == 4:
		print("删除")
		name = input("请输入你要删除的学生姓名:")
		for xjb in box:
			if xjb["name"] == name:
				num = int(input("是否要删除 1:yes 2:No"))
				if num == 1:
					box.remove(xjb)
					print("删除成功")
				else:
					print("删除失败")
             	
	
	elif num == 5:
		print("退出")
		break













