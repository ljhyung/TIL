package SWEA_5644;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

class rc{
    int r;
    int c;
    public rc(int r, int c){
        this.r = r;
        this.c = c;
    }
}

public class Main {
    private static int answer;
    private static int[][][] map;

    private static void mark(int r, int c, int d, int p){
        for(int i=0;i<10;i++){
            for(int j=0;j<10;j++){
                if ((Math.abs(r-i)+Math.abs(c-j))<=d){
                    for(int k=0;k<8;k++){
                        if(map[i][j][k]==0){
                            map[i][j][k] = p;
                            continue;
                        }
                    }
                }
            }
        }
    }
    public static void main(String[] args) throws FileNotFoundException {
        System.setIn(new FileInputStream("src/SWEA_5644/sample_input.txt"));
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        int[][] dir = {{1,0},{0,1},{-1,0},{0,-1}};
        for(int tc=1;tc<=T;tc++){
            map = new int[10][10][8];
            int M = sc.nextInt();
            int A = sc.nextInt();
            int[] userA = new int[M];
            int[] userB = new int[M];
            rc nowA = new rc(0,0);
            rc nowB = new rc(9,9);
            for(int i=0;i<M;i++){
                userA[i] = sc.nextInt();
            }
            for(int i=0;i<M;i++){
                userB[i] = sc.nextInt();
            }
            for(int i=0;i<A;i++){
                int r = sc.nextInt();
                int c = sc.nextInt();
                int d = sc.nextInt();
                int p = sc.nextInt();
                mark(r,c,d,p);
            }
            for(int i=0;i<M;i++){
                
            }
            System.out.println("#" + tc + " " + answer);
        }
    }
}
