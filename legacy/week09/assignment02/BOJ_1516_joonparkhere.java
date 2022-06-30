package assignment02;

import java.io.*;

public class BOJ_1516_joonparkhere {

    static int[][] conditions;
    static int[] costs;
    static int[] completions;

    public static void main(String[] args) throws IOException {
        input();
        solve();
    }

    static void input() throws IOException {
        int numOfElement = Integer.parseInt(br.readLine());
        conditions = new int[numOfElement + 1][];
        costs = new int[numOfElement + 1];

        for (int i = 1; i <= numOfElement; i++) {
            String[] strings = br.readLine().split(" ");
            costs[i] = Integer.parseInt(strings[0]);
            conditions[i] = new int[strings.length - 2];
            for (int j = 0; j < conditions[i].length; j++)
                conditions[i][j] = Integer.parseInt(strings[j + 1]);
        }
    }

    static void solve() throws IOException {
        completions = new int[costs.length];
        for (int building = 1; building < completions.length; building++) {
            int completion = completions[building];
            if (completion == 0)
                completion = build(building);
            bw.append(String.valueOf(completion)).append("\n");
        }
        bw.flush();
        bw.close();
    }

    static int build(int building) {
        int max = 0;
        for (int condition : conditions[building]) {
            int cur = completions[condition];
            if (cur == 0)
                cur = build(condition);
            if (cur > max)
                max = cur;
        }
        completions[building] = max + costs[building];
        return completions[building];
    }

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

}
