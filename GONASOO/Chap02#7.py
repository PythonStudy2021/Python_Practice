###
### list를 문자열(str)로 변환
###

import numpy as np

a = ['Life','is','too','short']
print(a)

# create an empty string
# add each element of list
result = ''
for k in range (len(a)):
    result += a[k] + ' '

print(result)