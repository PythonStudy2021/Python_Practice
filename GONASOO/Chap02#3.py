###
### 주민등록번호 나누기
### 881120-1068234
### YYYYMMDD + num
###

pin = '881120-1068234'

# yyyymmdd = pin[0,1,2,3,4,5]
yyyymmdd = pin[:6]

# num = pin[7,8,9,10,11,12,13]
num = pin[7:]


print(yyyymmdd)
print(num)