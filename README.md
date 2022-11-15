# 파이썬의 실행 원리 

if __name__ = "__main__":
 - __name__은 실행 주체는 main이고 그 외는 모두 해당 파일의 이름
 - 쉽게 말하면 실행 주체를 제외하고 나머지 __main__은 소속된 파일명이 된다.

### 파이썬에서의 import
from something import some
- something이라는 파일의 some이라는 클래스 혹은 메서드를 호출하여 사용 하고 싶다.
- 우리는 some이라는 메서드, 클래스를 가져다 그것만 쓰는줄 알았지만
- 사실은 something안의 모든 함수 혹은 print문 같은것들이 복붙 하듯 딸려 오는 것이다.
- 그래서 import 하는 것만으로도 호출된 파일의 print문을 출력 해준다.
