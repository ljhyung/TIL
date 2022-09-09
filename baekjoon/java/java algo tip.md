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




















