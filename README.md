# 💻Algorithm Study

꾸준함을 지향하는 알고리즘 스터디 그룹입니다.

<br>

## 👨‍💻Who

|                 스터디원                  | 사용 언어 |
| :---------------------------------------: | :-------: |
| [박승호](https://github.com/joonparkhere) |  Golang   |
| [최현진](https://github.com/HyeonjinChoi) |  Golang   |

<br>

## 🎁What

### Language 학습

해당 스터디는 다양한 언어를 경험하고자 합니다.

- Golang
  TDD (Test-Driven Development) 방식으로 배우는 Golang 서적, [Golang with Test](https://quii.gitbook.io/learn-go-with-tests/) 을 정독하여 언어 기초를 학습합니다.

<br>

### BOJ  / LeetCode 풀이

BOJ 와 LeetCode 순으로, 백준 기준 골드 난이도의 문제를 주차별 알고리즘에 맞춰 풀이합니다. ([과제 목록](https://github.com/joonparkhere/algorithm-study/blob/main/Assignment-list.md))

<br>

### 정기적인 모의 코딩 테스트

주요 알고리즘에 대한 감이 잡히면 정기적으로 모여, 제한 시간 내에 코딩 테스트 문제를 푸는 모의 시험을 진행합니다.

<br>

## 🔍How

### 비동기 커뮤니케이션 기반

매주 3~4 문제를 풀고, 풀이 코드와 설명을 각자의 Branch에 Push하고 Master Branch에 Pull Request를 보냅니다.

1명 이상의 Reviewer를 선택하고, 해당 Reviewer는 풀이 코드에 대한 피드백을 합니다.

- 피드백이 **Approve Changes**인 경우, Master Branch에 Merge함으로써 해당 주차 과제 제출을 완료합니다.
- 피드백이 **Request Changes**인 경우, 피드백을 반영하여 다시 Pull Request를 보냅니다.

<br>

### 모의 코딩 테스트

TBD.

<br>

## 📢Convention

스터디에서 서로 지키고자 하는 약속입니다.

<br>

### Code Convention

- 상호 간의 원활한 코드 리뷰를 위해 클린 코드를 지향합니다.

  메서드와 변수의 네이밍을 역할에 맞게 선정합니다.

  불필요한 주석은 달지 않습니다.

- 시간 복잡도 명시

  보다 효율적인 알고리즘을 위해, 풀이 코드의 시간 복잡도를 명시합니다.

<br>

### Commit Convention

- 커밋 타입에 맞게 메시지를 작성합니다.

  ```
  docs: README.md 등 문서 작성 및 수정
  code: 풀이 코드 제출
  fix: 풀이 코드 수정
  merge: 자신의 Branch에서 Master Branch로 병합
  ```


- 개인 Branch 명은 Github 닉네임으로 설정합니다.

<br>

### Pull Request Convention

- PR 제목은 `이름: 문제 번호 및 제목`으로 작성합니다.

  만약 BOJ에서 1234번 도시 찾기라는 문제에 대한 과제를 제출한다면, `홍길동: BOJ 1234 도시 찾기`으로 설정합니다.

- 1명 이상의 Reviewer 설정

  스터디원 중 최소 1명을 Reviewer로 설정합니다.

- PR Label 에는 해당 문제의 알고리즘 종류와 난이도를 명시합니다.

<br>

### Review Convention

리뷰어는 대상 코드의 개선점 혹은 대안 등을 Comment로 제안합니다.

제안의 정도에 따라서 **Approve Changes** 혹은 **Request Changes**를 선택해 리뷰를 남깁니다.

