java 알고 팁

1. class 이름 Main으로

2. main 함수

```java
public static void main(String[] args) {
```

3. 입력
   
   ```java
   Scanner sc = new Scanner(System.in);
   int[] lst = new int[9];
   lst[i] = sc.nextInt();
   ///////////////////////////////////
   BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
   String[] tokens = br.readLine().split(" ");
   N = Integer.parseInt(tokens[0]);
   M = Integer.parseInt(tokens[1]);
   ///////////////////////////////////
   BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
   StringTokenizer st = new StringTokenizer(br.readLine());
   int n = Integer.parseInt(st.nextToken());
   int m = Integer.parseInt(st.nextToken());
   ```

4. 큐
   
   ```java
   //전역 선
   private static Queue<Integer> queue;
   queue = new LinkedList<Integer>();
   ```

5. 큐에 list나 좌표를 넣고 싶을 때
   
   ```java
   class rcd {
       int r;
       int c;
       int d;
       public rcd(int r, int c,int d) {
           this.r = r;
           this.c = c;
           this.d = d;
       }
   }
   ```
   
   클래스 형식으로 만들어서 
   
   ```java
   Queue<rcd> queue = new LinkedList<>();
   queue.add(new rcd(shark[0], shark[1],0));
   ```





9/17 시험

퍼즐 맞추기 1234 5678

                      9876



가장 많은 면, 가장 위, 가장 왼쪽
