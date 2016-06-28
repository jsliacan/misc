#include <stdio.h>

/**
 * Problem 1
 *
 * IDEA:
 * If number divisible by 3 or 5, add to the sum.
 */
int main(){

  int sum = 0;
  for(int i=1; i<1000; i++){
    if((i%3==0) || (i%5==0))
      sum += i;
  }

  printf("%d\n", sum);
  return 0;
}
