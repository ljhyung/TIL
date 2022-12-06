### JVM 메모리 구조

![JVM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ee3f4c43-4505-4bdb-8e57-bdc3d821968e/JVM.png)

1. Method Area
   - `Class` 파일을 실행하면 관련 데이터를 이곳에 저장한다.
   - `Class 변수` 도 이곳에 저장된다.
2. Call stack(=execution stack)
   - 메서드 작업에 필요한 공간 제공
   - 메서드 연산에 필요한 지역변수들과 연산 중간 결과 저장
   - 메서드 종료 시 메모리 공간 반환
   - `main` : public static void main 에서 main 메서드가 맨 아래에 깔리고 호출이 시작되는 것

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/021c6c67-a9bb-496d-a57d-2e0364add743/Untitled.png)

1. Heap
   
   - 인스턴스(+인스턴스 변수들)가 생성되는 공간
   
   - GC가 관여하는 공간
     
     - 유효한 참조를 Reaceable로 구분하고 이 참조와 연관된 모든 객체를 Reacheable로 분류
     - 이 외를 Unreacheable로 구분 후 메모리에서 삭제
   
   - String(불변 객체)값이 저장되는 곳
     
     - String: immutable 객체
       
       - 왜? immutable 인가?
         - thread-safe 하기 때문이다.
           - multi-thread 환경에서도 안정적인 값 보장
         - java의 String 데이터베이스와 연관한 값이 많다.
           - 이를 변경하지 못하도록 한 것
       - String Pool
         - **String Constant Pool**
           - `""` 로 생성 : 같은 값 = 같은 주소
         - **String Pool**
           - `new` 키워드로 생성 : 같은 값 ⇒ 다른 주소
     
     - mutable 한 객체 사용에서 나온 개념
       
       - StringBuffer vs StringBuilder
       
       - StrinBuffer : multi-thread 환경에서 사용가능하도록 `sysnchronized` 키워드 사용
         
         ```java
         @Override
         public synchronized StringBuffer append(CharSequence s) {
            toStringCache = null;
            super.append(s);
            return this;
         }
         ```
       
       - StringBuilder : multi-thread 환경에 취약
         
         ```java
         @Override
         public StringBuilder append(String str) {
            super.append(str);
            return this;
         }
         ```
