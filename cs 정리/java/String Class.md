# 면접 질문 정리

### **1. 자바에서 String은 무엇인가? 데이터 타입인가?**

String은 int, long, double과 같은 primitive data type은 아니고 클래스 혹은 더 간단히 사용자 정의 타입입니다.

java.lang 패키지에 정의되어 있고 내부적으로는 character array에 저장되어 있습니다. (java9부터는 compact string과 관련해서 byte array로 저장됨)

### **2. 자바에서 String은 왜 final로 선언되어 있나?**

String은 보안, 최적화, String pool 유지를 위해서 final로 선언되어 있습니다.

```java
public final class String
    implements java.io.Serializable, Comparable<String>, CharSequence {
```

immutable은 변하지 않기 때문에 thread간 공유 시에 lock이 필요없고, 중복된 값에 대해서 메모리에 하나만 저장하면 되기 때문에 공간 절약이 됩니다.

### **3. String과 StringBuffer의 차이가 무엇인가?**

String 객체는 immutable 합니다.

즉 한번 생성이 되면 변경이 불가능 합니다.

예를 들면 String 2개를 연결하는 작업을 할 때에 새로운 String을 객체를 이용하여 문자열을 참조하게 됩니다.

StringBuilder와 StringBuffer는 mutable(가변성)하며 .append() .delete() 등의 API를 이용하여 동일 객체 내에서 문자열을 변경하는 것이 가능합니다.

문자열의 추가, 수정, 삭제가 빈번하게 발생할 때 사용합니다.

추가로 StringBuilder와 StringBuffer의 차이점은 멀티쓰레드 상태에서 동기화의 지원 여부가 다릅니다.

StringBuffer은 멀티쓰레드 환경에서 동기화를 보장하지만 StringBuilder은 동기화를 보장하지 않습니다.

- JDK 1.5버전 이하에서는 String을 사용할때 StringBuilder와 성능 차이가 있었지만 1.5버전 이후부터는 String을 컴파일 할때 자동적으로 StringBuilder로 컴파일 하여 실행되므로 성능 차이가 사라졌다고 합니다.

### **4. C와 Java에서 String의 차이가 무엇인가?**

C는 선언했을 때 null로 끝나는 문자배열이고 자바에서 String은 객체이며 기본적으로 빈 배열로 초기화가 됩니다.

Java의 String은 C보다 더 많은 기능이 있습니다.

### **5. 왜 비밀번호를 저장에 String보다 char array가 더 나을까?**

1. Java에서 **문자열은 변경할 수 없으므로** 암호를 일반 텍스트로 저장하면 가비지 수집기가 이를 지울 때까지 메모리에서 사용할 수 있으며 문자열은 재사용성을 위해 문자열 풀에서 사용되기 때문에 오랜 시간 동안 메모리에 남아있을 확률이 높고 이는 보안 위협으로 이어질 수 있습니다.

메모리 덤프에 액세스할 수 있는 사람은 누구나 암호를 일반 텍스트로 찾을 수 있기 때문에 항상 일반 텍스트보다 암호화된 암호를 사용해야 하는 또 다른 이유입니다.

문자열은 변경할 수 없기 때문에 문자열의 내용을 변경할 수 있는 방법은 없습니다.

[변경하면 새 문자열이 생성](http://javarevisited.blogspot.com/2011/07/string-vs-stringbuffer-vs-stringbuilder.html) 되기 때문입니다 .

반면 char[]이면 여전히 모든 요소를 공백이나 0으로 설정할 수 있습니다.

그래서 **문자 배열에 암호를 저장하면 암호 도용의 보안 위험을 확실히 완화**할 수 있습니다.

.

### **6. 자바에서 문자열 비교는 어떻게 하나?**

1. equals method (자주 사용)

2. equalsIgnoreCase method

3. compareTo method (compareTo == 0으로 확인, 자주 사용)

4. compareToIgnoreCase method

### 7. 자바 생성 방식 중 new 연산자를 이용한 방식과 리터럴을 이용한 방식의 차이는 무엇인가?

자바7 이전에는 new로 String을 생성하면 Heap 영역에 존재하게 되고 리터럴을 이용할 경우 string constant pool이라는 영역에 존재하게 되는데 string constant pool은 Permanent(이하 perm) 영역에 존재합니다.

하지만 perm영역은 고정 사이즈이기 때문에 OOM(Out Of Memory) 문제로 string constant pool 또한 heap 영역으로 변경되었습니다.

따라서 String 객체들도 GC에 의해 할당해제가 되면서 메모리 관리가 됩니다.

### 8. String constant pool이란?

- 일단 method area(또는 클래스영역)의 runtime constant pool과는 별개의 영역이기 때문에 구분해서 이해해야 합니다.
  
  - **runtime constant pool**: 클래스 내의 final 제어자가 붙어있는 모든 상수들에 대한 symbol table을 관리(레퍼런스를 저장).
    클래스 영역(method, data, static 영역, 동의어)에 저장
    정적 공간이라는 이름처럼 프로그램이 종료될 때까지 메모리에 남아있고 GC가 동작하지 않습니다.
  - **String constant pool**: 리터럴로 초기화된 String 변수값을 저장함. `Heap` **영역 내에 있는 String constant pool에 저장**
  
  ```java
  String s1 = "apple";
  String s2 = new String("banana");
  ```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7ca38e8e-7e0c-48d6-8144-b8d7505b3644/Untitled.png)

String 생성 방식에 따른 리터럴 저장위치 차이

- **new로 생성하면 Heap 영역에 저장**
  - String pool에 존재하는 다른 같은 값의 객체가 있던 별개의 주소를 가진 객체
- **String 리터럴로 생성하면 해당 값은 heap영역 내의 string constant pool에 저장됨(String interning)**
  - String을 literal로 선언하면 내부적으로 String의 intern()메서드가 호출되면서 string constant pool을 탐색합니다.
    같은 값이 있으면 주소를 반환해주고 없으면 constant pool에 넣고 새로운 주소를 반환합니다.

### 9. 자바에서 불변 객체를 이용하는 이유는?

- [자바를 직접 만든 제임스 고슬링에 따르면](https://www.artima.com/articles/james-gosling-on-java-may-2001#part13) 캐싱, 보안, 복사가 필요없는 빠른 재사용성, 동기화 성능 때문입니다.
  - 보안적인 이슈: 만약 네트워크 통신을 통해서 받은 ID와 password String이 mutable하다면 validation을 거친 이후에도 받아온 String이 안전한지 알수 없습니다.
  - 동기화 이슈: 애초에 변경 불가능한 불변객체이면 여러 쓰레드에서 접근해도 thread-safe(쓰레드 세이프)하기 때문에.
  - String.hashCode() 이용한 캐싱: String이 불변객체이므로 이를 키값으로 이용한 해싱 컬렉션의 퍼포먼스가 향상됩니다.
    hashcode()로 정수값을 받아 키값으로 이용하도록 컬렉션들이 설계되어 있기 때문에 이 방식은 String pool에서도 사용되서 결과적으로 기존에 캐싱된 String값이 있는지 빠르게 조회할 수 있다.

---

# ※ Runtime constant pool이란?

## 자바 메모리 - Runtime Data Area

런타임 데이터 영역(Runtime Data)은 실제 클래스 파일이 적재되는 곳으로 JVM이 OS로부터 자바 프로그램 실행을 위한 데이터와 명령어를 저장하기 위해 할당받는 메모리 공간이다.

주로 `메소드`, `힙`, `스택` 영역을 언급한다.

![Runtime Data Area](https://blog.kakaocdn.net/dn/SDLq7/btriooQgkjm/rbKq3AxnpbkmUNBg69VNr1/img.png)

Runtime Data Area

- **메소드(=클래스=스태틱) 영역**
  - 가장 먼저 데이터가 저장됨
  - 클래스 로더에 의해 로드된 클래스, 메소드 정보와 클래스 변수 정보 저장
  - 클래스 변수 남발 시 메모리 공간 부족할 수 있음
    - Java 7의 경우 부족할 수 있었으나 Java 8부터는 개선됨
  - 프로그램 시작부터 종료될 때까지 메모리에 적재
  - 명시적 null 선언 시 GC가 청소
  - 모든 스레드가 공유함
- **힙 영역**
  - 런타임 시 결정되는 참조 자료형이 저장됨
    - 런타임 시 결정됨에 따라 동작 중의 문제(범위 초과 참조 등)가 발생할 코드임에도 문법의 문제는 아니기에 컴파일 시 에러를 출력하지 않음
  - new 연산자를 통해 생성된 객체(인스턴스)가 저장되는 공간
    - 즉, 인스턴스 변수도 여기에 저장됨
  - 객체가 더 이상 쓰이지 않거나 명시적 null 선언 시 GC가 청소
  - 모든 스레드가 공유함
- **스택**
  - 컴파일 시 결정되는 기본 자료형(&참조변수)이 저장됨
    - 컴파일 시 결정됨에 따라 자료형의 범위를 초과한 값 할당 등의 코드가 컴파일 단계에서 검출됨
    - 참조 변수는 기본 자료형을 Wrapper Class로 boxing한 변수(Integer, Byte 등)
  - 메소드 호출 시 메모리에 FILO로 삽입
  - 메소드 종료 시 메모리에서 LIFO로 제거
  - 메소드가 호출될 때마다 각각의 스택 프레임이 생성됨
    - 각 스택 프레임은 하나의 메소드에 대한 정보를 저장
  - {} 혹은 메소드가 종료될 때 삭제됨
    - 메소드 종료 시 프레임 별로 삭제
  - 각 스레드 별로 생성
- PC 레지스터
  - JVM이 수행할 명령어의 주소를 저장하는공간
    - OS의 PC 레지스터와 유사한 역할이나 CPU와는 별개로 JVM이 관리
  - 스레드가 시작될 때마다 생성됨
  - 각 스레드 별로 생성
- 네이티브 메소드 스택
  - 바이트 코드가 아닌 기계어로 작성된 코드를 실행하는 공간
  - 다른 언어(c/c++)로 작성된 코드를 수행하기 위함
  - Java Native Interface를 통해 바이트 코드로 변환됨
  - Java Code를 수행하다 JNI 호출 시 Java Stack에서 Native Stack으로 동적 연결(Dynamic Linking)을 통해 확장됨
    - 따라서 나뉘어졌다고는 하나 stack에서 연결할 수 있음
  - JNI(Java Native Interface) 호출 시 생성
  - 각 스레드 별로 생성

---

## Runtime Data Area의 구분

그런데 변수 저장에 대해 공부하다 보면 위의 내용에 따라 클래스 변수는 Method Area에 저장된다는데 오라클 문서에 따르면 logical하게는 heap에 속한다 설명한다.

엄밀하게 각 영역별로 어떻게 구성되는지 따져보고자 한다.

크게 저장 공간에 따라 heap과 stack으로 구성되고 그 내부에 다른 영역이 포함된다고 간주하면 되겠다.

### Heap 영역? Method 영역?

![https://blog.kakaocdn.net/dn/EctUX/btripGbRQDJ/Bb6qix5JgcHD1ondHKCduK/img.png](https://blog.kakaocdn.net/dn/EctUX/btripGbRQDJ/Bb6qix5JgcHD1ondHKCduK/img.png)

위 그림은 일반적으로 jvm의 heap 구조를 설명할 때 사용하는 그림이다.

그런데 permanent 영역은 보통 heap취급을 하지 않지만 이렇게 heap 영역에 "포함된" 상태다.

그런데 일반적으로 permanent 영역과 heap 영역은 구분해서 설명한다.

그리고 Method 영역은 permanent 영역에 속해있어 heap 영역이 아니라고 보통 이야기한다.

따라서, heap 영역에 포함되어 있기는 하나 heap 영역과는 구분해서 간주함으로 인해 오라클 문서에서 logical하게는 heap의 한 부분이라고 설명하는 것이다.

### Heap의 Permanent Generation영역 변화

- Java 7 JVM

```
<----- Java Heap -----------------> <--- Native Memory --->
+------+----+----+-----+-----------+--------+--------------+
| Eden | S0 | S1 | Old | Permanent | C Heap | Thread Stack |
+------+----+----+-----+-----------+--------+--------------+
                        <--------->
                       Permanent Heap
S0: Survivor 0
S1: Survivor 1
```

- Java 8 JVM

```
<----- Java Heap -----> <--------- Native Memory --------->
+------+----+----+-----+-----------+--------+--------------+
| Eden | S0 | S1 | Old | Metaspace | C Heap | Thread Stack |
+------+----+----+-----+-----------+--------+--------------+
```

Permanent 영역은 JVM에 의해 크기가 제한된 영역으로 Java 7까지 유지되었다.

따라서 영역 제한으로 인해 메모리 범위 초과 문제가 있었다.

대신 Java 8부터는 Permanent Generation을 제거하고 Metaspace로 대체하였고
heap이 아니라 JVM에 의해 메모리가 제한되지 않는 Native Memory 영역으로 전환하여
OS에 의해 메모리 할당 공간이 자동으로 조절되므로 이론상
아키텍쳐가 지원하는 메모리 크기까지 확장할 수 있다.

따라서, 애매하게 heap에 걸쳐있던 permanent 영역이 non-heap이라고 구분하던 과거와는 달리
명확하게 method area는 heap이 아니라고 정의할 수 있게 되었다.

변경 이유는 ArrayList와 같은 레퍼런스 타입의 동적 배열 객체를 static으로 생성하면 레퍼런스를
Permanent 영역에 저장하는데 해당 객체 배열에 객체 원소를 추가하면
그대로 static object의 레퍼런스가 Permanent 영역에 쌓일 뿐만 아니라
string literal data를 저장하던 string pool도 permanent 영역에 저장하느라
OOM 에러가 발생하는 이슈가 잦았다고 한다.

### Permanent에서 Metaspace로 변경됨에 따른 변화

오라클 문서에 The proposed implementation will allocate class meta-data in native memory and move interned Strings and class statics to the Java heap. Hotspot will explicitly allocate and free the native memory for the class meta-data.라고 나와있다. 해석하자면 class meta-data는 native memory로 이동된 Metaspace에 저장하고 permanent에 저장했던 interned strings와 static 변수는 heap 영역으로 보낸다는 의미가 된다. Java8부터는 static 변수를 heap영역에서 관리함은 gc 대상이 될 수 있음을 의미한다. 으레 다들 설명하듯 PermGen에 속한 Method area가 클래스 변수를 저장한다고 알고 있다면 이해하기 쉽지 않다. static 변수는 클래스 변수로 명시적 null 선언이 되지 않으면 gc되어서는 안되는 변수다. Method area가 클래스 변수를 저장한다고 이해하는 시점에서 오해가 발생한다 Method area는 class의 meat-data를 저장할 뿐 실질적인 객체와 데이터는 Method area 바깥의 PermGen에 저장됨을 알아야 한다.

class meta-data가 metaspace로 이동하고 기존에 perment 영역에 저장되던 static object는 heap영역에 저장되도록 변경되었다고 설명하는데 이는 reference는 여전히 metaspace에서 관리됨을 의미하기에 참조를 잃은 static object는 GC의 대상이 될 수 있으나 reference가 살아있다면 GC의 대상이 되지 않음을 의미한다.

따라서, metaspace는 여전히 static object에 대한 reference를 보관하며 애매하게 heap에 걸쳐지지 않고 non-heap(native memory)로 이관되며 static 변수(primitive type, interned string)는 heap 영역으로 옮겨짐에 따라 GC의 대상이 될 수 있게끔 조치한 것이다.

이 내용을 언급하는 이유는 클래스 변수 및 객체의 저장위치와 클래스 메타 정보의 위치가 Method 영역이 속한 ParmGen으로부터 Heap과 메모리로 서로 분리되었다는 점을 의미하기 때문이다.

### Stack 영역

![https://blog.kakaocdn.net/dn/brMEvP/btriooJwkPp/Wkei5HinstBQzMgoeiod70/img.png](https://blog.kakaocdn.net/dn/brMEvP/btriooJwkPp/Wkei5HinstBQzMgoeiod70/img.png)

PC 레지스터와 스택, Native Method 스택은 각 스레드마다 생성된다고 설명했다. 그리고 스택에는 메소드 호출마다 프레임이 생성되어 쌓이며 프레임에는 리턴할 값, 지역 변수, 연산자 스택, 현재 클래스 constant pool의 값을 호출할 레퍼런스가 있다. 이 레퍼런스를 통해 클래스, 인스턴스 변수들이나 생성된 참조 자료형을 호출한다.

> 출처: [](https://8iggy.tistory.com/229)[Java 런타임 데이터 영역 :: 스터디룸](https://8iggy.tistory.com/229)
