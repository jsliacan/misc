#include <stdio.h>


/**
 * Problem 2
 *
 * IDEA:
 * Start with Fa=1, Fb=2. Whenever Fb even, add it to the sum and
 * continue computing next Fb.
 */


int main(){

  long int evensum = 0;
  int a = 1;
  int b = 2;
  int c;
  
  while(b<4000000){
    
    if(b%2==0)
      evensum += b;

    c = b;
    b = a+b;
    a = c;
    
  }

  printf("\n\n%ld\n\n", evensum);
  
  return 0;
}
