#include "day1.c"

int main() {
  FILE *fp = fopen("small.txt", "r");

  char *testStr = NULL; 
  size_t num = 0;
  getline(&testStr, &num, fp);
  printf("%s\n", testStr);
  fixUpStr(testStr);
  printf("%s\n", testStr);
}
