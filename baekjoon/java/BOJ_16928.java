import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class BOJ_16928 {
    private static int N, M;
    private static int[] board;
    private static int[] visit;
    private static Queue<Integer> queue;

    private static void bfs(){
        queue = new LinkedList<Integer>();
        queue.add(1);
//        visit[1] = 1;
        while (queue.size()!=0){
            int now = queue.remove();
            if (now==100){
                System.out.println(visit[100]);
//                System.out.println(Arrays.toString(visit));
                return;
            }

            for(int dice=1;dice<7;dice++){
                int next = now + dice;
                if (next>100) continue;
//                if (board[next]<now) continue;
                if (visit[board[next]]!=0) continue;
                queue.add(board[next]);
                visit[board[next]] = visit[now]+1;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] tokens = br.readLine().split(" ");
        N = Integer.parseInt(tokens[0]);
        M = Integer.parseInt(tokens[1]);
        board = new int[101];
        visit = new int[101];
        for (int i=0;i<101;i++) board[i] = i;
        for (int i=0;i<101;i++) visit[i] = 0;
        for (int i=0;i<N;i++){
            tokens = br.readLine().split(" ");
            board[Integer.parseInt(tokens[0])] = Integer.parseInt(tokens[1]);
        }
        for (int i=0;i<M;i++){
            tokens = br.readLine().split(" ");
            board[Integer.parseInt(tokens[0])] = Integer.parseInt(tokens[1]);
        }
        bfs();
//        System.out.print(Arrays.toString(board));
    }
}
