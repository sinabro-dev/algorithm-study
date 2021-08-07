package assignment01;

import java.io.*;

public class LEET_122_joonparkhere {

    public static int maxProfitVer1(int[] prices) {
        int sum = 0, idx = 0, low, high;
        while (idx < prices.length - 1) {
            while ((idx < prices.length - 1) && (prices[idx] >= prices[idx + 1]))
                idx++;
            low = prices[idx];

            while ((idx < prices.length - 1) && (prices[idx] <= prices[idx + 1]))
                idx++;
            high = prices[idx];

            sum += high - low;
        }
        return sum;
    }

    public static int maxProfitVer2(int[] prices) {
        int sum = 0;
        for (int idx = 0; idx < prices.length - 1; idx++) {
            if (prices[idx + 1] > prices[idx])
                sum += prices[idx + 1] - prices[idx];
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().split(",");
        int[] prices = new int[input.length];
        for (int i = 0; i < input.length; i++) {
            prices[i] = Integer.parseInt(input[i]);
        }

        int result = maxProfitVer2(prices);
        bw.append(String.valueOf(result));
        bw.flush();
        bw.close();
    }

}
