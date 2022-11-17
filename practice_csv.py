import csv

with open('sample.csv') as f:
    csv_rows = csv.reader(f)
    for row in csv_rows:
        print(row)

"""
with: 어떤 프로세스의 시작과 끝을 자동으로 제어
open: 파일을 연다 (sample) 
as f: 파일을 open을 하면 파일 객체를 생성한다. (파일을 실행 시키면 메모리에 올라가게 된다. db와 유사하다 보면 되겠다.)
csv.reader(f): 파일 객체를 통해 csv 파일의 내용을 불러온다 -> 참고로 csv.reader(f)를 통해 나온 객체는 generator 이다.
 - 파일안에 얼마나 많은 row가 담겨 있는지 모르기 때문에 lazy하게 가져 와야 하기 때문
"""