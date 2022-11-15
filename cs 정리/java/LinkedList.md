## LinkedList란..

자바의 Collection 프레임 워크중 하나

데이터가 메모리상 연속되게 할당되는 방식이 아니라

**값**과 다음 노드의 **주소**를 가지는 **노드**라는 이름의 자료구조의 연결체 이다.

노드는 아래와 같은 형태로 존재(양방향 연결이라면 포인터가 좌우로 존재)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7a48683f-7d49-41e7-acf7-bf4c183d17ce/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b8195bbb-be73-4778-958c-a5412c01fc4d/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/79608adf-06f4-47b5-8ce6-80ca40a5d7d1/Untitled.png)

ArrayList 같은 경우 연속되게 할당되어 변수의 크기(몇Byte 인지)가 정해져 있기 때문에 메모리에서 쉽게 찾을 수 있음

- a[5]의 값을 얻고 싶다면 순서대로 올 필요 없이 첫 원소의 주소와, 원소의 크기, 찾아갈 인덱스만 있으면 계산되어 나옴

LinkedList 경우 노드마다 다음 노드의 주소를 가지고 있기 때문에 무조건 순차적으로 접근을 해야함 → 따라서 ArrayList보다 연산에 있어서 느림

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0ef8ad6c-d764-4cdc-9a7d-8f27e9f56db2/Untitled.png)

- amortized 라고 되어있는 부분은 분할 상환분석 이라는 시간 복잡도를 분석하는 기법중 하나인 것으로 보이고, 여기에서 다루기엔 딥해 보여서 나중에 시간 되면 개별 문서를 작성할 예정

## 성능표

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/342e659d-fdb8-4eda-b4c9-5ed6f4ee2db6/Untitled.png)

### 한줄 요약

조회시 ArrayList가 우위

삽입 / 삭제시 LinkedList가 우위

## LinkedList 사용법

```java
// LinkedList 객체 선언
LinkedList li = new LinkedList(); // 타입 설정x, object로 입력
LinkedList<LinkedListDemo> li = new LinkedList<LinkedListDemo>(); // List타입을 LinkedListDemo
LinkedList<Integer> li = new LinkedList<Integer>(); // int 타입으로 선언
LinkedList<Integer> li = new LinkedList<>(); // 타입 선언 생략도 가능
LinkedList<Integer> li = new LinkedList<Integer>(Arrays.asList(1, 2, 3)); // 초기화 할때 값 할당 가능        
LinkedList<String> li = new LinkedList<String>(); // String 타입 사용
LinkedList<Character> li = new LinkedList<Character>(); // Char 타입 사용

// LinkedList 값 추가하기.add()
li.add(object); // 맨끝에 추가하는 방식
li.add(int index, object); // 해당 위치에 추가

// LinkedList 원소값 변경 set() - 특정값을 바꾸는 것이기 때문에 index값이 필수
li.set(int index, object);

// LinkedList 값 삭제
li.removeFirst(); // 리스트 첫번째 데이터를 삭제
li.removeLast(); // 리스트 마지막 데이터를 삭제

li.remove(); // 리스트 첫번째 데이터 삭제
li.remove(int index); // 해당 위치 데이터 삭제

li.clear(); // 리스트의 모든데이터를 삭제

// LinkedList 크기 .size()
a = li.size(); // 로 쓰거나 print로 출력하거나 하면된다.

// LinkedList 값 검색 .contains(), indexOf();
li.contains(object); // 해당 값이 있는지 없는지만 판단 (true or false)
li.indexOf(object); // 해당 값의 첫번째 위치를 반환, 없으면 -1을 반환
```

## 면접 질문

Array, LinkedList는 무엇인지

- Array는 인덱스와 인덱스에 대응하는 데이터로 이루어져 있는 선형 자료구조?
- LinkedList 데이터와 포인터를 가지고 있는 선형 자료구조?

각 차이점은 뭐가 있는지

- 각 장점을 말하면 될거같음

시간복잡도?

- 어거지 질문

## 부록) 연결 리스트 종류와 삽입/삭제 방식

필요 하다면 설명

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/73248f74-9186-479e-8e41-5a2dd2fc2127/Untitled.png)
