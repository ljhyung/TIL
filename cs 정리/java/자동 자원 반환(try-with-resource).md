<aside>
📌 정리

- `try-with-resources` 문은 try 코드 블록이 끝나면 자동으로 자원을 종료해주기 때문에 생성한 자원을 반납해야할 때 유용하다.
- try 구문에서 사용되는 자원은 반드시 AutoCloseable 인터페이스를 구현해야 한다.
- try 안에 `;` 를 사용하여 여러 리소스를 생성할 수 있다.
  
  </aside>

JDK 1.7 부터 `try-with-resources` 문이라는 try-catch 문의 변형이 새로 추가되었다.

이 구문은 주로 입출력(I/O) 과 관련한 클래스를 사용할 때 유용하다.

주로 입출력에 사용되는 클래스 중에서는 사용한 후에 꼭 닫아줘야 하는 것들이 있다. 그래야 사용했던 자원(resources) 이 반환되기 때문이다.

```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner; 

public class ResourceClose {
    public static void main(String[] args) {
        Scanner scanner = null;
        try {
            // scanner 생성
            scanner = new Scanner(new File("input.txt"));
            System.out.println(scanner.nextLine());
        } catch (FileNotFoundException e) {
            e.printStackTrace();        
                } finally {
            // scanner 리소스 반납
            if (scanner != null) {
                scanner.close();
            }
        }
    }
}
```

try-catch-finally 구문에서 리소스를 생성하고, 반납하는 코드

리소스의 생성은 try 구문에서, 반납은 finally 구문에서 하다보니 **리소스를 생성하고 반납을 빼먹는 경우가 종종 발생**

# `Try-with-resources`

**try에 자원 객체를 전달하면, try 코드 블록이 끝나면 자동으로 자원을 종료해주는 기능**

즉, 따로 finally 블록이나 모든 catch 블록에 종료처리를 하지 않아도 된다.

```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ResourceClose {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(new File("input.txt"))) {
            System.out.println(scanner.nextLine());
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
```

try with resources 구문에 사용 되는 리소스는 (try옆의 괄호 안에서 정의 될수 있는 리소스)반드시 java.lang.AutoCloseable 인터페이스를 구현해야 한다.

예제에 사용된, Scanner 클래스도 AutoCloseable 인터페이스가 구현되어 있다.

## 여러개의 리소스 생성 반납

```java
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner; 

public class ResourceClose {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(new File("input.txt"));
                PrintWriter pw = new PrintWriter(new File("output.txt"))) {
            System.out.println(scanner.nextLine());
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
```

여러개의 리소스를 같이 생성하고 반납할 수 있다.

try 에서 리소스를 생성할 때, `;` 로 구분하여 여러 리소스를 생성할 수 있다.

⚠️ 여러개의 리소스가 같이 선언되었을 경우에는 나중에 선언된 리소스부터 close(반납) 된다.

## Custom Resource 생성하기

AutoCloseable 인터페이스를 구현하여 사용자가 리소스 클래스를 생성할 수도 있다.

```java
public class CustomResource implements AutoCloseable {
     public CustomResource() {
        System.out.println("CustomResource Constructor");
    }
     public void printMessage() {
        System.out.println("CustomResource Print Message");
    }
     @Override
     public void close() throws Exception {
        System.out.println("CustomResource close");
     }
}
```

```java
public class ResourceClose {
    public static void main(String[] args) {
        try (CustomResource cr = new CustomResource()) {
            cr.printMessage();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

```
CustomResource Constructor
CustomResource Print Message
CustomResource close
```

close()를 따로 호출하지 않았지만, 자동으로 호출되어 "CustomResource close" 메세지가 출력된 것을 확인할 수 있다.

---

- 참고링크
  
  [[Java] Try with resources 로 자원 반납하기](https://hianna.tistory.com/546)
