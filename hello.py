# print("hello")  >  hello

# 숫자열 자료형 int(정수), float(실수)

# a = 1.24
# print(type(a))  >  <class 'float'>

# 사칙연산 *(곱하기), /(나누기), //(몫), %(나머지), **(제곱)

# a = 3
# b = 4
# print(a * b)  >  12

# 문자열 자료형 str \n(줄 바꿀 때), \t(탭 간격), \\(문자\ 표현), \'('출력)

# a = 'python's favorite food is perl' (SyntaxError)
# a = 'python\'s favorite food is perl'
# print(a)  >  python's favorite food is perl

# a = "python's favorite food is perl"
# print(a)  >  python's favorite food is perl

# a = 'Life is too short\nYou need python'
# print(a)  >  Life is too short
#              You need python

# a = "python"
# b = " is fun!"
# print(a + b)  >  python is fun!
# print(a * 100)  >  pythonpythonpythonpythonpython...

# 인덱싱(Indexing) a[] 파이썬은 0부터 숫자를 센다.

# a = "Life is too short, You need python"
# print(a[0])  >  L

# 슬라이싱(Slicing) a[이상:미만:간격]

# a = "Life is too short, You need python"
# print(a[:8])  >  Life is 

# 문자열 포매팅 %s(문자열(만능)), %d(정수), %f(실수)

# a = "I eat " + str(3) + " apples."
# b = "I eat %d apples" % 3
# print(b)  >  I eat 3 apples

# number = 10
# day = 3
# a = "I ate %d apples, so I was sick for %s days." % (number, day)
# print(a)  >  I ate 10 apples, so I was sick for 3 days

# a = "나의 이름은 {name}입니다. 나이는 {age}살 입니다.".format(name = "서수홍", age = 26)
# print(a)  >  나의 이름은 서수홍입니다. 나이는 26살 입니다.

# name = "서수홍"
# age = 26
# a = f"나의 이름은 {name}입니다. 나이는 {age}살 입니다."
# print(a)  >  나의 이름은 서수홍입니다. 나이는 26살 입니다.

# 소수점 표현 (%간격.소수점 남기는 자리 수f)

# a = "%0.4f" % 3.42134234
# print(a)  >  3.4213

# 문자열 개수 세기(count)

# a = "hobby"
# print(a.count('b'))  >  2

# 위치 알려주기(find)

# a = "hobby"
# print(a.find('b'))  >  2
# print(a.find('x'))  >  -1

# 위치 알려주기2(index)

# a = "Life is too short"
# print(a.index('t'))  >  8

# 문자열 삽입(join)

# a = ",".join("abcd")
# print(a)  >  a,b,c,d

# 소문자를 대문자로 바꾸기(upper)

# a = "hi"
# print(a.upper())  >  HI

# 대문자를 소문자로 바꾸기(lower)

# a = "HI"
# print(a.lower())  >  hi

# 양쪽 공백 지우기(strip)

# a = "    hi     "
# print(a.strip())  >  hi

# 문자열 바꾸기(replace)

# a = "Life is too short"
# print(a.replace("Life", "Your leg"))  >  Your leg is too short

# 문자열 나누기(split)

# a = "Life is too short"
# print(a.split())  >  ['Life', 'is', 'too', 'short']
# a = "a:b:c:d"
# print(a.split(":"))  >  ['a', 'b', 'c', 'd']

# 리스트 자료형[]

# a = ["서수홍", "황수정", "홍길동", "포미"]
# print(a[1])  >  황수정
# a = ["서수홍", "황수정",["홍길동", "포미"]]
# print(a[2][1])  >  포미

# 리스트의 인덱싱

# a = [1, 2, 3]
# print(a[0] + a[2])  >  4

# 리스트의 슬라이싱

# a = [1, 2, 3, 4, 5]
# print(a[0:3])  >  [1, 2, 3]

# 리스트 더하기

# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)  >  [1, 2, 3, 4, 5, 6]

# 리스트 반복하기

# a = [1, 2, 3]
# print(a * 3)  >  [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트 바꾸기

# a = ["서수홍", "황수정", "홍길동"]
# a[2] = "포미"
# print(a)  >    >  ['서수홍', '황수정', '포미']
# a = ["서수홍", "황수정", "홍길동"]
# a[:2] = ["Seo Su Hong", "Hwang Su Jeong"]
# print(a)  >  ['Seo Su Hong', 'Hwang Su Jeong', '홍길동']
# a = ["서수홍", "황수정", "홍길동"]
# del a[0]
# print(a)  >  ['황수정', '홍길동']

# 리스트에 요소 추가(append)

# a = ["서수홍", "황수정", "홍길동"]
# a.append("포미")
# print(a)  >  ['서수홍', '황수정', '홍길동', '포미']

# 리스트 정렬(sort(문자는 가나다순 숫자는 크기순))

# a = [1, 5, 3]
# a.sort()
# print(a)  >  [1, 3, 5]

# 리스트 뒤집기(reverse)

# a = [1, 5, 3]
# a.reverse()
# print(a)  >  [3, 5, 1]

# 위치 반환(index)

# a = [1, 2, 3]
# print(a.index(2))  >  1

# 리스트에 요소 삽입(insert)

# a = [1 ,2, 4, 5]
# a.insert(2, 3)
# print(a)  >  [1, 2, 3, 4, 5]

# 리스트 요소 제거(remove)

# a = [10, 20, 30, 40, 40, 50]
# a.remove(40)
# print(a)  >  [10, 20, 30, 40, 50]

# 리스트 요소 끄집어내기(pop)

# a = [1, 2, 3, 4, 5, "서수홍"]
# a.pop()
# print(a)  >  [1, 2, 3, 4, 5]

# 리스트에 포함된 요소 X의 개수 세기(count)

# a = [1, 2, 1, 3, 1]
# print(a.count(1))  >  3

# 리스트 확장(extend)

# a = ["서수홍", "황수정", "포미"]
# a.extend(["홍길동", "갑돌이"])
# print(a)  >  ['서수홍', '황수정', '포미', '홍길동', '갑돌이']

# 튜플()

# 튜플 요소값 변경 시 오류

# t1 = (1, 2, 'a', 'b')
# del t1[0]
# TypeError: 'tuple' object doesn't support item deletion
# t1 = (1, 2, 'a', 'b')
# t1[0] = 'c'
# TypeError: 'tuple' object does not support item assignment

# 튜플 인덱싱, 슬라이싱

# t1 = (1, 2, 'a', 'b')
# print(t1[0])  >  1
# print(t1[0:2])  >  (1, 2)

# 튜플 더하기, 곱하기

# t1 = (1, 2, 'a', 'b')
# t2 = (3, 4)
# print(t1 + t2)  >  (1, 2, 'a', 'b', 3, 4)
# print(t1 * 3)  >  (1, 2, 1, 2, 1, 2)

# 딕셔너리(dictionary)

# dic = {'name' : 'SuHong', 'age' : 26}
# print(dic['name'])  >  SuHong

# 딕셔너리 쌍 추가하기

# a = {'name' : "서수홍"}
# a['age'] = 26
# print(a)  >  {'name': '서수홍', 'age': 26}

# 딕셔너리 요소 삭제하기

# a = {'name' : "서수홍"}
# a['age'] = 26
# del a['name']
# print(a)  >  {'age': 26}

# 딕셔너리 키 중복

# a = {1 : 'a', 1 : 'b'}
# print(a)  >  {1: 'b'}
# 키 중복X, 벨류 중복O(키가 핵심)

# Key, Value 리스트 만들기

# a = {1 : "서수홍", 2 : "황수정", 3 : "포미"}
# print(a.keys())  >  dict_keys([1, 2, 3])
# print(a.values())  >  dict_values(['서수홍', '황수정', '포미'])
# print(a.items())  >  dict_items([(1, '서수홍'), (2, '황수정'), (3, '포미')])

# 모두 지우기

# a = {1 : "서수홍", 2 : "황수정", 3 : "포미"}
# a.clear()
# print(a)  >  {}

# Key값으로 Value얻기

# a = {1 : "서수홍", 2 : "황수정", 3 : "포미"}
# print(a[1])  >  서수홍
# print(a[4])  >  KeyError: 4
# print(a.get(4, '없음'))  >  없음

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)

# a = {1 : "서수홍", 2 : "황수정", 3 : "포미"}
# print(1 in a)  >  True
# print(4 in a)  >  False

# 집합(set), (중복된 요소를 가질 수 없다.)

# s1 = set([1, 2, 3])
# s1 = {1, 2, 3}
# print(s1)  >  {1, 2, 3}
# ex)
# l = [1, 2, 2, 3, 3, 3, 4]
# newList = list(set(l))
# print(newList)  >  [1, 2, 3, 4]

# 교집합(&, intersection)

# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])
# print(s1 & s2)  >  {4, 5, 6}
# print(s1.intersection(s2))  >  {4, 5, 6}

# 합집합(|, union)

# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])
# print(s1 | s2)  >  {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(s1.union(s2))  >  {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 차집합(-, difference)

# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])
# print(s1 - s2)  >  {1, 2, 3}
# print(s1.difference(s2))  >  {1, 2, 3}

# 값 1개 추가하기(add)

# s1 = set([1, 2, 3])
# s1.add(4)
# print(s1)  >  {1, 2, 3, 4}

# 값 여러개 추가하기(update)

# s1 = set([1, 2, 3])
# s1.update([4, 5, 6])
# print(s1)  >  {1, 2, 3, 4, 5, 6}

# 특정 값 지우기(remove)

# s1 = set([1, 2, 3, 4, '서수홍'])
# s1.remove('서수홍')
# print(s1)  >  {1, 2, 3, 4}

# 불(True, False)

# a = True
# print(type(a))  >  <class 'bool'>

# a = [1, 2, 3, 4]
# while a:
#    a.pop()
#    print(a)  >  [1, 2, 3]
#                 [1, 2]
#                 [1]
#                 []

# 변수

# a = [1, 2, 3]
# b = a
# a[1] = 4
# print(id(a))  >  14436
# print(id(b))  >  14436
# print(a is b)  >  True

# a = [1, 2, 3]
# b = a[:]
# a[1] = 4
# print(a)  >  [1, 4, 3]
# print(b)  >  [1, 2, 3]

# a, b = ('python', 'life') # a = b = 'hello'
# print(a)  >  python
# print(b)  >  life

# a = 3
# b = 5
# a, b = b, a
# print(a)  >  5
# print(b)  >  3

# 조건문(if문)

# money = True
# if money:
#    print("택시를 타고 가라.")
# else:
#    print("걸어가라.")
#  >  택시를 타고 가라.

# 비교연산자(>, <, >=, <=, !=)

# a = 1
# b = 2
# if a > b:
#    print("a가 b보다 더 크다.")
# else:
#    print("b가 a보다 더 크다.")
#  >  b가 a보다 더 크다.

# and(%), or(|), not

# money = 2000
# card = 1
# if money >= 3000 or card:
#    print('참이다.')
# else:
#    print('거짓이다.')
#  >  참이다.

# x in s, x not in s

# if 1 not in [1, 2, 3]:
#    print("참이다.")
# else:
#    print("거짓이다.")
#  >  거짓이다.


# 다중 조건 판단 (elif)

# pocket = ['paper', 'cellphone']
# card = 0
# car = 1
# if 'money' in pocket:
#    print('버스를 타고 가라.')
# elif card:
#    print('택시를 타고 가라.')
# elif car:
#    print('차를 타고 가라.')
# else:
#    print('걸어가라.')
#  >  차를 타고 가라.

# 조건부 표현식

# money = 4000
# message = "택시를 타고 가라." if money >= 3000 else "걸어가라."
# print(message)  >  택시를 타고 가라.

# 반복문(while문)

# treeHit = 0
# while treeHit < 10:
#    treeHit = treeHit +1
#    print("나무를 %d번 찍었습니다." %treeHit)
#    if treeHit == 10:
#        print("나무가 쓰러졌습니다.")
#  >  나무를 1번 찍었습니다.
#     나무를 2번 찍었습니다.
#     나무를 3번 찍었습니다.
#     .
#     .
#     나무를 10번 찍었습니다.
#     나무가 쓰러졌습니다.

# break

# coffee = 10
# money = 300
# while money:
#    print("돈을 받았습니다. 커피를 줍니다.")
#    coffee = coffee -1
#    print("남은 커피의 양은 %d개 입니다." % coffee)
#    if not coffee:
#        print("커피가 매진되었습니다. 판매를 중단합니다.")
#        break
#  >  돈을 받았습니다. 커피를 줍니다.
#     남은 커피의 양은 9개 입니다.
#     돈을 받았습니다. 커피를 줍니다.
#     남은 커피의 양은 8개 입니다.
#     .
#     .
#     돈을 받았습니다. 커피를 줍니다.
#     남은 커피의 양은 0개 입니다.
#     커피가 매진되었습니다. 판매를 중단합니다.

# continue

# a = 0
# while a < 10:
#    a = a + 1
#    if a % 2 == 0:
#        continue
#    print(a)
#  >  1
#     3
#     5
#     7
#     9

# 무한루프(ctrl + c로 빠져나가기)

# while True:
#    print('안녕하세요')
#  >  안녕하세요
#     안녕하세요
#     .
#     .

# for문

# test_List = ['one', 'two', 'three']
# for i in test_List:
#    print(i)
#  >  one
#     two
#     three

# a = [(1, 2), (3, 4), (5, 6)]
# for (first, last) in a:
#    print(first + last)
#  >  3
#     7
#     11

# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#    number = number + 1
#    if mark >= 60:
#        print("%d번 학생은 합격입니다." % number)
#    else:
#        print("%d번 학생은 불합격입니다." % number)
#  >  1번 학생은 합격입니다.
#     3번 학생은 합격입니다.
#     5번 학생은 합격입니다.

# continue

# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#    number = number + 1
#    if mark < 60: continue
#    print('축하합니다. %d번 학생은 합격입니다.' % number)
#  >  축하합니다. 1번 학생은 합격입니다.
#     축하합니다. 3번 학생은 합격입니다.
#     축하합니다. 5번 학생은 합격입니다.

# range

# sum = 0
# for i in range(1, 11):
#    sum = sum + i
# print(sum)  >  55

# 이중for문(구구단)

# for i in range(2, 10):
#    for j in range(1, 10):
#        print(i * j, end=" ")
#    print('')
#  >  2 4 6 8 10 12 14 16 18 
#     3 6 9 12 15 18 21 24 27 
#     4 8 12 16 20 24 28 32 36
#     5 10 15 20 25 30 35 40 45
#     6 12 18 24 30 36 42 48 54
#     7 14 21 28 35 42 49 56 63
#     8 16 24 32 40 48 56 64 72
#     9 18 27 36 45 54 63 72 81

# 리스트 내포

# result = []
# a = range(1, 11)
# for num in a:
#    if num % 2 == 0:
#        result.append(num*3)

# a = range(1, 11)
# result = [num * 3 for num in a if num % 2 == 0]
# print(result)  >  [6, 12, 18, 24, 30]

# result = []
# for x in range(2, 10):
#    for y in range(1, 10):
#        result.append(x * y)

# result = [x * y for x in range(2, 10) for y in range(1, 10)]
# print(result)  >  [2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]

# 함수

# def sum(a, b):
#    result = a + b
#    return result
# print(sum(1, 2))  >  3

# 입력값이 없는 함수

# def say():
#    return 'Hi'
# print(say())  >  Hi

# 결과값이 없는 함수

# def sum(a, b):
#    print("%d, %d의 합은 %d입니다." % (a, b, a + b))
# sum(1, 2)  >  1, 2의 합은 3입니다.

# 입출력 둘 다 없는 함수

# def say():
#    print('Hi')
# print(say())  >  Hi

# 여러개의 입력값(*)

# def sum_many(*args):
#    sum = 0
#    for i in args:
#        sum = sum + i
#    return sum
# print(sum_many(1, 2, 3))  >  6

# 키워드 파라미터(**)

# def print_kwargs(**kwargs):
#    for k in kwargs.keys():
#        if (k == "name"):
#            print("당신의 이름은 : " + kwargs[k])
# print(print_kwargs(name = "서수홍", b = 2))

# 함수의 결과값은 언제나 하나이다.

# def sum_and_mul(a, b):
#    return a + b, a * b, a - b
# print(sum_and_mul(1, 2))  >  (3, 2, -1)

# 매개 변수에 초깃값 미리 설정하기

# def say_myself(name, age, man):
#    print("나의 이름은 %s입니다." %name)
#    print("나이는 %d살입니다." %age)
#    if man:
#         print('남자입니다.')
#    else:
#         print("여자입니다.")
# say_myself('서수홍', 26, True)

# 함수 안에서 선언된 변수의 효력 범위

# a = 1
# def vartest(a):
#    a = a + 1
# vartest(a)
# print(a)  >  1

# 함수 안에서 함수 밖의 변수를 변경하는 방법 1

# a = 1
# def vartest(a):
#    a = a + 1
#    return a
# a = vartest(a)
# print(a)  >  2

# 함수 안에서 함수 밖의 변수를 변경하는 방법 2

# a = 1
# def vartest():
#    global a
#    a = a + 1
# vartest()
# print(a)  >  2

# immutable(정수, 실수, 문자열, 튜플)

# a = 1
# def vartest(a):
#     a = a + 1
# vartest(a)
# print(a)  >  1

# mutable(리스트, 딕셔너리, 집합)

# b = [1, 2, 3]
# def vartest2(b):
#     b = b.append(4)
# vartest2(b)
# print(b)  >  [1, 2, 3, 4]

# lambda

# def add(a, b):
#     return a+b

# add = lambda a, b: a + b
# print(add(1, 2))  >  3

# myList = [lambda a, b: a + b, lambda a, b: a * b]
# print(myList[1](1, 2))  >  2

# 사용자 입력과 출력

# input의 사용

# number = input("숫자를 입력하세요 : ")
# print(number)

# print문(, = 띄어쓰기, end="" = 값 중간에 입력될 문자)

# print("life", "is", "too short")  >  life is too short

# for i in range(10):
#     print(i, end=" hi ")  >  0 hi 1 hi 2 hi..9 hi

# 파일 읽고 쓰기

# 쓰기모드(w)

# f = open("c:/python/새 파일.txt", 'w', encoding="UTF-8")
# for i in range(1, 11):
#    data = "%d번째 줄입니다.\n" % i
#    f.write(data)
# f.close()

# 읽기모드(r)
# f = open("c:/python/새 파일.txt", 'r', encoding='UTF-8')
# line = f.readline()
# print(line)
# f.close()

# f = open("c:/python/새 파일.txt", 'r', encoding='UTF-8')
# while True:
#    line = f.readline()
#    if not line: break
#    print(line)
# f.close()

# readlines()함수 이용하기

# f = open("c:/python/새 파일.txt", 'r', encoding='UTF-8')
# lines = f.readlines()
# for line in lines:
#    print(line.strip("\n"), end=" ")
# f.close()

# read()함수 이용하기

# f = open("c:/python/새 파일.txt", 'r', encoding='UTF-8')
# data = f.read()
# print(data)
# f.close()

# 추가모드(a)

# f = open("c:/python/새 파일.txt", 'a', encoding='UTF-8')
# for i in range(11, 21):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# with문과 함께 사용하기

# with open("foo.txt", 'w')as f:
#    f.write("Life is too short, You need python")

# 클래스(설계도)

# class FourCal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
# a = FourCal(4, 2)
# a.setdata(4, 2)
# print(a.add())

# 클래스의 상속

# class FourCal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result

# 클래스의 상속2 - 메서드 추가

# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result

# 클래스의 상속3 - 메서드 오버라이딩(자식 > 부모)

# class SafeFourCal(FourCal):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first / self.second

# a = MoreFourCal(4, 2)
# b = SafeFourCal(4, 0)
# print(a.add())
# print(a.pow())
# print(b.div())

# 클래스 변수

# class Family:
#     lastname = "김"

# Family.lastname = "박"
# print(Family.lastname)
# a = Family()
# b = Family()
# print(a.lastname)
# print(b.lastname)

# 모듈(미리 만들어 놓은 .py 파일(함수, 변수, 클래스))

# import mod1
# print(mod1.add(1, 3))

# from mod1 import div
# print(div(4, 2))

# 다른 경로 모듈 가져오기(sys.path.append)

# import sys
# sys.path.append("c:/파이썬기초/subfolder")
# import mod2
# print(mod2.add(1, 2))

# 패키지(라이브러리) (가상의 game패키지 예)

# import game.sound.echo
# game.sound.echo.echo_test()

# from game.sound import echo
# echo.echo_test()

# from game.sound.echo import echo_test
# echo_test()

# from game.sound.echo import echo_test as e
# e()

# __all__

# from game.sound import *
# echo.echo_test()

# relative 패키지(다른 경로에 있는 모듈 불러오기)

# graphic/render.py에서 sound/echo.py모듈 불러오기

# from ..sound.echo import echo_test
# def render_test():
#     print("render")
#     echo_test()

# 예외처리(오류 최상위 부모 : Exception)

# try, except문

# try:
#     4 / 0
# except ZeroDivisionError as e:
#     print(e)

# try .. else

# try:
#     f = open('none', 'r')
# except FileNotFoundError as e:
#     print(str(e))
# else:
#     data = f.read()
#     print(data)
#     f.close()

# try .. finally

# f = open('foo.txt', 'w')
# try:
#     data = f.read()
#     print(data)
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# 여러 개의 오류 처리하기

# try:
#     a = [1, 2]
#     print(a[2])
#     4 / 0
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱싱할 수 없습니다.")

# 오류 회피하기

# try:
#     f = open('없는 파일', 'r')
# except FileNotFoundError:
#     pass

# 오류 일부러 발생시키기

# class Bird:
#     def fly(self):
#         raise NotImplementedError
# class Eagle(Bird):
#     def fly(self):
#         print("very fast")
# eagle = Eagle()
# eagle.fly()

# 내장함수(파이썬에서 기본적으로 포함하고 있는 함수(print(), type()))

# abs(절대값)
# print(abs(-3))

# all(모두 참인지 검사)
# print(all([1, 2, 3]))
# print(all([1, 2, 3, 0]))

# any(하나라도 참이 있는가?)
# chr(ASCII 코드를 입력받아 문자 출력)
# * ASCII(아스키 코드) = 0 ~ 127 사이의 숫자를 각 문자에 대응
# dir(자체적으로 가지고 있는 변수나 함수를 보여줌)
# divmod(몫과 나머지를 튜플 형태로 돌려줌)
# eval(실행 후 결과값을 돌려줌)
# id(주소 값)
# input(사용자 입력 받는 함수)
# int(10진수 정수 형태로 변환)
# len(길이)
# list(리스트로 변환)
# max(최대 값)
# min(최소 값)
# open(파일 열기)
# pow(제곱한 결과값 반환)
# range(범위)
# round(반올림)
# sorted(정렬)
# str(문자열 반환)
# tuple(튜플 반환)
# type(타입을 출력)
# zip(자료형을 묶어주는 열할)

# enumerate(열거하다)

# for i, name in enumerate(['body', 'foo', 'bar']):
#     print(i, name)

# filter(함수를 통과하여 참인 것만 돌려줌)

# def positive(x):
#     return x > 0
# a = list(filter(positive, [1, -3, 2, 0, -5, 6]))
# print(a)

# map(각 요소가 수행한 결과를 돌려줌)

# def two_times(x): return x * 2
# a = list(map(two_times, [1, 2, 3, 4]))
# print(a)

# a = list(map(lambda a: a * 2, [1, 2, 3, 4]))
# print(a)

# 외장함수(라이브러리 함수, import해서 쓰는 것)

# pickle(pickle.dump에 저장해서 언제든지 가져와 쓸 수 있는 기능)
# time(시간을 잴 수 있는 함수)
# time.sleep(x초씩 텀을 주어 값 출력)
# random(ex)로또번호)
# webbrowser(웹브라우저를 열 수 있는 기능)

# 정규표현식

# 문자 클래스[]
# ex) [abc] = "a"(O), "before"(O), "dude"(X)
# [abc] = [a-c], [012345] = [0-5]

# dot(.) (줄바꿈(￦n)을 제외한 모든 문자와 매치)
# ex) a.b = "aab"(O), "aOb"(O), "abc"(X)

# 반복(*)
# ex) ca*t = "ct"(O), "cat"(O), "caaat"(O)

# 반복(+)
# ex) ca*t = "ct"(X), "cat"(O), "caaat"(O)

# 반복({m, n}, ?)
# {m, n} == m회 이상, n회 이하
# ex) ca{2}t = "cat"(X), "caat"(O)
# ex) ca{2, 5}t = "cat"(X), "caat"(O), "caaaaat"(O)
# ? == {0, 1}와 같은 표현(0회 or 1회)
# ex) ab?c = "abc"(O), "ac"(O)

# 정규 표현식 시작하기(파이썬에서 정규 표현식을 지원하는 re모듈)

# import re
# p = re.compile('ab*')

# match

# import re
# p = re.compile('[a-z]+')
# m = p.match('3 python')
# print(m)

# search

# import re
# p = re.compile('[a-z]+')
# m = p.search('3 ptyhon')
# print(m)

# findall

# import re
# p = re.compile('[a-z]+')
# m = p.findall('life is too short')
# print(m)

# finditer

# import re
# p = re.compile('[a-z]+')
# m = p.finditer('life is too short')
# for r in m:
#     print(r)

# match 객체의 메서드 1
# .group() = 매치된 문자열을 리턴한다.
# .start() = 매치된 문자열의 시작 위치를 리턴한다.
# .end() = 매치된 문자열의 끝 위치를 리턴한다.
# .span() = 매치된 문자열의 (시작, 끝)에 해당되는 튜플을 리턴한다.

# import re
# p = re.compile('[a-z]+')
# m = p.match('python')
# print(m.group())
# print(m.start())
# print(m.end())
# print(m.span())

# 컴파일 옵션

# DOTALL, S (dot(.)사용 시 줄바꿈(\n)도 매치)

# dot(.)은 줄바꿈(\n)이 매치가 안 된다.
# import re
# p = re.compile('a.b')
# m = p.match('a\nb')
# print(m)

# DOTALL, S을 추가해주면 줄바꿈(\n)도 매치가 가능하다.
# import re
# p = re.compile('a.b', re.S)
# m = p.match('a\nb')
# print(m)

# IGNORECASE, I (대소문자 구분 없이 전부 매치)

# import re
# p = re.compile("[a-z]+", re.I)
# print(p.match('python'))
# print(p.match('Python'))
# print(p.match('PYTHON'))

# MULTILINE M (각 라인을 훑으면서 검사)

# import re
# p = re.compile("^python\s\w+", re.M)
# data = """python one
# life is too short
# python two
# you need python
# python three"""
# print(p.findall(data))

# VERBOSE, X (공백, 줄바꿈도 컴파일 가능)

# import re
# charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
# charref = re.compile(r"""
# &[#]                  # Start of a number entity referance
# (
#      0[0-7]+          # Octal form
#    | [0-9]+           # Decimal form
#    | x[0-9a-fA-F]+    # Hexadecimal form
# )
# ;                     # Trailing semicolon
# """, re.VERBOSE)

# 백슬래시(\) 문제
# \section은 " (\s)ection"으로 인식
# p = re.compile('\\section') 은 "\\"는 "\"으로 치환됨
# p = re.compile('\\\\section') 은 인식 가능
# p = re.compile(r'\\section') 으로 r(rowstring)을 사용하여 간소화

# 강력한 정규 표현식의 세계로

# 메타문자 | (or)

# import re
# p = re.compile("Crow|Servo")
# m = p.match('Crowhello')
# print(m)

# 메타문자 ^ (맨 처음)

# import re
# print(re.search('^Life', 'Life is too short'))
# print(re.search('^Life', 'My Life'))

# 메타문자 $ (맨 끝)

# import re
# print(re.search('short$', 'Life is too short'))
# print(re.search('short$', 'life is too short, you need python'))

# 메타문자 \b (공백)

# import re
# p = re.compile(r'\bclass\b')
# print(p.search('no class at all'))
# print(p.search('the declassified algorithm'))
# print(p.search('one subclass is'))

# 그룹핑 ()

# import re
# p = re.compile('(ABC)+')
# m = p.search('ABCABCABC OK?')
# print(m)
# print(m.group())

# 전방탐색 : 긍정형 (?=)

# import re
# p = re.compile('.+(?=:)')
# m = p.search("http://google.com")
# print(m.group())

# 전방탐색 : 부정형 (?!)

# import re
# p = re.compile(".*[.](?!bat$|exe$).*$", re.M)
# l = p.findall("""
# autoexec.exe
# autoexec.bat
# autoxexc.jpg
# """)
# print(l)

# 문자열 바꾸기 sub

# import re
# p = re.compile('blue|white|red')
# print(p.sub('color', 'blue socks and red shoose'))

# Greedy vs Non-Greedy (?)

# import re
# s = '<html><head><title>Title</title>'
# print(re.match('<.*>', s).group())    #Greedy
# print(re.match('<.*?>', s).group())   #Non-Greedys