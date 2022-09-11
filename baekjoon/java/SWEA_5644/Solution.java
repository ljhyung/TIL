package SWEA_5644;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

class rc{
    int r;
    int c;
    public rc(int r, int c){
        this.r = r;
        this.c = c;
    }
}

public class Solution {
    private static int answer;
    private static int[][][] map;

    private static void mark(int r, int c, int d, int p, int n){
        for(int i=0;i<10;i++){
            for(int j=0;j<10;j++){
                if ((Math.abs(r-i)+Math.abs(c-j))<=d){
//                    for(int k=0;k<8;k++){
//                        if(map[i][j][k]==0){
//                            map[i][j][k] = p;
//                            break;
//                        }
//                    }
                    map[i][j][n] = p;
                }
            }
        }
    }

    public static int getIndexOf(int[] lst, int k){
        for(int i=0;i<lst.length;i++){
            if (lst[i]==k){
                return i;
            }
        }
        return -1;
    }

    private static void sol(rc nowA, rc nowB){
        int[] sortA = map[nowA.r][nowA.c].clone();
        Arrays.sort(sortA);
        int[] sortB = map[nowB.r][nowB.c].clone();
        Arrays.sort(sortB);

        if (getIndexOf(map[nowA.r][nowA.c],sortA[7])==
                getIndexOf(map[nowB.r][nowB.c],sortB[7])&&sortA[7]!=0&&sortB[7]!=0){
            if (sortA[6]==0&&sortB[6]==0){
//                System.out.println(answer + " " + sortA[7]);
                answer += sortA[7];
            } else {
//                System.out.println(answer + " " + sortA[7] + " " + Math.max(sortA[6], sortB[6]));
                answer += sortA[7] + Math.max(sortA[6], sortB[6]);
            }

        } else {
//            System.out.println(answer + " " + sortA[7] + " " + sortB[7]);
            answer += sortA[7] + sortB[7];
        }
    }
    public static void main(String[] args) throws FileNotFoundException {
        System.setIn(new FileInputStream("src/SWEA_5644/sample_input.txt"));
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        int[][] dir = {{0,0},{1,0},{0,1},{-1,0},{0,-1}};
        for(int tc=1;tc<=T;tc++){
            answer=0;
            map = new int[10][10][8];
            int M = sc.nextInt();
            int A = sc.nextInt();
            int[] userA = new int[M];
            int[] userB = new int[M];
            rc nowA = new rc(9,0);
            rc nowB = new rc(0,9);
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
                mark(10-c,r-1,d,p,i);
            }
            sol(nowA, nowB);
            for(int i=0;i<M;i++){
                nowA.r += dir[userA[i]][0];
                nowA.c += dir[userA[i]][1];
                nowB.r += dir[userB[i]][0];
                nowB.c += dir[userB[i]][1];
                sol(nowA, nowB);
            }
            System.out.println("#" + tc + " " + answer);
        }
    }
}
