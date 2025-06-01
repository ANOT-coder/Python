#include <iostream>
using namespace std;
void myFunction(int num) {
    num = 10; // Changes only the local copy
  }
  int main() {
    int x = 5;
    myFunction(x);
    cout << x << endl; // Output: 5 (original x unchanged)
    return 0;
  }