import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class swea14889 {
    static int N;
    static int minus = Integer.MAX_VALUE;
    static int[][] lst;
    static boolean[] visited;

    static void dfs(int depth, int idx) {
        if (minus==0) return;
        if (depth==N/2) {
            int startSum = 0;
            int linkSum = 0;

            for (int r=0;r<N-1;r++){
                for (int c=r+1;c<N;c++){
                    if (visited[r] && visited[c]){
                        startSum += lst[r][c];
                        startSum += lst[c][r];
                    } else if (!visited[r] && !visited[c]) {
                        linkSum += lst[r][c];
                        linkSum += lst[c][r];
                    }


                }

            }

            int val = Math.abs(startSum - linkSum);
            if (val == 0) {
                System.out.println(val);
                System.exit(0);
            }
            minus = Math.min(val, minus);

            return;
        }

        for (int i=idx;i<N;i++){
            if (!visited[i]){
                visited[i]=true;
                dfs(depth+1, i+1);
                visited[i]=false;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        lst = new int[N][N];
        visited = new boolean[N];


        for (int i=0;i<N;i++) {

            for (int j=0;j<N;j++) {
                lst[i][j] = sc.nextInt();
            }
        }

        dfs(0, 0);
        System.out.println(minus);
    }
}
