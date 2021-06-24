using namespace std;

#include<vector>
#include<iostream>

void print_array (vector<int> array_to_print) {
    for (auto const& element : array_to_print) {
        cout << element << ' ';
    }
    cout << '\n';
};

vector<int> solution (vector<int> &A, int K) {
    int end_i = A.size() - 1;

    for (int k=0; k < K; k++) {
        int last = A[end_i];

        for (int i=end_i; i > 0; i--) {
            A[i] = A[i-1];
        }

        A[0] = last;
    }

    return A;
};

int main() {
    vector<int> vect{ 3, 8, 9, 7, 6 };
    int K = 3;
    vector<int> array_final = solution(vect, K);
    print_array(array_final);
};
