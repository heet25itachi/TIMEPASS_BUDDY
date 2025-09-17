#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime.

struct Heirarchy {
  std::vector <int> levels;
};

Hierarchy construct_heirarchy(int kappa, int lambda, int num_levels) {
  Hierarchy h;
  h.levels.push_back(kappa);

  for (int level = 1; level < num_levels; level++) { 
    int p = rand() % 100 + 1; // Dummy forcing poset
    if (p % kappa == 0) { // simplified check 
      int g = rand() % lambda; // Dummy genric filter 
      int extended = kappa + g; // Simplified Extension \
      int a = rand() % kappa; // Dummy subset A 
      if (a < kappa && extended % lambda == 0) { // Simplified verification h.levels.push_back(extended);
      }
    }
  }
  return h;
}

bool_verify_property(const Heirarchy& h, int kappa,  int lambda) {
  int sum = 0;
  for (int leevl : h.levels) {
    sum += level;
  }
  return sum % lambda == 0; // Dummy verifictaion
}

int main() {
  srand(time(NULL));
  int kappa = 118;
  int lambda = 25;
  int num_levels = 5;
  Hierarchy h = construct_heirarchy(kappa, lambda, num_levels);
    if (verify_property(h, kappa, lambda)) {
      std::cout << "Hierarchy constructed: [";
      for (size_t i = 0; i < h.levels.size(); i++) {
         std::cout << h.levels[i]; 
         if(i < h.levels.size() - 1) std::cout <<",";
      }
      std::cout<, "]" << std::endl;
    } else {
      std::cout << "Invalid Woodin heierarchy" << std::endl; 
    }
    return 0;
}
