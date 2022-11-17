# 파이썬의 실행 원리 

if __name__ = "__main__":
 - __name__은 실행 주체는 main이고 그 외는 모두 해당 파일의 이름
 - 쉽게 말하면 실행 주체를 제외하고 나머지 __main__은 소속된 파일명이 된다.
```python
if __name__ == '__main__':
    print("111")
```
- __name__ 이란 무엇일까?
- 공식적인 명칭은 special value

---

### 파이썬에서의 import
from something import some
- something이라는 파일의 some이라는 클래스 혹은 메서드를 호출하여 사용 하고 싶다.
- 우리는 some이라는 메서드, 클래스를 가져다 그것만 쓰는줄 알았지만
- 사실은 something안의 모든 함수 혹은 print문 같은것들이 복붙 하듯 딸려 오는 것이다.
- 그래서 import 하는 것만으로도 호출된 파일의 print문을 출력 해준다.

```python
# a.py

import b

if __name__ == '__main__':
    print("111")

    
# b.py
print("b")
```
- 위의 코드를 보았을때 결과값이 어떨지 예상이 가는가?
- 속성으로만 배웠던 나에겐 그저 111이라는 결과값만 찍힐거라 예상 했었는데
- 정답은 b가 출력되고 111이 출력 된다.

---
- 왜 b가 출력 됬을까 생각해 보았을때 b에 대한 호출이라고 생각 되는건 import b를 시킨것 밖에 없다.
- 하지만 저 import라는 구문은 사실 b.py의 코드들을 호출 한다고 생각하면 된다.
- 그럼 결국 코드가 어떻게 되느냐
```python
# a.py

import b # 기존의 import 시키던 것은 사실

print("b") # == import b

if __name__ == '__main__':
    print("111")

    
# b.py
print("b")
```
- import b를 했다는건 b의 코드들을 불러 오겠다
- 즉, b에 있는 코드들을 호출한 파일내에 포함 시키겠다 라는 뜻이다.
- 생각해 보면 구조라는게 왜 만들어 졌는지 알 수 있다고 생각 한다.
- 극 초기의 개발자들은 한 파일에 순차적으로 함수를 만들어 나갔을것이다.
- 하지만 재사용의 불편함 등으로 인해 구조라는 해결책을 냈을 것이고 함수들을 분산시켜 재사용성을 높이고 가독성을 높인것 같다.
- 결론은 import 한다는 것은 해당 파일의 코드들을 그대로 가지고 온다고 보면 될것 같다.
- 그래서 a.py에서 실행을 시켰을때 a.py 내에는 b.py의 코드들이 이미 채워져 있다고 생각 하고 위에서 부터 순차적으로 실행되어
- b가 출력되고 111이 실행 되는 것이다.

---

### sys.argv
- python python.py 인자값 인자값 인자값 인자값 ~~~

```python
import sys

print(sys.argv[1]) # python main.py {인자값} [0]은 파일명.py [1]부터 인자값 출력

input_list = sys.argv[1].split(",") # python main.py 1,2,3,4,5를 입력하면 1,2,3,4,5 리스트를 얻을수 있음 
result = 0
for i in input_list:
    result += int(i)
print(result)

result = sum([int(i) for i in sys.argv[1].split(",")])
result = sum(map(int, sys.argv[1].split(",")))
print(result)

print(f"{sys.argv[1]}를 받은 인수입니다.{sys.argv[0]}입니다.")

```

---

with: 어떤 프로세스의 시작과 끝을 자동으로 제어
open: 파일을 연다 (sample) 
      파일을 open을 하면 파일 객체를 생성한다. (파일을 실행 시키면 메모리에 올라가게 된다. db와 유사하다 보면 되겠다.)
csv.reader(f): 파일 객체를 통해 csv 파일의 내용을 불러온다 -> 참고로 csv.reader(f)를 통해 나온 객체는 generator 이다.
 - 파일안에 얼마나 많은 row가 담겨 있는지 모르기 때문에 lazy하게 가져 와야 하기 때문

 - csv.Dictreader(f): 파일 객체를 통해 csv 파일의 key, value를 불러 온다
   - 첫번째 row가 헤더값으로(Key) 들어가고 두번째 row부터(Value) 형태로 입력 된다.
   - Generator 객체 이기 때문에 next를 사용할수 있다.
   ```python
    csv_value = csv.Dictreader(f)
    next(csv_value) -> {'첫번째 row 첫번째 cell값': '두번째 row 첫번째 cell 값'...... }
 
```
---
