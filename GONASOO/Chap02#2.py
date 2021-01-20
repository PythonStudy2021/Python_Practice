###
### 자연수의 홀수/짝수 판별
###

n = int(input())

# int 0 : false
# int except 0 : true
if n%2: print(n, ' : 홀수')
else: print(n, ' : 짝수')