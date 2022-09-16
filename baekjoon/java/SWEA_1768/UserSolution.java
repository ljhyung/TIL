package SWEA_1768;

import java.util.LinkedList;
import java.util.List;

class UserSolution {
    public final static int N = 4;
    private static List<int[]> guessList;
    private static int[] visited;
    public void dfs(int depth, int[] start) {
        if (depth == 4) {
            guessList.add(start.clone());
            return;
        } else {
            for (int d = 0; d < 10; d++) {
                if (visited[d] == 1) continue;
                start[depth] = d;
                visited[d] = 1;
                dfs(depth+1, start);
                visited[d] = 0;
            }
        }
    }

    public void doUserImplementation(int guess[]) {
        // Implement a user's implementation function
        //
        // The array of guess[] is a return array that
        // is your guess for what digits[] would be.

        Solution s = new Solution();
        Solution.Result result = new Solution.Result();
        Solution.Result prvResult = new Solution.Result();
        visited = new int[10];
        int[] kill = new int[10];
        guessList = new LinkedList<>();
        dfs(0,new int[4]);
        for(int i=0;i<guessList.size();i++){
            for(int j=0;j<4;j++){
                if (kill[guessList.get(i)[j]]==1) continue;
            }

            for(int h=0;h<4;h++) guess[h] = guessList.get(i)[h];
            result = s.query(guess);

            int strike = result.strike;
            int ball = result.ball;
            if (strike==4){
                return;
            }
            if ((strike+ball)==0){
                for(int j=0;j<4;j++){
                    kill[guessList.get(i)[j]]=1;
                    continue;
                }
            }
            if (strike+ball==4){
                //순서 바꾸기
            }

            if (i==0){
                prvResult.strike = result.strike;
                prvResult.ball = result.ball;
                continue;
            }


            if (prvResult.strike< result.strike){       // 1. strike 늘었을 때
                if (prvResult.ball== result.ball){      // 1-1. 볼은 그대로인 상황

                } else if (prvResult.ball > result.ball) { // 1-2. 볼이 줄어든 상황

                }
            } else if (prvResult.strike> result.strike) {   // 2. strike 줄었을 때
                if (prvResult.ball< result.ball){           // 2-1. ball 늘었을 때

                } else if (prvResult.ball== result.ball) {  // 2-2. ball 그대로

                }
            }else {                                         // 3. strike 그대로
            if (prvResult.ball< result.ball){               // 3-1. ball 늘었을 때

                } else if (prvResult.ball > result.ball) {  // 3-2. ball 줄었을 때

                } else if (prvResult.ball== result.ball) {  // 3-3. ball 그대로일 때

                }
            }

            
        }

        //////////////////////////


//        Solution s = new Solution();
//        int [] number = new int[10];
//        int[] guessG = new int[4];
//        int[][] findNum = new int[4][2]; //결과를 찾앗을때
//        int guessCnt =1;
//        int findCnt=0;
//        int possibleCnt =10;
//        Solution.Result resultT = new Solution.Result();
//        Solution.Result result = new Solution.Result();
//        while(true) {
//            int count=0,i=0; //숫자 4개 들어갔나, i는 몇부터 시작해서 넣어야할지
//            while(count<4) {  //숫자를 추측한다
//                if(findNum[count][1]==1) {
//                    count++;
//                    continue;
//                }else if(number[i]==0)
//                    guessG[count++]= i;
//                if(i>=10) i=0;
//                else i++;
//            }
//            result = s.query(guessG);
//            if(result.ball==0&&result.strike==0){
//                for(int j=0;j<4;j++) {
//                    possibleCnt--;
//                    number[guessG[j]]=1;
//                }
//                continue;
//            }else {
//                for(int j=i;j<=9;j++) {
//                    for(int k=0;k<4;k++) {
//                        if(possibleCnt<=(4-findCnt)||findCnt==4||result.strike==4) { //조합 하거나 이미 찾았거나
//                            for(int h=0;h<4;h++) guess[h] = guessG[h];
//                            result  = s.query(guess);
//                            if(findCnt==4||result.strike==4) return; //스트라이크가 4개일 떄는 retrun;
//                            while(result.strike!=4) {//조합을 해야하는 경우
//                                int[] real = new int[4];
//                                for(int q=0;q<4;q++)real[q]=findNum[q][1];
//                                for(int t=0;t<3;t++) {
//                                    if(real[t]==1)continue;
//                                    for(int g =t+1;g<4;g++) {
//                                        if(real[g]!=1) {
//                                            swap(guess,t,g);
//                                            resultT = s.query(guess);
//                                            if(resultT.strike==4){ //찾앗을때
//                                                return;
//                                            }else if(resultT.strike==result.strike+2) { //2개증가
//                                                real[g]=real[t]=1;
//                                                break;
//                                            }else if(resultT.strike==result.strike-2) { //2개 감소
//                                                swap(guess,g,t);
//                                                real[g]=real[t]=1;
//                                                break;
//                                            }
//                                            swap(guess,g,t);
//                                        }
//                                    }
//                                }
//                                result  = s.query(guess);
//                            }
//                        }else if(findNum[k][1]!=1&&number[j]==0) {
//                            int temp = guessG[k];
//                            guessG[k]=j;
//                            resultT = s.query(guessG);
//                            if(resultT.strike>result.strike) { //strick만 늘어난다.
//                                if(resultT.ball==result.ball) {
//                                    number[temp]=1; // 가지치기
//                                    possibleCnt--;
//                                }
//                                findNum[k][1]=1;
//                                findNum[k][0]=j;
//                                number[j]=1; // 가지치기
//                                findCnt++;
//                                possibleCnt--;
//                                result.ball=resultT.ball;
//                                result.strike=resultT.strike;
//                                break;
//                            }else if((resultT.strike==result.strike&&resultT.ball==result.ball-1)) { //strick도 줄고 ,ball도 줄면
//                                number[j]=1; // 가지치기
//                                possibleCnt--;
//                                guessG[k]=temp; //원상 복구
//                                break;
//                            }else if(resultT.strike==result.strike-1){ //스트라이크 줄고, 볼만 올라간다.
//                                if(resultT.ball==result.ball) number[j]=1; // 가지치기
//                                findNum[k][1]=1;
//                                findNum[k][0]=temp;
//                                number[temp]=1; // 가지치기
//                                findCnt++;
//                                possibleCnt--;
//                                guessG[k]=temp; //원상 복구
//                                continue;
//                            }
//                            guessG[k]=temp; //원상 복구
//                        }
//                    }
//                }
//
//            }
//        }


    }
//    public void swap(int[] guess, int a,int b) {
//        int temp = guess[a];
//        guess[a]= guess[b];
//        guess[b] = temp;
//    }


}

