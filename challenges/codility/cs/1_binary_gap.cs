using System;
using System.Collections;

class Solution {
    public int solution(int N) {
        byte[] bytes = BitConverter.GetBytes(N);
        BitArray bits = new BitArray(bytes);

        int largest_gap = 0;
        int gap = 0;
        bool counting = false;
        for (int i = 0; i < bits.Length; i++) {
            bool bit = bits[i];
            if (!bit && counting) {
                gap++;
            } else if (bit) {
                if (!counting) {
                    counting = true;
                } else {
                    if (gap > largest_gap) {
                        largest_gap = gap;
                    }
                    gap = 0;
                }
            }
        }

        return largest_gap;
    }
}
