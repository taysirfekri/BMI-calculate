def BMI():
	hight=input("how tall are you ?");
	weight=input("what is your weight?");
	bmi_value=int(weight)/(int(hight)/100)**2;
	print('your BMI is {} '.format(round(bmi_value,2)));
	if bmi_value<18.5:
		print('you must eat more')
	elif bmi_value>=18.5 and bmi_value<=24:
		print('good job bro ^_^')
	else:
		print("you need lose some weight ")
BMI()
