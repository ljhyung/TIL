# Stack & Queue

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/98a21cba-7269-4a29-b4db-dbafd12f147c/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ad929867-38ae-411a-b33b-f4d930023d3d/Untitled.png)

## Stack

- 후입선출 (LIFO) : 가장 나중에 넣은 데이터를 가장 먼저 꺼낸다
- 용어 및 메소드
  - **top** - 스택의 가장 윗부분 (꼭대기)
  - **bottom** - 스택의 가장 아랫부분 (바닥)
  - **push(item)** - 데이터를 넣는 작업
  - **pop()** - 데이터를 꺼내는 작업
  - **peek()** - 스택의 가장 위에 있는 항목 조회

## Queue

- 선입선출 (FIFO) : 가장 먼저 넣은 데이터를 가장 먼저 꺼낸다.
- 용어 및 메소드
  - **front** - 데이터를 꺼내는 쪽(맨 앞)
  - **rear** - 데이터를 넣는 쪽(맨 뒤)
  - **enqueue(item)** - 데이터를 넣는 작업
  - **dequeue()** - 데이터를 꺼내는 작업
  - **peek()** - 큐의 가장 앞에 있는 항목 조회

# 자바에서 제공하는 Stack 과 Queue

스택과 큐를 구현하기 위해서 어떤 컬렉션 프레임워크를 사용하는게 좋을까?

- 스택
  - 순차적 데이터 추가/삭제
  - **ArrayList** 와 같은 배열 기반의 컬렉션이 적합
- 큐
  - 데이터를 꺼낼 때 항상 첫번재 저장된 데이터를 삭제
  - 중간에 데이터 추가/삭제가 쉬운 **LinkedList** 가 적합

```java
Stack<Integer> st = new Stack<>();
Queue<Integer> q = new LinkedList<>();   //  Queue 인터페이스의 구현체인 LinkedList 사용

st.push(1);
st.push(2);
st.push(3);

q.offer(1);
q.offer(2);
q.offer(3);

System.out.println("=====Stack=====");
while (!st.empty())
    System.out.println(st.pop());

System.out.println("=====Queue=====");
while (!q.isEmpty())
    System.out.println(q.poll());
```

```
=====Stack=====
3
2
1
=====Queue=====
1
2
3
```

java 에서 스택은 Stack 클래스로 제공하고 있지만 큐는 Queue 인터페이스로 정의되어 있다.

Queue 인터페이스를 구현한 클래스 중 하나를 선택해서 사용해야한다.

위의 예제에서는 LinkedList 를 사용했다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a6cc33d1-2d04-47ed-a2cb-d867187ad43b/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e3270060-aa34-4647-8da8-646e24f8d5bf/Untitled.png)

## **PriorityQueue**

- Queue 인터페이스의 구현체 중 하나
- 저장한 순서에 관계없이 우선순위(priority)가 높은 것부터 꺼냄
- null은 저장할 수 없음
- 각 요소를 '힙(heap)'이라는 자료구조로 저장
  - 힙 (heap) : 이진트리의 한 종류로 가장 큰 값이나 가장 작은 값을 빠르게 찾을 수 있다는 특징을 가짐

### PriorityQueue 의 추가/삭제?

## **Deque (Double-Ended Queue)**

Queue 의 변형으로, 한 쪽 끝으로만 추가/삭제 할 수 있는 Queue 와는 달리, Deque는 양쪽 끝에 추가/삭제가 가능하다. Deque 의 조상은 Queue이며, 구현체로는 ArrayDeque 와 LinkedList 등이 있다.

덱은 스택과 큐를 하나로 합쳐놓은 것과 같으며 스택으로도 사용할 수 있고, 큐로도 사용할 수 있다.

| Deque       | Queue   | Stack  |
| ----------- | ------- | ------ |
| offerLast() | offer() | push() |
| pollLast()  | -       | pop()  |
| pollFirst() | poll()  | -      |
| peekFirst() | peek()  | -      |
| peekLast()  | -       | peek() |

### Deque 구현방법 (예제코드)

---

- 참고 링크
  
  [](https://velog.io/@roro/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%8A%A4%ED%83%9D-%ED%81%90)
