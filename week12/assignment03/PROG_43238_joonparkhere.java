package assignment03;

import java.util.*;

public class PROG_43238_joonparkhere {

    public long solution(int n, int[] times) {
        Arrays.sort(times);

        long left = 1;
        long right = (long) n * times[times.length - 1];

        long answer = right;
        while (left <= right) {
            long mid = (left + right) / 2;

            long count = 0;
            for (int time : times) {
                count += mid / time;
            }

            if (count < n) {
                left = mid + 1;
            } else {
                right = mid - 1;
                answer = Math.min(mid, answer);
            }
        }

        return answer;
    }

}
