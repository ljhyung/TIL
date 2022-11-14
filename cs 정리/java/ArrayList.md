### 계층구조

```
java.lang.Object
-> java.util.AbstractCollection<E>
    -> java.util.AbstractList<E>
        -> java.util.ArrayList<E>
```

### 특징

- 가변적으로 변하는 선형리스트
- 객체들이 추가되어 저장 용량(capacity)을 초과한다면 자동으로 부족한 크기만큼 저장 용량(capacity)이 늘어난다는 특징을 가짐

### 사용

> construct (생성자)

- `ArrayList()` : initialCapacity = 10으로 빈 배열 생성
- `ArrayList(int initialCapacity)` : capacity 지정해서 생성
- `ArrayList(Collection<? extends E> c)` : 생성 시 값 추가

### 내부코드

```java
private static final int DEFAULT_CAPACITY = 10;
transient Object[] elementData;

public ArrayList(int initialCapacity) {
    if (initialCapacity > 0) {
        this.elementData = new Object[initialCapacity];
    } else if (initialCapacity == 0) {
        this.elementData = EMPTY_ELEMENTDATA;
    } else {
        throw new IllegalArgumentException("Illegal Capacity: "+
                                           initialCapacity);
}}

private static final int MAX_ARRAY_SIZE = Integer.MAX_VALUE - 8;

/**
 * Increases the capacity to ensure that it can hold at least the * number of elements specified by the minimum capacity argument. * * @param minCapacity the desired minimum capacity
 */private void grow(int minCapacity) {
    // overflow-conscious code
    int oldCapacity = elementData.length;
    int newCapacity = oldCapacity + (oldCapacity >> 1);
    if (newCapacity - minCapacity < 0)
        newCapacity = minCapacity;
    if (newCapacity - MAX_ARRAY_SIZE > 0)
        newCapacity = hugeCapacity(minCapacity);
    // minCapacity is usually close to size, so this is a win:
    elementData = Arrays.copyOf(elementData, newCapacity);
}
```

```java
import java.util.ArrayList;

List<Integer> list = new ArrayList<>();
ArrayList<Integer> list = new ArrayList<>(); // 기본 선언
ArrayList<Integer> num3 = new ArrayList<Integer>(10); //초기 용량(capacity)지정
ArrayList<Integer> list2 = new ArrayList<Integer>(Arrays.asList(1,2,3)); //생성시 값추가
```

> add (추가)

- `add (int index, E element)` [void]
- `add (E e)` [boolean]
- `addAll(int index, Collections<? extends >)` [boolean]
- `addAll(Collections<? extends >)` [boolean]

```java
List<Integer> list = new ArrayList<>();
list.add(1); // 1추가
list.add(0, 3); // 0번째에 3 추가
```

> delete (삭제)

- remove(int index)

```java
list.remove(0); // 인덱스로 삭제
```

> set (수정)

- set(int index, E element)

```java
list.set(0, 2); // 0번째를 2로 변경
```

> get (가져오기)

- get(int index)

```java
list.get(0);
```

> 기타

- size()
- contains()
- clear()
- **clone() : 얕은 복사**
- forEach()
- indexOf
- isEmpty()
- ...
  다양한 메소드들이 있다!

### 면접 질문

1. ArrayList와 Array의 차이는?
   - ArrayList는 길이가 가변적이고 Array는 길이가 불변하다!
2. ~~(관련X) Arrays.sort()와 Collections.sort()의 정렬 알고리즘~~

### 출처

- oracle java 11 공식문서 [](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/ArrayList.html)[ArrayList (Java SE 11 &amp; JDK 11 )](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/ArrayList.html)
