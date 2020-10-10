# part 1
print(1+2);
print(3-4);
print(12*12);
print(24/2);
print(24%3);

# part 2
Helloworld = "Helloworld!";
name = "James";
print(name + " " + Helloworld);

# part 3
happy = ["dog", "family", "money", "job"];
print(len(happy));
print(happy[1]);
happy.remove(happy[0]);
print(len(happy));

# part 4
num = 1;
while num <= 5:
  print(num);
  num = num + 1;

# basic
#정수를 한 개 입력받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성해 보세요.
inputValue = int(input("첫번째 숫자 입력해주세요!"));
number = 1;
while number <= inputValue:
  print(number, ":", number * number);
  number += 1;

# basic
# 고무 공을 100 미터 높이에서 떨어뜨리는데, 이 공은 땅에 닿을 때마다 원래 높이의 3/5 만큼 튀어오릅니다. 공이 열 번 튈 동안, 그때마다 공의 높이를 계산합니다.

height = 100;
rounds = 1;
while rounds <= 10:
  try:
    height = height * (3/5);
    print(rounds, ":", height);
    rounds = rounds + 1;
  except:
    print("Error");

# part 5
# 윤년은 역법을 실제 태양년에 맞추기 위해 여분의 하루 또는 월을 끼우는 해입니다. 현재 사용하는 그레고리력의 윤년 규칙은 다음과 같습니다.

#서력 기원 연수가 4로 나누어 떨어지는 해는 윤년으로 한다. (1988년, 1992년, 1996년, 2004년, 2008년, 2012년, 2016년, 2020년, 2024년, 2028년, 2032년, 2036년, 2040년, 2044년 ...) 서력 기원 연수가 4, 100으로 나누어 떨어지는 해는 평년으로 한다. (1900년, 2100년, 2200년, 2300년, 2500년...)서력 기원 연수가 4, 100, 400으로 나누어 떨어지는 해는 윤년으로 둔다. (2000년, 2400년...)    
# Basic
leap_year = int(input("연도를 입력해주세요"));
if leap_year % 4 == 0:
  if leap_year % 100 == 0:
    if leap_year % 400 == 0:
      print("윤년입니다."); 
    else:
      print("평년3");
  else:
    print("평년2");
else:
  print("평년1.");

# part 6

family = ["mother", "father", "gentleman"];
for x in family:
  print("who:", x);


    
  
