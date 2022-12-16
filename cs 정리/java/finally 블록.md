## finally 블록

> finally 블록은 예외 발생 여부와 상관없이 무조건 실행되는 문장을 의미
> → 즉 try문이 종료되면 실행된다

```java
try{
  // 예외가 발생할 가능성이 있는 코드 
}catch(Exception e){
  // 예외 처리 동작
}catch(Ex){
}finally{
    // finally 블럭은 생략 가능하다
}
```

try 문이 종료되는 상황은 다음과 같다

1. 정상적으로 블록의 끝에 도달 했을때
2. break, continue 또는 return에 의해
3. 예외가 발생했지만 catch블록에서 처리가 되었을때
4. 예와가 발생되었고 그것이 잡히지 않았을때

### ex)

```java
// ================ try-catch
try {
            System.out.println("Exception STEP 1 =======");    
        } catch(Exception e) {
            System.out.println("Exception STEP 2 =======");                
        }
// 결과물
// 1

// ================ try-finally
try {
            System.out.println("1");    
        } finally {
            System.out.println("2");                
        }
// 결과물
// 1
// 2

// ================ try-catch-finally (예외 발생x)
try {
            System.out.println("1");    
        } catch(Exception e) {
            System.out.println("2");                
        } finally {
            System.out.println("3");                
        }
// 결과물
// 1
// 3

// ================ try-catch-finally (예외 발생o)
try {
            System.out.println("1");    
            throw new Exception();
        } catch(Exception e) {
            System.out.println("2");                
        } finally {
            System.out.println("3");                
        }

// 결과물
// 1
// 2
// 3
```

## 요약

**try**문은 **catch** 또는 **finally**중 **하나는 생략가능** but **둘다 생략은 불가능**.

다만 예외처리를 할려면 정보가 담긴 Exception 클래스의 e 인스턴스가 필요하다
