# 구구단 프로그램(함수) 만들기(n 입력하면 n단 출력)

# def GuGu(n):
#     result = []
#     i = 1
#     while i < 10:
#         result.append(n * i)
#         i = i + 1
#     return result
# print(GuGu(2))

# 3과 5의 배수 합하기

# result = 0
# for n in range(1, 1000):
#     if n % 3 == 0 or n % 5 == 0:
#         result += n
# print(result)

# 게시판 페이징하기

# def GetTotalPage(m, n):
#     if m % n == 0:
#         return m // n
#     else:
#         return m // n + 1

# print(GetTotalPage(5, 10))
# print(GetTotalPage(10, 10))
# print(GetTotalPage(15, 10))
# print(GetTotalPage(20, 10))
# print(GetTotalPage(25, 10))

# 간단한 메모장 만들기

# 탭을 4개의 공백으로 바꾸기

# 하위 디렉터리 검색하기