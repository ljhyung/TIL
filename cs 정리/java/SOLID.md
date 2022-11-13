# 객체 지향 설계를 위한 원칙

`SOLID`란

- **SRP (Single Responsibility Principle) 단일 책임 원칙**
- **OCP (Open Closed Principle) 개방 폐쇄 원칙**
- **LSP (Liskov Substitution Principle) 리스코프 치환 원칙**
- **ISP (Interface Segregation Principle) 인터페이스 분리 원칙**
- **DIP (Dependency Inversion Principle) 의존 역전 원칙**

의 앞글자를 따서 만들어진 용어 [로버트 C.마틴 출처]

객체지향의 4대 특성

- 캡슐화
- 상속
- 추상화
- 다형성

이 특성을 활용해 객체 지향을 올바르게 설계할 수 있는 원칙을 정리한 것이 SOLID

잘된 설계란 클래스 내부의 응집도는 높이고, 다른 클래스와의 결합도는 낮추는 High Cohension - Loose Coupling 원칙을 객체 지향 관점에서 도입한 것.

모듈 또는 클래스마다 하나의 책임을 부여해 더욱 독립된 모듈과 클래스를 만들기 위함.

이렇게 설계된 소프트웨어는 재사용성이 좋아지고 수정이 최소화되기 때문에 유지보수가 용이해짐.

### 1. **단일 책임 원칙 - Single Responsibility Principle - SRP**

> **"어떤 클래스를 변경해야 하는 이유는 오직 하나 뿐이어야 한다." -로버트 C. 마틴**

- 의미: 모든 클래스는 각각 하나의 책임만을 가지라는 의미

즉 클래스를 설계할 때 어플리케이션의 경계를 정하고, 추상화를 통해 어플리케이션 경계 안에서 필요한 속성과 메서드를 선택하여 설계 해야 함을 의미

예시1) 하나의 클래스에 유저정보(프로필)와 채팅 정보를 동시에 보유 중

```java
public class ChatProfile {
    private String userName;
    private int age;
    private String profileImage;
    private String chatRoomName;
    private String[] recentChatMessage;
    private int numberParticipants;

    // getter and setter
}
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e4589fc6-40f3-4c74-b857-6545a13c7c9f/Untitled.png)

만약 프로필 정보만 보여줄 거라면 당연히 채팅정보는 불필요

클래스에 여러 가지 책임을 부여하면 클래스 크기가 커지므로 가독성에도 안 좋고 무엇보다 SRP를 위배하게 됨

예시2)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c6519737-1a00-41c4-986c-cbc579b79c26/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0ee576ab-8dfd-47c5-9ed9-e7e13c2aeedb/Untitled.png)

---

### 2. 개방 폐쇄 원칙 - **Open Closed Principle - OCP**

> "소프트웨어 엔티티(클래스,모듈,함수 등)는 확장에 대해서는 열려 있어야 하지만
> 변경에 대해서는 닫혀 있어야 한다."

- 로버트 C. 마틴

예시) 각 차량마다 다른 클래스를 만들게 되면 새로운 차를 만들 때 또 새로운 클래스를 만들어야 할 수도 있으며 각 클래스간 호환이 불가능하기 때문에 유지보수성이 낮아짐

또한 해당 클래스를 사용하는 운전자는 사용하는 자동차 클래스가 달라질 때마다 사용성 또한 달라질 수 있음

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d0ade623-7f4b-4c7e-8836-79799a544beb/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/449755fd-223e-4f7f-b5ed-6a4852d59535/Untitled.png)

하지만 자동차란 인터페이스를 만들고 이것을 각 자동차가 상속받는다면 새로운 종류의 차량 또한 자동차 인터페이스를 상속받음으로써 확장성이 증가하고 운전자는 그 변경 사항에 영향을 받지 않음

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6d3db13a-5918-4224-abb9-ee82db38cf5a/Untitled.png)

예시2)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9f76096c-9b37-4010-956a-9401c7cb64f0/Untitled.png)

---

### 3. 리스코프 치환 원칙 - **Liskov Substitution Principle - LSP**

> "서브 타입(자식)은 언제나 자신의 기반 타입(부모)으로 교체할 수 있어야 한다."

- 로버트 C 마틴

- 의미
  
  - 특정 메소드가 상위 타입을 인자로 사용한다고 할 때, 그 타입의 하위 타입도 문제 없이 정상적으로 작동을 해야 하는 것
  - 부모 객체를 호출하는 동작에서 자식 객체가 부모 객체를 완전히 대체 가능한 것

예시) “정사각형은 직사각형이다”

### ● 리스코프 치환 원칙을 위배한 코드

```java
/**
 * 직사각형 클래스
 * @출처 <https://blog.itcode.dev/posts/2021/08/15/liskov-subsitution-principle>
 * @author RWB
 * @since 2021.08.14 Sat 11:12:44
 */
public class Rectangle
{
    protected int width;
    protected int height;

    /**
     * 너비 반환 함수
     *
     * @return [int] 너비
     */
    public int getWidth()
    {
        return width;
    }

    /**
     * 높이 반환 함수
     *
     * @return [int] 높이
     */
    public int getHeight()
    {
        return height;
    }

    /**
     * 너비 할당 함수
     *
     * @param width: [int] 너비
     */
    public void setWidth(int width)
    {
        this.width = width;
    }

    /**
     * 높이 할당 함수
     *
     * @param height: [int] 높이
     */
    public void setHeight(int height)
    {
        this.height = height;
    }

    /**
     * 넓이 반환 함수
     *
     * @return [int] 넓이
     */
    public int getArea()
    {
        return width * height;
    }
}
```

Rectangle은 직사각형을 구현한 객체이기에 너비와 높이를 지정, 반환할 수 있으며 지정된 값을 통해 자신의 넓이를 계산할 수 있음.

정사각형 역시 넓게 보면 직사각형의 한 종류이기 때문에 직사각형을 상속하여 정사각형 객체를 만들 수 있을까?

```java
/**
 * 정사각형 클래스
 *
 * @author RWB
 * @since 2021.08.14 Sat 11:19:07
 */
public class Square extends Rectangle
{
    /**
     * 너비 할당 함수
     *
     * @param width: [int] 너비
     */
    @Override
    public void setWidth(int width)
    {
        super.setWidth(width);
        super.setHeight(getWidth());
    }

    /**
     * 높이 할당 함수
     *
     * @param height: [int] 높이
     */
    @Override
    public void setHeight(int height)
    {
        super.setHeight(height);
        super.setWidth(getHeight());
    }
}
```

위처럼 정사각형 객체 Square를 Rectangle의 상속을 통해 빠르게 구현하였음.

정사각형의 경우 직사각형과 달리 너비와 높이가 같으니 너비나 높이를 지정하면 그에 맞게 너비와 높이를 모두 일치시켜주도록 오버라이딩을 하였음.

구현한 Rectangle의 넓이를 구해보면

```java
/**
 * 메인 클래스
 *
 * @author RWB
 * @since 2021.06.14 Mon 00:06:32
 */
public class Main
{
    /**
     * 메인 함수
     *
     * @param args: [String[]] 매개변수
     */
    public static void main(String[] args)
    {
        Rectangle rectangle = new Rectangle();
        rectangle.setWidth(10);
        rectangle.setHeight(5);

        System.out.println(rectangle.getArea());
    }
}

// output : 50
```

Rectangle의 넓이는 너비가 10, 높이가 5이기 때문에 넓이 50이 정상적으로 반환됨.

리스코프 치환 원칙에 의하면, 자식 객체는 부모 객체를 완전히 대체할 수 있다고 했으므로, Rectangle을 상속받은 square로 대체하여 넓이를 구해보면 동일한 결과인 50을 반환해야 함.

```java
/**
 * 메인 클래스
 *
 * @author RWB
 * @since 2021.06.14 Mon 00:06:32
 */
public class Main
{
    /**
     * 메인 함수
     *
     * @param args: [String[]] 매개변수
     */
    public static void main(String[] args)
    {
        Rectangle rectangle = new Square();
        rectangle.setWidth(10);
        rectangle.setHeight(5);

        System.out.println(rectangle.getArea());
    }
}

//output: 25
```

50이 아닌 25로 반환된 이유는 setHeight(5)를 통해 가로, 세로 모두 5가 할당되었기 때문.

이 객체는 리스코프 치환 원칙에 위배되는 코드이며 따라서 직사각형과 정사각형은 상속관계가 될 수 없음.

사각형의 특징을 서로 가지고 있지만, 두 사각형 모두 사각형의 한 종류일 뿐, 하나가 다른 하나를 완전히 포함하지 못하는 구조이기 때문.

이렇게 잘못된 객체를 상속하거나, 올바르게 확장하지 못 할 경우 겉으로 보기엔 정상적이지만 올바른 객체는 아님.

### ● 리스코프 치환 원칙을 준수한 코드

올바른 상속과 구현을 통해 리스코프 치환 원칙에 부합한 코드를 작성할 수 있음.

직사각형과 정사각형은 상속의 관계가 성립되기 어렵기 때문에 이보다 더 상위 개념인 사각형 객체를 구현하고 정사각형, 직사각형이 이를 상속받으면 되는 것.

```java
/**
 * 사각형 객체
 *
 * @author RWB
 * @since 2021.08.14 Sat 11:39:02
 */
public class Shape
{
    protected int width;
    protected int height;

    /**
     * 너비 반환 함수
     *
     * @return [int] 너비
     */
    public int getWidth()
    {
        return width;
    }

    /**
     * 높이 반환 함수
     *
     * @return [int] 높이
     */
    public int getHeight()
    {
        return height;
    }

    /**
     * 너비 할당 함수
     *
     * @param width: [int] 너비
     */
    public void setWidth(int width)
    {
        this.width = width;
    }

    /**
     * 높이 할당 함수
     *
     * @param height: [int] 높이
     */
    public void setHeight(int height)
    {
        this.height = height;
    }

    /**
     * 넓이 반환 함수
     *
     * @return [int] 넓이
     */
    public int getArea()
    {
        return width * height;
    }
}
```

```java
/**
 * 직사각형 클래스
 *
 * @author RWB
 * @since 2021.08.14 Sat 11:12:44
 */
class Rectangle extends Shape
{
    /**
     * Rectangle 생성자 함수
     *
     * @param width: [int] 너비
     * @param height: [int] 높이
     */
    public Rectangle(int width, int height)
    {
        setWidth(width);
        setHeight(height);
    }
}
/**
 * 정사각형 클래스
 *
 * @author RWB
 * @since 2021.08.14 Sat 11:19:07
 */
class Square extends Shape
{
    /**
     * Square 생성자 함수
     *
     * @param length: [int] 길이
     */
    public Square(int length)
    {
        setWidth(length);
        setHeight(length);
    }
}
```

shape를 상속받는 Rectangle은 인스턴스 생성 시 width와 height를, Square 객체는 length 하나만을 파라미터로 받음.

```java
/**
 * 메인 클래스
 *
 * @author RWB
 * @since 2021.06.14 Mon 00:06:32
 */
public class Main
{
    /**
     * 메인 함수
     *
     * @param args: [String[]] 매개변수
     */
    public static void main(String[] args)
    {
        Shape rectangle = new Rectangle(10, 5);
        Shape square = new Square(5);
        System.out.println(rectangle.getArea());
        System.out.println(square.getArea());
    }
}

//output
// 50
// 25
```

이제 Rectangle과 Square는 상속 관계가 아니므로 결과 값이 달라도 되며, 리스코프 치환 원칙을 위배하지 않게 됨.

### 정리

리스코프 치환 원칙은 상속되는 객체는 반드시 부모 객체를 완전히 대체해도 아무런 문제가 없도록 권고
위의 직사각형과 정사각형의 케이스처럼 올바르지 못한 상속관계는 제거하고, 부모 객체의 동작을 완벽하게 대체할 수 있는 관계만 상속하도록 코드를 설계해야 함.

리스코프 치환 원칙을 지키기 위해선 가급적 부모 객체의 일반 메소드를 그 의도와 다르게 오버라이딩 하지 않는 것이 중요.

부모 객체의 오버라이딩은 주로 동일한 메소드를 자식 객체만의 동작을 추가하기 위해 한다는 걸 감안하면 매우 준수하기 까다로운 원칙.

---

### 4. 인터페이스 분리 원칙 - **Interface Segregation Principle - ISP**

> "클라이언트는 자신이 사용하지 않는 메소드에 의존 관계를 맺으면 안 된다."

- 로버트 C 마틴

예시)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2e8b9138-67f2-4a71-97d8-f9dfefb27131/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4c6550d6-b9c7-4e3d-826f-738ddf0ea12a/Untitled.png)

SRP를 지키기 위해 남자 클래스를 단일 책임을 갖는 클래스로 나누었지만 너무 많은 클래스 구현이 필요해짐.

따라서 다양한 역할을 인터페이스로 만들고 남자라는 클래스는 각 인터페이스를 구현한 클래스로 지정

```java
import java.io.*;
import java.util.*;

class 남자 implements 남자친구, 사원, 소대원, 아들 {
    public void 기념일챙기기() {
        System.out.println("기념일 챙기기");
    }

    public void 키스하기() {
        System.out.println("키스하기");
    }

    public void 효도하기() {
        System.out.println("효도하기");
    }

    public void 안마하기() {
        System.out.println("안마하기");
    }

    public void 출근하기() {
        System.out.println("출근하기");
    }

    public void 아부하기() {
        System.out.println("아부하기");
    }

    public void 사격하기() {
        System.out.println("사격하기");
    }

    public void 구보하기() {
        System.out.println("구보하기");
    }
}

interface 남자친구 {
    abstract void 기념일챙기기();
    abstract void 키스하기();
}

interface 아들 {
    public void 효도하기();
    public void 안마하기();
}

interface 사원 {
    public void 아부하기();
    public void 출근하기();
}

interface 소대원 {
    public void 사격하기();
    public void 구보하기();
}

public class Main {
    public static void main(String[] args) throws IOException {
        남자친구 홍길동 = new 남자();
        홍길동.기념일챙기기();
        ((아들) 홍길동).안마하기();
        ((소대원) 홍길동).사격하기();
    }
}
```

**빈약한 상위 클래스 vs 풍성한 상위 클래스**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f78d5985-c645-46ca-9b15-83ec5924b20c/Untitled.png)

상위클래스가 풍성할 수록 캐스팅(Casting)이 적게 일어나서 소스코드가 깔끔해지기 때문에 상위클래스가 풍성한 것이 좋음.

---

### 5. 의존 역전 원칙 - **Dependency Inversion Principle - DIP**

> "고차원 모듈은 저차원 모듈에 의존하면 안 된다. 이 두 모듈 모두 다른 추상화된 것에 의존해야 한다."
> "추상화된 것은 구체적인 것에 의존하면 안된다. 구체적인 것이 추상화된 것에 의존해야 한다.
> "자주 변경되는 구체(Concrete) 클래스에 의존하면 안된다."

- 로버트 C 마틴"

- 의미
  
  - 자신보다 변하기 쉬운 것에 의존하지 말 것

추상클래스 또는 상위클래스는 구체적인 구현클래스 또는 하위클래스에게 의존하면 안됨.

왜냐면 구체적인 클래스는 코딩에 있어서 가장 전면적으로 노출되고 사용되기 때문에 변화에 민감.

만약 DIP(의존 역전 원칙)에 의해서 설계하지 않는다면, 구체화된 클래스가 수정될 때마다 상위클래스나 추상클래스가 변화 해야 하는데 또 그 상위 또 그 상위 계속 연관 되어 있는 클래스들이 수정되어야 함.

따라서 **하위클래스나 구체클래스에게 의존하면 안됨.**

DIP를 구현하는 방법이 스프링에서 사용되는 Dependency Injection - DI

예시)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/009d44af-fc5b-4826-810a-a5a0b6e0bf3c/Untitled.png)

자동차는 스노우 타이어에 의존하고 있음.

눈이 올 때는 스노우 타이어를 장착하지만 눈이 오지 않는다면? 타이어 변경이 필요한데 이는 번거롭고 귀찮은 작업.

해당 의존 관계를 `타이어` 인터페이스를 사용하여 역전

구체적인 `스노우 타이어`에 의존하던 것을 추상적인 `타이어`에 의존하는 것으로 변경

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8bd91642-30c6-42de-9dd4-1f72f3c03893/Untitled.png)

`상위클래스` 일 수록, `인터페이스`일 수록, `추상 클래스`일 수록 변하지 않을 가능성이 크기 때문에 번거로운 교체 작업을 해줄 필요가 없음

---

# 정리 - 복습용

### **1. Single Responsibility Principle 단일 책임의 원칙**

비교적 간단한 원칙이다. 말 그대로 **하나의 클래스는 하나의 책임만을 수행하게 하자**는 뜻이다.

객체 지향이 절차 지향과 다른 점은 class를 가지고 객체를 생성할 수 있다는 뜻인데, 가끔 객체 지향 언어로 코드를 짜는 사람 중에서는 이러한 객체 지향의 장점을 적극 활용하지 않고 하나의 클래스에 모든 기능을 넣는 사람이 있다.

물론 메소드를 구분하여 기능을 분류할 수 있지만 엄연히 다른 일을 수행하는 객체의 경우 class를 구분하는 것이 더 맞는 방식이다.

만약 class를 책임 별로 구분하지 않는다면 하나의 class가 수행하는 일이 거대해져 객체 지향 프로그래밍의 의미를 잃게 된다.

따라서 단일 책임의 원칙 (Single Responsiblity Principle) 에서는 **클래스가 제공하는 모든 서비스는 하나의 책임을 수행하는 데 집중되어 있어야 한다**고 말하고 있다. 1번 원칙인 만큼 **단일 책임의 원칙은 나머지 2~5번 원칙의 기초가 되는 원칙**이다.

---

### **2. Open Close Principle 개방 폐쇄 원칙**

컴포넌트, 클래스, 모듈, 함수와 같은 **소프트웨어 구성요소는 확장에는 열려있고, 변경에는 닫혀있어야 한다는 원칙**이다.

Java 언어를 배운 사람들은 쉽게 이해할 텐데, 상속을 받아서 하위 클래스에서 overriding 등을 하는 것은 가능하지만, 외부 class에서 접근해서 특정 field를 바꾸는 것을 제한하기 위해서 접근 제한자(private, protected 등)를 사용한다.

즉 해당 class뿐 아니라 이외 소프트웨어의 구성요소를 확장하여 사용할 때는 open 되어 있는 반면, 해당 구성요소를 외부에서 임의로 변경하려는 시도는 제한하여 그 경우에는 closed 되어 있어야 한다는 원칙이다.

개방 폐쇄 원칙은 협업 개발 시 매우 중요하게 생각해보아야 할 원리로, 내가 개발한 구성요소가 다른 사람에게 적절한 때 개방되고 폐쇄되는지에 대해 신중히 고민해보아야 한다.

---

### **3. Liskov Substitution Principle 리스코프 치환의 원칙**

**상속받은 하위 클래스는 어디서나 상위 클래스로 교체할 수 있어야 한다는 원칙**이다.

리스코프 치환의 원칙은 ***예시***로 이해하는 것이 가장 빠른 것 같다. 다음은 리스코프 치환의 원칙에 위배되는 예시이다.

만약 '도형'이라는 상위 class가 있다고 가정해보자. 그리고 '도형'이라는 class에 '꼭짓점의 개수는 ~개이다'라는 것을 나타내주는 method가 있다고 가정해보자.

그리고 '도형'이라는 상위 class를 상속받아 '사각형'이라는 하위클래스와 '원'이라는 하위클래스를 만들어주었다.

사각형이라는 하위 클래스는 꼭짓점을 4개 가지고 있으니 상위클래스인 도형으로 교체가 가능하다.

하지만 '원'이라는 하위클래스는 상위클래스인 도형이 가지고 있는 메서드를 충족시킬 수 없으므로 리스코프 치환의 원칙에 위배된다.

리스코프 치환의 원칙에 위배되지 않게끔 클래스를 설계하려면 '꼭짓점이 있는 도형'과 '꼭짓점이 없는 도형'의 상위클래스를 설계하고 꼭짓점이 있는 도형을 상속받아 삼각형, 사각형 등의 하위클래스를 만들고, 꼭짓점이 없는 도형을 상속받아 타원, 원 등의 하위클래스를 만들어야 할 것이다.

---

### **4. Interface Segregation Principle 인터페이스 분리의 원칙**

class와 달리 인터페이스는 다중 구현이 가능하다. Java interface를 생각해보면 implements라는 keyword 이후에 여러 interface가 오는 것을 종종 본 적이 있을 것이다.

물론 여러 interface를 구현해도 되지만, 인터페이스 분리의 원칙에서는 **한 클래스는 자신이 사용하지 않는 인터페이스는 구현하지 말아야 한다**고 말하고 있다.

즉, **클라이언트가 사용하지 않는 인터페이스 때문에 영향을 받아서는 안 된다**는 원칙이다.

가끔 만들어둔 모든 인터페이스를 모두 구현하여 필요한 것만 사용하는 경우가 있는데, 물론 편리하겠지만 사용하는 인터페이스만 구현하도록 노력해야 할 것이다.

---

### **5. Dependency Inversion Principle 의존성 역전의 원칙 (DIP)**

의존성 역전의 원칙은 **의존성 관계를 맺을 때 변화하기 쉬운 것보다는 변화가 없는 것에 의존관계를 맺어야 한다는 원칙**이다.

간단하게 DIP라고 부르기도 한다. 만약 어떠한 상점이 할인정책으로 fixed amount discount policy, 즉 모든 물건에 대해 정해진 양 ex) 2000원 할인을 실시했다고 치자.

![https://k.kakaocdn.net/dn/oOKdY/btrsfWqi2yw/Blwbq9LEuw57IjSMARkrAK/img.png](https://k.kakaocdn.net/dn/oOKdY/btrsfWqi2yw/Blwbq9LEuw57IjSMARkrAK/img.png)

의존성 역전의 원칙이 잘 지켜지지 않는 경우

discount policy로 fixed amount discount policy를 채택해서 위와 같은 diagram 형식의 class 구조가 되었지만, 사실 이는 5번 의존성 역전의 원칙을 잘 준수하지 않은 예시이다.

왜냐하면 만약 이후 상점이 마음이 바뀌어 할인정책으로 정량할인정책이 아닌, 정률할인정책을 사용한다면 단순히 fixed amount class를 바꾸어야 할 뿐만 아니라 store의 다른 영향을 받는 부분까지 모두 다 변경해야 하기 때문이다.

현재 store class는 변화가 있을 수 있는 fixed amount policy라는 class에 의존관계를 맺고 있기 때문에 의존성 역전의 원칙을 만족시키지 않는 것이다.

의존성 역전의 원칙을 잘 만족시키기 위해서는 변화가 없는 interface나 상위 클래스와 의존관계를 맺어야 한다. 위의 예시를 수정하면 아래와 같은 다이어그램이 될 것이다.

![https://k.kakaocdn.net/dn/crezQl/btrseRisdi1/slYDChUakwscUpdLlTEJ90/img.png](https://k.kakaocdn.net/dn/crezQl/btrseRisdi1/slYDChUakwscUpdLlTEJ90/img.png)

의존성 역전의 원칙이 잘 지켜지는 경우

즉 store는 변화가 잘 없는 discount policies라는 interface와 의존관계를 맺고 있으며, 이럴 경우 상점이 택하고 있는 할인정책이 변하더라도 store 자체 class는 큰 변경 없이 사용이 가능하다.

만약 두 가지 할인 정책 이외에 새로운 할인정책을 변경하고 싶다면 discount policies 를 구현하는 새로운 하위 클래스를 만들어 사용하면 되기 때문에 문제가 없다.

오히려 개발자의 입장에서는 변경이 용이해진 것이다.

의존성 역전의 원칙은 5가지 원칙 중 가장 이해하기가 까다로운 원칙이었을 것이다.

중요하지 않아 보일 수 있지만 이러한 의존성 역전의 원칙은 자바, 특히 이후 **Spring**에서 매우 중요하게 강조되는 개념이므로 잘 알아두면 유용할 것이다.
