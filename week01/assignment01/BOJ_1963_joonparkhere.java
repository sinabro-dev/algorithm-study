package assignment01;

import java.io.*;
import java.util.*;

public class BOJ_1963_joonparkhere {

    private static final int MAX_NUMBER = 9999;
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final boolean[] isPrime = new boolean[MAX_NUMBER + 1];

    public static void main(String[] args) throws IOException {
        findPrime();
        solve();
    }

    private static void findPrime() {
        Arrays.fill(isPrime, true);

        for (int i = 2; i <= MAX_NUMBER; i++) {
            if (!isPrime[i]) {
                continue;
            }
            for (int j = i*2; j <= MAX_NUMBER; j += i) {
                isPrime[j] = false;
            }
        }
    }

    private static void solve() throws IOException {
        int numOfCase = Integer.parseInt(br.readLine());

        for (int i = 0; i < numOfCase; i++) {
            String[] input = br.readLine().split(" ");
            int start = Integer.parseInt(input[0]);
            int target = Integer.parseInt(input[1]);

            int answer = findAnswer(start, target);
            if (answer == -1) {
                bw.append("Impossible");
            } else {
                bw.append(String.valueOf(answer));
            }
            bw.newLine();
        }

        bw.flush();
        bw.close();
    }

    private static int findAnswer(int start, int target) {
        Queue<Integer> queue = new LinkedList<>();
        boolean[] isVisit = new boolean[MAX_NUMBER + 1];
        int[] counts = new int[MAX_NUMBER + 1];

        queue.add(start);
        isVisit[start] = true;
        counts[start] = 1;

        while (!queue.isEmpty()) {
            Integer current = queue.remove();
            if (current == target) {
                break;
            }

            List<Integer> nextList = findNext(current);
            for (Integer next : nextList) {
                if (isVisit[next]) {
                    continue;
                }
                queue.add(next);
                isVisit[next] = true;
                counts[next] = counts[current] + 1;
            }
        }

        return counts[target] == 0 ? -1 : counts[target] - 1;
    }

    private static List<Integer> findNext(int number) {
        List<Integer> nextList = new ArrayList<>();

        for (int i = 3; i >= 0; i--) {
            int currentDigit = (int) Math.pow(10, i);
            int nextDigit = 10 * currentDigit;

            for (int j = 1; j <= 9; j++) {
                int prefix = (number / nextDigit) * nextDigit;
                int value = (number + j * currentDigit) % nextDigit;

                int temp = prefix + value;
                if (temp >= 1000 && isPrime[temp]) {
                    nextList.add(temp);
                }
            }
        }

        return nextList;
    }

}
