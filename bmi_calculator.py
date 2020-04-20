# 過輕 < 18.5
# 正常 18.5 <= BMI < 24
# 過重 24 <= BMI < 27
# 輕度肥胖 27 <= BMI < 30
# 中度肥胖 30 <= BMI < 35
# 重度肥胖 BMI >= 35
# BMI值計算公式:    BMI = 體重(公斤) / 身高2(公尺2)
# http://depart.femh.org.tw/dietary/3OPD/BMI.htm

weight = float(input('您的體重(公斤)：'))
height = float(input('您的體重(公分)：'))

bmi = weight / ((height/100)**2)

if bmi < 18.5:
	print('體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('體重正常')
elif bmi >= 24 and bmi < 27:
	print('體重過重')
elif bmi >= 27 and bmi < 30:
	print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('中度肥胖')
else:
	print('重度肥胖')
