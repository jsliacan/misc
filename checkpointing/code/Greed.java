
import java.util.List;
import java.util.ArrayList;

class Greed{
	
	public static void main(String[] args){
		
		int k = 10;		// number of checkpoints;
		int MAX_TIMES = 10*k;		// max number of checkpoint transpositions
		double[] Intervals = new double[k];	// there are up to k+1 intervals at any time, but we are only interested in times when there are k intervals
		List<double> maxIntervalLength = new ArrayList<double>();	// stores normalized max interval at every step
		
		// initialization 1
		for(int i = 0; i < k; i++){
			Intervals[i] = 1.0;
		}
		
		// initialization 2
		maxIntervalLength.add(1.0);
		
		
		// --------------------------------------  MAIN LOOP ------------------------------------- //
		for(int t = 0; t < MAX_TIMES; t++){
			
			int intervalsToMerge = 0;	// default merge 0th and 1st
			double optimalIk = 0;		// optimal length of kth interval
			double MIN = k;				// will store minimal maximum so far
			
			
			for(int i = 0; i < k-1; i++){	// for each pair of intervals that can be merged
				
				double[] newIntervals = new double[k];	// will store lengths of new intervals
				
				mergeIntervals(i, Intervals, newIntervals);	// will merge ith and (i+1)st interval and store all new intervals in newIntervals
				newIntervals[k-1] = optimalNewInterval(newIntervals, Intervals, MIN);	// compute kth interval;
				
				if(newIntervals[k-1] != -1){
					optimalIk = newIntervals[k-1];
					intervalsToMerge = i;
				}
				
			} // end for(i)
			
			// update intervals for the next loop
			for(int i = 0; i < k; i++){
				Intervals[i] = newIntervals[i]/(total(newIntervals))*k;
			}
			
			// save the max normalized interval length from this step
			maxIntervalLength.add(MIN);
			
		}	// end for(t)


		for(int i = 0; i < maxIntervalLength.size(); i++){
			System.out.println(maxIntervalLength.get(i));
		}

	}	// end main()
	
	
	
	
	/****************************************************************************
	*
	*								FUNCTIONS
	*
	*****************************************************************************/
	
	// MERGE TWO INTERVALS FROM ONE ARRAY AND PUT THE RESULTING INTERVALS IN THE OTHER ARRAY
	static void mergeIntervals(int indexOfMerge, double[] sourceArray, double[] destArray){
		
		for(int j = 0; j < indexOfMerge; j++){
			destArray[j] = sourceArray[j];
		}
				
		destArray[indexOfMerge] = sourceArray[indexOfMerge] + sourceArray[indexOfMerge+1];
				
		for(int j = indexOfMerge+1; j < k-1; j ++){
			destArray[j] = sourceArray[j+1];
		}
		
	}
	
	
	
	//	RETURN SMALLEST INDEX OF A MAXIMAL ENTRY IN AN ARRAY
	static int max(double[] array){	
		int maxx = 0; 
		for(int i = 0; i < array.length; i++){
			if(array[i] < array[maxx]) maxx = i;
		}
	}
	
	// RETURN SUM OF ENTRIES IN THE ARRAY
	static double total(double[] array){
		double sum = 0; 
		for(int i = 0; i < array.length; i++){
			sum = sum + array[i];
		}
	}
	
	
	
	//	COMPUTE THE APPROXIMATION OF OPTIMAL LENGTH OF THE NEW INTERVAL
	static double optimalNewInterval(double[] mergedIntervals, double[] Intervals, double normalizedMIN){
		
		double optimalLength = 0;
		double normalizedMax = k;		// normalized maximum for k intervals (at time T)
		
		for(int newInterval = 0; newInterval < 3; newInterval = newInterval + 0.1){
			
			double[] newints = new double[k];	// dummy array
			for(int i = 0; i < k-1; i++){
				newints[i] = mergedIntervals[i]/(k+i);	 	// notice that total(intervals) = k;
			}
			newints[k-1] = i/(k+i);
			
			double[] oldints = new double[k+1];
			for(int i = 0; i < k; i++){
				oldints[i] = Intervals[i]/(k+i);	 	// notice that total(intervals) = k;
			}
			oldints[k-1] = i/(k+i);
			
			int MAXk = newints[max(newints)];
			int MAXk1 = oldints[max(oldints)];
			
			if(normalizedMax > MAXk && normalizedMax > MAXk1){
				if(MAXk > MAXk1){
					normalizedMax = MAXk;
				}
				else{
					normalizedMax = MAXk1;
				}
				optimalLength = i;
			}
			
		}
		
		// Return -1 if this is not less than the min we had until now
		if(normalizedMIN > normalizedMax){
			normalizedMIN = normalizedMax;
			return optimalLength;
		}
		else{
			return -1;
		}
	}
}
