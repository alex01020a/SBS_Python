# 나머지 연산자 : %  정수 나누기 연산자 : //
# A += 1 => A = A+1 
# input() = 사용자로부터 데이터를 입력 받는 함수
# int : 문자열을 정수로 변환  float : 문자열을 실수로 변환  ex)int('123) => 123   int('abc') => error

# 변수 선언
a = 10
b = 12.34
c = '홍길동'

print( type(a) )
print( type(b) )
print( type(c) )

x = 10
y = 20

print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x % y =", x % y)

i = 2
j = 3
print("2의 3제곱 : ", i ** j)

# 연산자는 곱셈, 나눗셈이 덧셈, 뺄셈보다 우선이다
print(" 1 + 2 * 3 = ", 1 + 2 * 3)
print("( 1 + 2 ) * 3 =", ( 1 + 2 ) * 3 )
print(" 1 + ( 2 * 3 ) = ", 1 + ( 2 * 3 ) )