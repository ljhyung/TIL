# 예외발생 (Exception Handling)

## 에러의 종류

- 컴파일 에러 : 컴파일시에 발생하는 에러
- 런타임 에러 : 실행 시에 발생하는 에러
- 논리적 에러 : 실행는 되지만, 의도와는 다르게 동작하는 것

## 런타임 에러

- 에러(Error) : 프로그램 코드에 의해서 수습될 수 없는 심각한 오류
  - 메모리부족(OutOfMemoryError)
  - 스택오버플로우(StackOrverflowError)
- 예외(Exception) : 프로그램 코드에 의해서 수습될 수 있는 다소 미약한 오류

## **예외 클래스 계층 구조**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/100b56fd-912b-4dd5-913e-a2b345559cd5/Untitled.png)

1. `Exception` 클래스와 RuntimeException를 제외한 자손(`checked`)
   - 사용자의 실수와 같은 외적인 요인에 의해 발생하는 예외
   - FileNotFoundException, ClassNotFoundException, DataFormatException
   - checked : 컴파일러가 예외처리 확인
2. `RuntimeException` 클래스와 자손 (`unchecked`)
   - 프로그래머의 실수로 발생하는 예외
   - ArrayIndexOutOfBoundsException, NullPointerException, ClassCastException, ArithmeticException
   - unchecked : 컴파일러가 예외처리를 확인하지 않음

## **예외 처리(try-catch)**

- 프로그램 실행 시 발생할 수 있는 예외에 대비한 코드 작성
- 프로그램의 비정상 종료를 막고, 정상적인 실행상태 유지
- 발생한 예외를 처리하지 못하면, 프로그램은 비정상적으로 종료되고, 처리되지 못한 예외는 JVM의 예외처리기(UncaughtExceptionHandler)가 받아서 예외의 원인을 화면에 출력

```java
try{
  // 예외가 발생할 가능성이 있는 코드 
}catch(Exception e){
  // 예외 처리 동작
}catch(Ex){
}finally{ // 예외 발생과 관련없이 무조건 수행

}
```

- Exception가 최상위 클래스이기 때문에 모든 에러를 다 처리한다.
- 에러의 작은 단위부터 catch에 먼저 적어줘야한다.

## **메서드 예외 선언**

```java
void method() throws Exception{

}

main(){
    try{ // 메소드를 부를 때 예외처리를 해줘야한다.
        method()
    }catch(Exception){

    }
}
```

- 이 예외 뿐만 아니라 자손 타입의 예외까지도 발생할 수 있다.
- 오버라이딩 할 때 단순히 선언된 예외의 개수가 아니라 상속관계까지 고려해야한다.

## **트랜잭션(Transaction)**

- 하나의 작업 단위
- 하나가 실패하면 모두 취소하고 전의 상태로 되돌려야한다.

```java
상품발송() {
    try {
        포장();
        영수증발행();
        발송();
    }catch(예외) {
        모두취소();  // 하나라도 실패하면 모두 취소한다.
    }
}

포장() throws 예외 {
   ...
}

영수증발행() throws 예외 {
   ...
}

발송() throws 예외 {
   ...
}
```

## **면접 질문**

1. 프로그래밍을 할 때 발생할 수 있는 에러의 종류를 설명해보세요.
   - 컴파일, 런타임, 논리적 에러
2. 예외처리는 어떤 우선순위로 진행 해야하는지?
   - 범위가 작은 것 부터 예외처리를 해야한다.
3. ## 예외처리가 중요한 이유는?
