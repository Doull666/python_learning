age = int(input("请输入年龄："))
if age >= 18 and age < 30:
	print('成年')
elif age >= 30 and age < 60:
	print('中年')
elif age >= 60:
	print('老年')
