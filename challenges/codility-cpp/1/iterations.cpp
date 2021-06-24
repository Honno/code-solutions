#include <iostream>
#include <bitset>

class Solution {
public:
    int solution(int N) {
        int largest_gap = 0;
        std::string bitstring = std::bitset<32>(N).to_string();
        int gap_counter = 0;
        bool is_counting = false;
        for(char& c : bitstring) {
            if((c == '0') && is_counting) {
                gap_counter++;
            } else if(c == '1') {
                if(!is_counting) {
                    is_counting = true;
                } else {
                    if(gap_counter > 0) {
                        if(gap_counter > largest_gap) {
                            largest_gap = gap_counter;
                        };
                    };
                    gap_counter = 0;
                };
            };
        };

        return largest_gap;
    };
};

int main() {
    int N;
    std::cin >> N;

    Solution s;
    printf("%d", s.solution(N));
};
