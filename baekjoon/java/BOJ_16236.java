import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

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

public class BOJ_16236 {
	private static int[][] map;
	private static int[] shark;
	private static int time;
	private static boolean flag;
	private static int n;
	private static int sharkSize;
	private static int ateFishCnt;
//	private static int[][] dir;
	private static boolean[][] visited;
	
	
	private static void bfs() {
//		int[][] dir = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,0},{0,1},{1,-1},{1,0},{1,1}};
		int[][] dir = {{-1,0},{0,-1},{0,1},{1,0}};
		visited = new boolean[n][n];
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				visited[i][j]=false;
			}
		}
		visited[shark[0]][shark[1]]=true;
		Queue<rcd> queue = new LinkedList<>();
		queue.add(new rcd(shark[0], shark[1],0));
		int mind = Integer.MAX_VALUE;
		int nextR = Integer.MAX_VALUE;
		int nextC = Integer.MAX_VALUE;
		while (queue.size()>0) {
			rcd temprc = queue.remove();
			int r = temprc.r;
			int c = temprc.c;
			int d = temprc.d;
//			visited[r][c]=true;
			for (int[] temp: dir) {
				int nr = r+temp[0];
				int nc = c+temp[1];
				if (0>nr || nr>=n || 0>nc || nc>=n || map[nr][nc]>sharkSize) continue;
				if (visited[nr][nc]) continue;
				if (map[nr][nc]<sharkSize && map[nr][nc]!=0) {
//					time += d+Math.abs(temp[0])+Math.abs(temp[1]);
//					time += d+1;
//					shark[0] = nr;
//					shark[1] = nc;
//					ateFishCnt ++;
//					if (ateFishCnt==sharkSize) {
//						ateFishCnt=0;
//						sharkSize ++;
//					}
					if (mind>d+1) {
						mind = d+1;
						nextR = nr;
						nextC = nc;
						
					} else if (mind==d+1) {
						if (nextR>nr) {
							nextR = nr;
							nextC = nc;							
						} else if (nextR==nr) {
							if (nextC>nc) {
								nextR = nr;
								nextC = nc;	
							}							
						}
					}
//					map[nr][nc]=0;
//					System.out.printf("r: %d c: %d time: %d sharkSize: %d\n",r+temp[0], c+temp[1], time, sharkSize);
//					return;
				} else if (map[nr][nc]==0 || map[nr][nc]==sharkSize) {
					queue.add(new rcd(nr, nc, d+1));
					visited[nr][nc]=true;
				}
			}
			
			
			
		}
		if (mind!=Integer.MAX_VALUE) {
			time += mind;
			shark[0] = nextR;
			shark[1] = nextC;
			ateFishCnt ++;
			if (ateFishCnt==sharkSize) {
				ateFishCnt=0;
				sharkSize ++;
			}
			map[nextR][nextC]=0;
//			System.out.printf("r: %d c: %d time: %d sharkSize: %d\n",nextR, nextC, time, sharkSize);
			return;
		}
		flag=false;
		return;
		
	}

	public static void main(String[] args) {
		Scanner sc = new java.util.Scanner(System.in);
		n = sc.nextInt();
		map = new int[n][n];
		shark = new int[2];
		sharkSize = 2;
		time = 0;
		ateFishCnt=0;
		flag = true;
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				map[i][j] = sc.nextInt();
				if (map[i][j]==9) {
					shark[0] = i;
					shark[1] = j;
					map[i][j] = 0;
				}
			}
		}
		
		while (flag) {
			bfs();
//			move;
		}
		
		System.out.println(time);
		
	}
}
