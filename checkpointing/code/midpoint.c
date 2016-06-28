/**
 * MIDPOINT.C
 * 
 * Algorithm:
 * 1. Initialize k intervals -- each to have length 1
 * 2. Find two consecutive intervals I_j, I_{j+1} such that I_j + I_{j+1} is the smallest
 * 		among all such pairs of intervals.
 * 3. Find interval of maximum length. Let its length be M.
 * 4. Merge I_j and I_{j+1}. 
 * 5. Add a new interval at the end (on the right). Its length is (I_j + I_{j+1} + M)/2. Here
 * 		we mean I_j, I_{j+1} before their merging.
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
double findMaxInterval(double* ints, int k);


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
  double max_int;
  double *ptr;
  double performance_record[k];
  
  for(iteration = 0; iteration < N; iteration++){
	
	min_pair_addr = findMinPair(intervals, k);	// address of the first of two intervals to be merged
	max_int = findMaxInterval(intervals, k);	// length of max interval

	
	if(iteration >= N-k-1){		// save only the last k iterations (as those are the best -- needs proof, but wth)
	  performance_record[iteration - N + k + 1] = max_int*(k+1.0)/k;
	}
	
	// merge the two intervals
	*min_pair_addr = *min_pair_addr + *(min_pair_addr + 1);
	
	// shift the intervals to the right of the merged ones
	for(ptr = min_pair_addr+1; ptr < &intervals[k-1]; ptr++){
	  *ptr = *(ptr + 1);
	}
	
	// write the new interval
	intervals[k-1] = (*min_pair_addr + max_int)/2.0;	// min_pair_addr now contains the sum of two intervals so it's OK
	
	// normalize the new intervals 
	normalize(intervals, k);
	
  }
  
  /*
   * ***************	RESULT	*****************
   */
  
  double performance_sup = findMaxInterval(&performance_record[0], k);
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
 * among the current intervals.
 */
double findMaxInterval(double* ints, int k){
  
  double* ptr;	// dummy, for looping
  double maxval = 0; 	// OK start value, since intervals are non-negative and we look for max
  
  for(ptr = ints; ptr < ints + k; ptr++){
	
	if(maxval < *ptr){
	  maxval = *ptr;
	}
	
  }
  return maxval;
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
