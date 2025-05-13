#include <iostream>

#include "Calculate1.hpp"

int main() {
  Calculate1 calc;
  int ans = calc.Add(1, 2);
  std::cout << "ans=" << ans << std::endl;

  return 0;
}
