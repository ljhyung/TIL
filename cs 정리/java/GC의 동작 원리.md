# GC

## 정의

Garbage Collection은 JVM이 더 이상 사용되지 않는 object들을 메모리에서 제거하는 기능.

Heap 영역의 object 중 stack에서 도달이 불가능한 (Unreachable, Unreferenced) object 들이 gc의 대상.

## 구조

![Slide5.PNG](assets/a0f5d885c742af5bd9a70a2423a5b5cfd4b8c8bf.PNG)

## 동작 방식

1단계 : STW(Stop the world)

- JVM이 GC를 실행하기 위해서 애플리케이션의 실행을 멈추는 작업이다.

- GC를 실행하는 Thread 외 다른 모든 Thread는 작업이 중단된다.

- 최소화해야한다.

2단계 : Mark and Sweep

- stw 이후, GC가 stack의 모든 변수 또는 접근 가능한 Reachable 객체를 스캔해서 사용되는 메모리는 Mark하고 그렇지 못한 메모리를 제거하는 과정이 Sweep

![gc.png](assets/350c469a227f7698db300b74cf83ffb83288ff34.png)

## 프로세스

1. 새로운 object는 Eden 영역에 할당되고 두개의 Survivor Space는 비워진 상태에서 시작한다.

2. Eden 영역이 가득차면, MinorGC가 발생한다.

3. MinorGC 가 발생하면, Reachable 오브젝트들은 S0 으로 옮겨진다. Unreachable 오브젝트들은 Eden 영역이 클리어 될때 함께 메모리에서 사라진다.

4. 다음 MinorGC 가 발생할때, Eden 영역에는 3번과 같은 과정이 발생한다. Unreachable 오브젝트들은 지워지고, Reachable 오브젝트들은 Survivor Space 로 이동한다. 기존에 S0 에 있었던 Reachable 오브젝트들은 S1 으로 옮겨지는데, 이때, age 값이 증가되어 옮겨진다. 살아남은 모든 오브젝트들이 S1 으로 모두 옮겨지면, S0 와 Eden 은 클리어 된다. Survivor Space 에서 Survivor Space 로의 이동은 이동할때마다 age 값이 증가한다.

5. 다음 MinorGC 가 발생하면, 4번 과정이 반복되는데, S1 이 가득차 있었으므로 S1 에서 살아남은 오브젝트들은 S0 로 옮겨지면서 Eden 과 S1 은 클리어 된다. 이때에도, age 값이 증가되어 옮겨진다. Survivor Space 에서 Survivor Space 로의 이동은 이동할때마다 age 값이 증가한다.

6. Young Generation 에서 계속해서 살아남으며 age 값이 증가하는 오브젝트들은 age 값이 특정값 이상이 되면 Old Generation 으로 옮겨지는데 이 단계를 Promotion 이라고 한다.

7. MinorGC 가 계속해서 반복되면, Promotion 작업도 꾸준히 발생하게 된다.

8. Promotion 작업이 계속해서 반복되면서 Old Generation 이 가득차게 되면 MajorGC 가 발생하게 된다.

## 다양한 종류의 GC 알고리즘

[](https://mangkyu.tistory.com/m/119)

참조 링크

[](https://www.oracle.com/webfolder/technetwork/tutorials/obe/java/gc01/index.html)[Java Garbage Collection Basics](https://www.oracle.com/webfolder/technetwork/tutorials/obe/java/gc01/index.html)

[](https://d2.naver.com/helloworld/1329)[NAVER D2](https://d2.naver.com/helloworld/1329)

[](https://yaboong.github.io/java/2018/06/09/java-garbage-collection/)[자바 메모리 관리 - 가비지 컬렉션](https://yaboong.github.io/java/2018/06/09/java-garbage-collection/)

[](https://whitepro.tistory.com/m/462)[[자바 기초] 3. 자바의 동작원리 : Garbage Collection](https://whitepro.tistory.com/m/462)

## 면접용 질문

## 추가

### MinorGC, MajorGC

![ObjectLifetime.gif](assets/a5dcd4ea552479a9a4374ea3558ddda4f4b939d9.gif)

young 영역을

stw 시 eden 영역과 survivor 영역을 동시 mark and sweep?
