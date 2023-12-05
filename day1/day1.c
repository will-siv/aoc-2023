#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int numfromchar(char c) {
  int ret = c - 48;
  if (ret / 10 != 0)
    return -1;
  return ret;
}

char strnumToChar(const char *str) {
  if (strcmp(str, "one") == 0)
    return '1';
  if (strcmp(str, "two") == 0)
    return '2';
  if (strcmp(str, "three") == 0)
    return '3';
  if (strcmp(str, "four") == 0)
    return '4';
  if (strcmp(str, "five") == 0)
    return '5';
  if (strcmp(str, "six") == 0)
    return '6';
  if (strcmp(str, "seven") == 0)
    return '7';
  if (strcmp(str, "eight") == 0)
    return '8';
  if (strcmp(str, "nine") == 0)
    return '9';
  return 0;
}

void replaceAndShift(char *str, int start, int length, char replace) {
        int ii = start;
        int shift = length - 2;
        str[ii] = replace;

        /* shift */
        while (str[ii] != 0) {
          ii++;
          str[ii] = str[ii + shift];
        }
}

void fixUpStr(char *str) {
  int maxRange = 6;
  int length, start;
  char copy[6];

  /* replace word in string with number
   * shift remaining letters to start
   */
  for ( start = 0; str[start] != 0; start++) {
    for (length = 3; length <= maxRange; length++) {
      char replace;
      
      strlcpy(copy, str + start, length);
      replace = strnumToChar(copy);
      if (replace) {
        replaceAndShift(str, start, length-1, replace);
      }
    }
  }
}

int main(int argc, char **argv) {
  FILE *in = fopen("input.txt", "r");
  FILE *out = fopen("out.txt", "w");
  char *line = NULL;
  size_t len = 0;
  int sum = 0;

  if (argc > 1) {
    fclose(in);
    in = fopen(argv[1], "r");
  }

  while (getline(&line, &len, in) != -1) {
    int firstNum = -1, secondNum = -1, n;
    int i;
    fprintf(out, "line: %s", line);
    fixUpStr(line);
    fprintf(out, "new line: %s", line);
    for (i = 0; i < len; i++) {
      int num = numfromchar(line[i]);
      if (line[i] == 0)
        break;
      if (num != -1) {
        if (firstNum == -1) {
          firstNum = num;
        }
        secondNum = num;
      }
    }
    n = (firstNum * 10) + secondNum;
    fprintf(out, "number from line: %d\n", n);
    fprintf(out, "%d + %d => ", sum, n);
    sum += n;
    fprintf(out, "%d\n\n", sum);
  }

  fclose(in);
  fclose(out);

  if (line)
    free(line);

  printf("%d\n", sum);
}
