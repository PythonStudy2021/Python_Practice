# p47 문자열
multiline = """
Life is too short
You need python
"""
print(multiline)
# p49 문자열 연산하기
head = "Python"
tail = " is fun!"
print(head+tail)
a = "python"
print(a * 2)
# p50 문자열 길이구하기
print("=" * 50)
print("My Program")
print("=" * 50)
print(len(a))
# p51 문자열 인덱싱
print(a[3]+a[-1])
# p52 문자열 슬라이싱
print(multiline[0:5])
# p57 문자열 바꾸기
print(a[:1]+'i'+a[2:])
# p59 문자열 포매팅
number = 10
day = "three"
print("I ate %d%% apples. so I was sick for %s days." % (number, day))
# p60 문자열 포맷코드(정렬, 소수점)
print("%10s" % "hi")
print("%-10sjane" % "hi")
print("%10.4f" % 3.442134234)
# p63 포맷함수 사용 포매팅
print("I ate {0} apples. so I was sick for {1} days." .format(number, day))
print("{0:=^10}" .format("hi"))
# p65 f문자열 포매팅
print(f"나의 이름은 {number}입니다. 나이는 {day}입니다.")