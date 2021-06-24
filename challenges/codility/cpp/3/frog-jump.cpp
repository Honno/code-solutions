#include<iostream>
#include<cmath>

int solution(int X, int Y, int D) {
  double jumps = ((double)Y - (double)X) / (double)D;
  return ceil(jumps);
};

int main() {
  printf("%d", solution(30, 110, 30));
}
