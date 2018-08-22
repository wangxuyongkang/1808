import time
print("欢迎来到如家宾馆".center(30,'*'))
l = []
all_money = 0
while True:
	print("1.入住")
	print("2.离店")
	print("3.统计")
	print("4.退出")
	num = int(input("请学选择"))
	if num == 1:
		print("入住")
		box = {}
		sfz = input("请输入你的身份证:")
		name = input("你的姓名:")
		box['sfz'] = sfz
		box['name'] = name
		box['time'] = int(time.time())
		box['sj'] = True#开房时间
		if len(sfz) == 18:
			l.append(box)
			print("登记成功%s"%l)
		else:
			print("身份证错误请重新输入")
			continue
	elif num == 2:
		for i in l:
			name = input("请输入你的名字")
			if box['name'] == name:
				box['sj'] = False
				endtime = int(time.time())
				zdq = (endtime-box['time'])*10
				print("房费为%.02f"%zdq)
				money = float(input("请付钱(注:不找零):"))
				all_money += zdq
				print("离店成功")
			else:
				print("没有这个人请重试!")
				continue
	elif num == 3:
		account = input("请输入管理员账户:")
		pwd = input("请输入密码:")
		if account == 'xuyongkang' and pwd == 'xuyongkang':
			print("欢迎老板")
			cmd = input("请输入统计")
			count = 0
			if cmd == '统计':
				print("今日营业额日为%0.2f"%all_money)
				for i in l:
					if box['sj'] == False:
						count +=1
				print("今天退房%d"%count)
		print("今天住房%d"%len(l))
	elif num == 4:
		print("退出")
		break
