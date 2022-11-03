# 제네릭스(Generics)

## 제네릭스란?

Java에서 제네릭(Generic)은 Data type을 특정한 type 하나로 정하지 않고 **사용할 때마다 바뀔 수 있게** 범용적이고 포괄적으로 지정한다 라는 의미이다.

제네릭 타입은 <>을 가지는 클래스와 인터페이스를 말한다.

## 왜 제네릭인가

제네릭 타입을 사용함으로써 잘못된 타입이 사용될 수 있는 문제를 컴파일 과정에서 제거할 수 있다. 실행 시 타입 에러가 나는 것보다 컴파일 시에 에러를 사전에 방지하는 것이 좋기 때문이다. 또한 타입을 국한하기 때문에 요소를 찾아올 때 타입 변환을 할 필요가 없어 프로그램 성능이 향상된다.

```java
ArrayList list = new ArrayList(); //제네릭을 사용하지 않을경우
list.add("test");
String temp = (String) list.get(0); //타입변환이 필요함

ArrayList<String> list2 = new ArrayList(); //제네릭을 사용할 경우
list2.add("test");
temp = list2.get(0); //타입변환이 필요없음
```

## 제네릭 장점

1. 타입 안정성 제공한다.
   
   - 컴파일 타임에 타입 체크를 하기 때문에 런타임에서 ClassCastException과 같은 UncheckedException을 보장 받는다.

2. 타입 체크와 형변환 생략 가능하다.
   
   - 코드가 간결해진다.

## 제네릭 특징

모든 객체에 대해 동일하게 동작해야하는 static멤버에 타입 변수 T를 사용할 수 없다.

- T는 인스턴스 변수로 간주되기 때문이다.

- static 멤버는 인스턴스 변수를 참조할 수 없다.

```java
class Box<T> {
    static T item;    // 에러
    static int compare(T t1, T t2) { ... }    // 에
}
```



제네릭 타입의 배열을 생성하는 것도 허용되지 않는다.

- 제네릭 배열 타입의 참조변수를 선언하는 것은 가능하지만,  new T[10]과 같이 배열을 생성하는 것은 안 된다. new 연산자는 컴파일 시점에 타입 T가 무엇인지 명확히 알아야 하기 때문이다. instanceof 연산자도 같은 이유로 T를 피연산자로 사용할 수 없다.
- 꼭 제네릭 배열을 생성해야하면 'Reflecion API'의 new Instance()와 같이 클래스의 구조를 분석하여 동적으로 객체를 생성하는 메소드로 생성하거나 Object 배열을 생성해서 형변환 하는 방법을 사용한다.

## 제네릭 사용법

```java
public class 클래스명<T> {...}
public interface 인터페이스명<T> {...}
```

제네릭 타입은 타입을 파라미터로 가지는 클래스와 인터페이스를 말한다.

타입 파라미터는 정해진 규칙은 없지만 일반적으로 대문자 알파벳 한글자로 표현한다.

타입 파라미터(변수) : 제네릭에서의 타입 선언에 대한 청사진 또는 플레이스 홀더, 임의의 참조형 타입을 의미한다.

타입 인자 : 제네릭을 파라미터화하는데 사용하는 실제 타입

| 타입인자 | 설명      |
| ---- | ------- |
| <T>  | Type    |
| <E>  | Element |
| <K>  | Key     |
| <N>  | Number  |
| <V>  | Value   |
| <R>  | Result  |

## 

## 제네릭 클래스의 선언, 객체 생성과 사용

```java
class ExGeneric<T> {
    private T t;

    public void setT(T t) { 
        this.t = t;
    }

    public T getT() {
        return t;
    }
}


ExGeneric<Stirng> exGeneric = new ExGeneric<>();
```

구체적인 타입을 실제 설계한 클래스가 사용될 때 지정하면서 사용하면 타입 변환을 최소화 시킬 수 있다.

## 제한된 제네릭 클래스

### 한정된 타입 매개변수(Bounded Type)

타입 파라미터들은 제한될 수 있다.

바운드 된다는 의미는 제한된다는 의미인데 메소드가 받을 수 있는 타입을 제한할 수 있다는 것이다. 어떤 타입과 그 타입의 모든 서브 클래스들을 허용하거나, 어떤 타입과 그 타입의 모든 부모클래스들을 허용하도록 메소드를 작성할 수 있다.

```java
public class GenericTest<T extends Number> {
    public void set(T t) {}

    public static void main(String[] args) {
        GenericTest<Integer> genericTest = new GenericTest<>();

        genericTest.set("Hi!");
    }
}
```

GenericTest의 타입으로 Number의 서브 타입만 허용.

## 와일드 카드

코드에서 ?를 일반적으로 와일드 카드라고 부른다.

![](https://k.kakaocdn.net/dn/0aHCy/btqYusE6Sqi/a2zkPe3VkKvp0vBYJ5cdpk/img.png)

와일드카드 타입에 총 세가지 형태가 있으며 ?로 표현된다.



1. <?> : 타입 파라미터를 대치하는 것으로 모든 클래스나 인터페이스 타입이 올 수 있다. 
   
   - A~E 모두 가능

2. <? extends 상위타입 : 객체의 하위 클래스만 올 수 있다. 
   
   - <? extends D> : D, E 가능

3.  <? super 하위타입> : 객체의 상위 클래스만 올 수 있다.
- <? super D> : D, A 가능

## 제네릭 메소드

제네릭 메소드는 매개 타입과 리턴 타입으로 타입 파라미터를 갖는 메소드이다. 구현을 하기 위해서는 리턴 타입 앞에 <>기호를 추가하고, 타입 파라미터를 기술한 다음 리턴 타입과 매개 타입으로 타입 파라미터를 사용하면 된다.



## 제네릭 타입의 형변환



## 제네릭 타입의 제거

컴파일러가 제네릭 타입을 이용해 소스파일을 체크하고 필요한 곳에 형변환을 넣어준 후 제네릭 타입을 제거한다.

1. 제네릭 타입의 경계(bound)를 제거 : 
   
   <T extends Fruit>이면 T -> Fruit으로 치환 
   
   <T> 인 경우 T -> Object로 치환
   
   클래스 옆의 선언은 제거
   
   ```java
   // 변경 전
   class Box<T extends Fruit> { 
   	void add(T t) { . . . }
   }
   
   // 변경 후
   class Box { 
   	void add(Fruit t) { . . . }
   }
   ```

2. 제네릭 타입을 제거 후 타입이 일치하지 않으면 형변환 추가
   
   ```java
   // 변경 전
   T get(int i) {
       return list.get();
   }
   
   // 변경 후
   Fruit get(int i) {
       // List의 get()은 Object 타입을 반환해서 형변환
       return (Fruit)list.get(i);
   }
   ```





## 면접 질문

제네릭을 왜 써야 하느냐

제네릭을 대체할 방법이 무었이 있는지, 그에 비해 제네릭이 가지는 장점이나 단점
