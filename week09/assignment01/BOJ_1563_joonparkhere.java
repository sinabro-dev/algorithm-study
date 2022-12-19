package assignment01;

import java.io.*;

public class BOJ_1563_joonparkhere {

    static final int MOD = 1000000;
    static int[][][] memo;  // [현재 일 수][지각 횟수][연속 결석 횟수]

    public static void main(String[] args) throws IOException {
        int days = Integer.parseInt(br.readLine());
        memo = new int[days+1][2][3];

        memoization(days);

        int result = 0;
        for (int lateness = 0; lateness < 2; lateness++)
            for (int absence = 0; absence < 3; absence++)
                result += memo[days][lateness][absence];
        result %= MOD;

        bw.append(String.valueOf(result));
        bw.flush();
        bw.close();
    }

    static void memoization(int day) {
        memo[1][0][0] = 1;
        memo[1][0][1] = 1;
        memo[1][1][0] = 1;

        for (int i = 2; i <= day; i++) {
            memo[i][0][0] = memo[i-1][0][0] + memo[i-1][0][1] + memo[i-1][0][2];
            memo[i][0][1] = memo[i-1][0][0];
            memo[i][0][2] = memo[i-1][0][1];
            memo[i][1][0] = memo[i-1][0][0] + memo[i-1][0][1] + memo[i-1][0][2] + memo[i-1][1][0] + memo[i-1][1][1] + memo[i-1][1][2];
            memo[i][1][1] = memo[i-1][1][0];
            memo[i][1][2] = memo[i-1][1][1];

            for (int lateness = 0; lateness < 2; lateness++)
                for (int absence = 0; absence < 3; absence++)
                    memo[i][lateness][absence] %= MOD;
        }
    }

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

}
