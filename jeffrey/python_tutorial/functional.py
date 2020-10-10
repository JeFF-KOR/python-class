# 구구단

def multifly():
  for i in range(2, 10):
    for j in range(1, 10):
      print(i, "*", j, "=", i * j);

multifly();

# 재귀함수
def countDown(n):
  if n == 0:
    print("Hear we go!");
  else:
    print(n)
    countDown(n-1);

countDown(5);

# 예제: 각 자릿수를 더 한 값을 출력
# 실패
def sumoOfDigit(num):
  
  if num < 10:
    return num;
  else:
    seperated = [num];
    seperated.split("")
    sumoOfDigit(num )

sumoOfDigit(47253);

## Reference 코드
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 