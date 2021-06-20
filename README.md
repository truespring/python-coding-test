# 코딩테스트를 위한 자료공간

## IT 기업 코딩 테스트 최신 출제 경향

- 그리디(쉬운 난이도)
- 구현
- DFS/BFS 를 활용한 탐색

<img src="images/img01.jpg" alt="알고리즘 코딩 테스트 유형 분석01" width="450px" height="350px"></img>
<img src="images/img02.jpg" alt="알고리즘 코딩 테스트 유형 분석02" width="450px" height="350px"****></img>

## 복잡도(Complexity)

- 복잡도는 알고리즘의 성능을 나타내는 척도입니다.
    - 시간 복잡도: 특정한 크기의 입력에 대하여 알고리즘의 수행 시간 분석
    - 공간 복잡도: 특정한 크기의 입력에 대하여 알고리즘의 메모리 사용량 분석

- 동일한 기능을 수행하는 알고리즘이 있다면, 일반적으로 복잡도가 낮을 수록 좋은 알고리즘이다.

### 빅오 표기법(Big-O Notation)

- 가장 빠르게 증가하는 항만을 고려하는 표기법입니다.
    - 함수의 상한만을 나타내게 됩니다.

- 예를 들어 연산 횟수가 3N<sup>3</sup> + 5N<sup>2</sup> + 1,000,000인 알고리즘이 있다고 합시다.
    - 빅오 표기법에서는 차수가 가장 큰 항만을 남기므로 O(N<sup>3</sup>)으로 표현됩니다.

<img src="images/img03.jpg" alt="빅오 표기법" width="450px" height="350px"></img>

## 알고리즘 설계 Tip

- 일반적으로 CPU 기반의 개인 컴퓨터나 채점용 컴퓨터에서 연산 횟수가 5억을 넘어가는 경우:
    - C언어를 기준으로 통산 1 ~ 3초 가량의 시간이 소요됩니다.
    - Python을 기준으로 통산 5 ~ 15초 가량의 시간이 소요됩니다.
        - PyPy의 경우 때때로 C언어보다도 빠르게 동작하기도 합니다.
    - O(N<sup>3</sup>)의 알고리즘을 설계한 경우, N의 값이 5,000이 넘느다면 얼마나 걸릴까요?
    - 코딩 테스트 문제에서 시간제한은 통산 1 ~ 5초가량이라는 점에 유의하세요.
        - 혹여 문제에 명시되어 있지 않은 경우 대략 5초 정도라고 생각하고 문제를 푸는 것이 합리적입니다.

### 요구사항에 따라 적절한 알고리즘 설계하기

- 문제에서 가장 먼저 확인해야 하는 내용은 시간제한(수행시간 요구사항)입니다.
- 시간제한이 1초인 문제를 만났을 때, 일반적인 기분은 다음과 같습니다.
    - N의 범위가 500인 경우: 시간 복잡도가 O(N<sup>3</sup>)인 알고리즘을 설계하면 문제를 풀 수 있습니다.
    - N의 범위가 2,000인 경우: 시간 복잡도가 O(N<sup>2</sup>)인 알고리즘을 설계하면 문제를 풀 수 있습니다.
    - N의 범위가 100,000 경우: 시간 복잡도가 O(NlogN)인 알고리즘을 설계하면 문제를 풀 수 있습니다.
    - N의 범위가 10,000,000 경우: 시간 복잡도가 O(N)인 알고리즘을 설계하면 문제를 풀 수 있습니다.

### 알고리즘 문제 해결 과정

- 일반적인 알고리즘 문제 해결 과정은 다음과 같습니다.
    1. 지문 익기 및 컴퓨터적 사고
    2. 요구사항(복잡도) 분석
    3. 문제 해결을 위한 아이디어 찾기
    4. 소스코드 설계 및 코딩

- 일반적으로 대부분의 문제 출제자들은 핵심 아이디어를 캐치한다면, 간결하게 소스코드를 작성할 수 있는 형태로 문제를 출제합니다.

### 수행 시간 측정 소스코드 예제

- python

```angular2html
import time
start_time = time.time()  # 측정 시작

# 프로그램 소스코드
end_tiem = time.time()  # 측정 종료
print("time:", end_time - start_time)  # 수행 시간 출력
```

## 출처

- 동빈나 유튜브 영상(이것이 취업을 위한 코딩테스트다 with 파이썬) 참고