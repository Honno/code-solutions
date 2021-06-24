using namespace std;

#include<vector>
#include<map>
#include<iostream>

int solution (vector<int> &A) {
    map<int, bool> are_occurences_odd_map = {};

    for (auto const& element: A) {
        auto iter = are_occurences_odd_map.find(element);
        if (iter != are_occurences_odd_map.end()) {
            iter->second = !iter->second;
        } else {
            pair<int, bool> new_occurence(element, true);
            are_occurences_odd_map.insert(new_occurence);
        }
    }

    for (auto const& occurence : are_occurences_odd_map) {
        if (occurence.second) {
            return occurence.first;
        }
    }
};

int main() {
    vector<int> vect{ 1, 2, 3, 1, 3 };
    printf("%d", solution(vect));
}
