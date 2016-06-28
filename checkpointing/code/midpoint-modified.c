/**
 * MIDPOINT-MODIFIED.C
 * 
 * Algorithm:
 * 1. Initialize k intervals -- each to have length 1
 * 2. Find two consecutive intervals I_j, I_{j+1} such that I_j + I_{j+1} is the smallest
 * 		among all such pairs of intervals.
 * 3. Find two longest intervals. Let their lengths be M1 and M2.
 * 4. Merge I_j and I_{j+1}. 
 * 5. Add a new interval at the end (on the right). Its length is (M1 + M2)/2. 
 * 6. Normalize new set of intervals to have cumulative length k.
 * 7. Compute the measure of the longest interval among the new set of intervals. Call such interval I_{max}.
 * 		Then the measure is I_{max}*(k+1)/k
 * 8. Go to step 2 if have not been there more than N times.
 * 
 */

#include <stdio.h>
#include <stdlib.h>

/**************** FUNCTIN DECLARATIONS *****************/
void normalize(double* ints, int k);
double* findMinPair(double* ints, int k);
double* findMaxInterval(double* ints, int k, double* I);


/*******************	MAIN	*********************/
int main(){
  
  int k;	// number of checkpoints
  int N;	// number of iterations
  int i;	// used as index
  int iteration;	// keeps count of the iteration  -1 < iteration < N
  
  // get k, N from the user
  printf("k = ");
  scanf("%d", &k);
  printf("N = ");
  scanf("%d", &N);
  
  // create and initialize intervals
  double intervals[k];
  
  for(i = 0; i < k; i++){
	intervals[i] = 1.0;
  }
  
  /*
   * **************	ITERATE	****************
   */
  
  double *min_pair_addr;
  double max_int, max_int2;
  double *ptr, *max_int_ptr;
  double performance_record[k];
  
  for(iteration = 0; iteration < N; iteration++){
	
	min_pair_addr = findMinPair(intervals, k);	// address of the first of two intervals to be merged
	max_int_ptr = findMaxInterval(intervals, k, NULL);	// length of max interval
	max_int = *max_int_ptr;
	max_int2 = *findMaxInterval(intervals, k, max_int_ptr);	// length of the second max interval
	
	if(iteration >= N-k-1){		// save only the last k iterations (as those are the best -- needs proof, but wth)
	  performance_record[iteration - N + k + 1] = max_int*(k+1.0)/k;
	}
	
	// merge the two intervals
	*min_pair_addr = *min_pair_addr + *(min_pair_addr + 1);
	
	// shift the intervals to the right of the merged ones
	for(ptr = min_pair_addr+1; ptr < &intervals[k-1]; ptr++){
	  *ptr = *(ptr + 1);
	}
	
	// max_int is always greater or equal to max_int2
	if(max_int2 > *min_pair_addr){
	  intervals[k-1] = (max_int + max_int2)/2.0;	// min_pair_addr now contains the sum of two intervals so it's OK
	}
	else{
	  intervals[k-1] = (max_int + *min_pair_addr)/2.0;
	}
	
	// normalize the new intervals 
	normalize(intervals, k);
	
  }
  
  /*
   * ***************	RESULT	*****************
   */
  
  double performance_sup = *findMaxInterval(&performance_record[0], k, NULL);
  printf("\n%lf\n", performance_sup); 
  
  return 0;
  
}

/************ NORMALIZE **************
 * Take a vector, its total value, and normalize
 * the vector by the total value.
 */
void normalize(double* ints, int k){
  
  double* ptr = ints;	// dummy, for looping
  
  while(ptr < ints + k){
	*ptr = (*ptr)*k/(k + ints[k-1]);	// normalize entry
	ptr++;
  }
  
}

/************ FIND-MAX-INTERVAL **************
 * Find the address of the longest interval from 
 * among the current intervals, if it is not the interval I
 */
double* findMaxInterval(double* ints, int k, double* I){
  
  double* ptr;	// dummy, for looping
  double maxval = 0; 	// OK start value, since intervals are non-negative and we look for max
  double* max_int_ptr = ints;	// will hold the address of the max interval (not I)
  
  for(ptr = ints; ptr < ints + k; ptr++){
	
	if((ptr != I) && (maxval < *ptr)){	// check if the value is not a
	  maxval = *ptr;
	  max_int_ptr = ptr;
	}
	
  }
  return max_int_ptr;
}

/************ FIND-MIN-PAIR **************
 * Find the pair of intervals that have the greatest
 * cumulative length. Return the pointer to the first
 * of them. 
 */
double* findMinPair(double* ints, int k){
  
  double* current_addr = ints;
  double* next_addr = current_addr + 1;
  double current_value;
  double minval = k;
  double* minval_addr = ints;
  
  while(current_addr < ints + k - 1){
	
	current_value = (*current_addr) + (*next_addr);
	
	if(minval > current_value){
	  minval = current_value;
	  minval_addr = current_addr;
	}
	
	current_addr += 1;
	next_addr = next_addr + 1;
  }
  
  return minval_addr;
}
