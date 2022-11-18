참조 : [](https://devlog-wjdrbs96.tistory.com/253)[[Java] HashMap vs Hashtable 차이는 무엇일까? :: Gyun's 개발일지](https://devlog-wjdrbs96.tistory.com/253)

참조 : [](https://memostack.tistory.com/233)[Java - HashMap과 Hashtable의 차이](https://memostack.tistory.com/233)

### 0. 미리보는 요약본

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/67d392a3-c8c9-4a08-a9a3-845431a0a58a/Untitled.png)

### 1. HashTable vs HashMap

- 둘은 명명에서 알 수 있듯이 Hashing을 이용해 데이터를 저장한다.
  - Hashing을 활용해 `Key - Value` 형식으로 데이터를 저장한다.
    - `Key`는 중복이 불가능하지만 `Value`는 중복 가능하다.
    - 중복으로 `Key` 값이 들어오면 나중값으로 `Value` 를 덮어씌운다.
- HashMap은 컬렉션프레임워크이며 HashTable은 컬렉션 프레임워크 이전에 정의된 클래스이다.

### 2. HashTable/HashMap의 원리

- 시간복잡도 : `O(1)` : keys ⇒ Hash Function

- `Dictionary` 상속, `Cloneable` 과 `Serializable` 구현

- `Capacity` : StringBuffer/Builder에서도 사용되었던 개념, 초기용량

- `LoadFactor` = 데이터의 개수/초기용량
  
  - 언제 `Capacity` 의 용량을 두 배로 만들어 데이터를 옮길 것인지에 대한 기준점
    - 초기용량을 적게 설정한다면? ⇒ 용량 교체가 자주 발생할 수 있음
    - 초기용량을 크게 설정한다면? ⇒ 메모리 낭비가 발생할 수 있음
  - `0.75` 가 보통 기준이며, 이는 `Capacity` 의 3/4 용량이 채워질 경우 2배로 재설정함을 의미

- 해시충돌 : `1/M` 확률로 같은 공간을 가르키게 되며 이를 해시충돌이라고 한다.
  
  - open addressing : 충돌이 발생하면 근처 버킷(공간)에 자료를 저장한다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f008c3bc-0325-4c77-a1c2-a8c105e366f1/Untitled.png)
    
    - 충돌은 연쇄적으로 발생할 수 있다. A와 B가 153를 가르켜 B가 154로 가면 C가 154를 가리킬 때 이를 피해 155에 저장하는 것
  
  - Separate Chaining
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/180bddd7-54ef-43db-9400-28312b0ec053/Untitled.png)
    
    - 같은 버킷을 가르킬 때 피하지 않고 내부에서 연쇄적으로 엮는 방식
  
  - 데이터의 개수가 적을 때 open addressing 이 유리하며 데이터가 많아질수록 Chaining 방식이 유리하다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/31567bb0-383a-4f37-a5bc-63e8db86eebd/Untitled.png)

```java
public class Hashtable<K,V>
    extends Dictionary<K,V>
    implements Map<K,V>, Cloneable, java.io.Serializable {

    private float loadFactor;

    public Hashtable(int initialCapacity, float loadFactor) {

    }

    public Hashtable(int initialCapacity) {
        this(initialCapacity, 0.75f); 
    }

    public Hashtable() {
        this(11, 0.75f);
    }
}
```

### 3. HashTable과 HashMap의 차이점

- HashTable이 더 엄격한 클래스이다.
  
  - null 불가 : `key`와 `value`의 null값 불가
  - Multi-Thread 환경에서도 사용 가능 : `synchronized` 를 활용한 `Thread-Safe`
  - Enumeration 제공 : not fail-fast Enumeration을 제공
    - 내부에서 오류를 빠르게 발견해 결과값을 더 신속하게 보임
  - 해시충돌 해결 : Open Addressing ⇒ 데이터가 많아질수록 불리하다
  - 초기 Capacity 용량이 작아 데이터가 많아질수록 교체가 빈번하다.

- 하지만 HashMap은 지속적으로 개선되고 있다.
  
  - 단일 스레드 환경에서 매우 빠름
  
  - 해시충돌 해결 : Separate Chaining
  
  - 보조 해시를 사용 : 해시충돌이 적다는 성능상 이점
    
    - 기본 : java의 hashcode는 32비트의 정수를 반환한다.
    - java 8의 보조해시 함수이다.
      - 원래의 hashcode를 상위 16비트의 값과 XOR 연산한다.
    - 매우 단순하다. 왜냐하면 java8 버전부터 근본적인 로직이 개선되었기 때문이다.
    
    ```java
    //java 8 보조해시 함수
    static final int hash(Object key) { 
        int h;
      return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16); 
    }
    ```
    
    - java 8부터는 해시충돌이 많아질경우 `LinkedList` ⇒ `Tree` 를 사용한다.
    - 해시함수의 성능이 증가 ⇒ 균등분포가 증가 ⇒ 보조해시 로직이 단순화

### 4. 면접 질문 예시

1. 왜 HashTable은 null값을 사용하지 못하는가?
   
   - 설명
     
     HashTable은 key값이 없을 때 `null` 값을 반환하는 구조다. 그러므로 예외처리를 위해 `null`값을 사용할 수 없도록 한다.
     
     HashMap은 Map을 상속했고 `containsKey` 메서드를 활용해 true, false 값으로 key값의 유무를 확인할 수 있다.

2. HashMap과 HashTable의 차이점?
   
   - 위 내용 참고
