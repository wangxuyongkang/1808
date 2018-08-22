

















import time
print("欢迎来到麒麟网咖".center(30,"$"))
lis = []
while True:
	print("1.上机")
	print("2.下机")
	print("3.管理员登录")
	num =int(input("请选择功能"))
	if num == 1:
		d = {}
		card = int(input("请输入身份证:"))
		money = float(input("请输入金额"))
		d['card'] = card
		d['money'] = money
		lis.append(d)
		print(lis)
		print("上机")
	elif num == 2:
		card = int(input("请输入身份证号"))
		for i in lis:
			if i ['card'] == card:
				endtime == int(time.time())
				diff_money = (endtime-i['time'])*10
				diff = i['money'] - diff_money
				if diff < 0:
					moeny
				print("上网花了%.02f元,还剩%.02f"%(diff_money,diff))
			else:
				print("输入的身份证不一样!")
		print("下机")
		break
	elif num == 3:
		account = input("请输入管理员账号")
		pwd = inpu("请输入管理员密码")
		if account == "admin" and pwd == "admin":
			print("欢迎老板进入系统")
			
