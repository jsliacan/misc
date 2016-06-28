/**
 *
 * Backtrack Turan number of a 3-graph P3: (1 2 (3) 4 (5) 6 7).
 * Interested in n = 10, 11, 12.
 *
 * [CURRENT WORKING VERSION]
 *
 * Set N = 10, 11, 12 to run the cases.
 *
 */


#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 7
#define E (N*(N-1)*(N-2)/6)
#define MAX_COUNT ((N-1)*(N-2)/2)

int edges[E][4]; // edge = [0111000000,0100000000,0010000000,0001000000]
int current_max = 0; 
int counter = 0;

void bug(int bugid){
  printf("bugs around: %d\n", bugid);
  exit(1);
}

void printarr(int* arr, int n){
  for(int i=0; i<n; i++){
    printf("%d ", arr[i]);
  }
  printf("\n");
}


void printedge(int edge){
  
  int k = edges[edge][0];

  for(int i=N-1; i >=0; i--){
    (k&(1<<i)) ? putchar('1') : putchar('0');
  }
  printf("\n");
}

/*
int bitsum(int k){
  int sum = 0;
  for(int i=0; i < sizeof(int)*8; i++){
    if(k&(1<<i)) sum++;
  }
  return sum;
}
*/

void genedges(){
  /*
   * Generate edges, i.e. all N-bit sequences with 3 bits ON and N-3 bits OFF.
   */

  int ebasis[N];
  for(int i=0; i<N; i++){
    ebasis[i] = 1<<i;
  }

  int edge = 0;
  for(int i=0; i<N-2;i++){
    for(int j=i+1; j<N-1; j++){
      for(int k=j+1; k<N; k++){
	edges[edge][0] = ebasis[i] + ebasis[j] + ebasis[k];
	edges[edge][1] = ebasis[i];
	edges[edge][2] = ebasis[j];
	edges[edge][3] = ebasis[k];
	edge++;
      }
    }
  }
}



int edge_overlap(int e1, int e2){
  /*
   * RETURN: 
   *  1  if e1 and e2 overlap on exactly 1 vertex. 
   * -1  if they overlap on more than 1 vertex. 
   *  0  otherwise.
   *
   * INPUT:
   * e1 - index of the first edge
   * e2 - index of the second edge
   */

  int overlap = 0;

  for(int i=1; i<4; i++){
    for(int j=i; j<4; j++){
      if(edges[e1][i] & edges[e2][j]){ // if these two vertices are the same

	if(overlap == 0){ // if there has been no other overlapping vertex
	  overlap = 1;
	}
	else if(overlap > 0){ // if there already is overlapping vertex
	  overlap = -1;
	}
      }
    }
  }

  return overlap;
}



int can_add(int *graph, int *fe, int newedge){

  /*
   * RETURN:
   *  1  if newedge can be added to graph keeping it P3-free.
   *  0  otherwise.
   *
   * INPUT:
   * graph    - list of edge
   * newedge  - edge to be added
   */

  for(int i=0; i<E-1; i++){
    for(int j=i+1; j<E; j++){

      if((i!=newedge) && (j!=newedge)){
	if(((graph[i]==1) || (graph[j]==1)) && (graph[i] != -1) && (graph[j] != -1)){
	  if((edge_overlap(i,j) == 0) && (edge_overlap(i,newedge)==1) && edge_overlap(j,newedge)==1){
	    if(graph[i]==1 && graph[j]==1){
	      return 0;
	    }
	    else if(graph[i]==1 && graph[j]==0){
	      graph[j] = -1;
	      (*fe)++;
	    }
	    else{
	      graph[i] = -1;
	      (*fe)++;
	    }
	    /*
	    else if(graph[i]==0 && graph[j]==1){
	      toforbid[i] = 1;
	    }
	    else{
	      bug(991);
	    }
	    */
	  }
	  else if((edge_overlap(j, newedge) == 0) && (edge_overlap(i,j)==1) && edge_overlap(i,newedge)==1){
	    if(graph[i]==1 && graph[j]==1){
	      return 0;
	    }
	    else if(graph[i]==1 && graph[j]==0){
	      graph[j] = -1;
	      (*fe)++;
	    }
	    else{
	      graph[i] = -1;
	      (*fe)++;
	    }
	    /*
	    else if(graph[i]==0 && graph[j]==1){
	      toforbid[i] = 1;
	    }
	    else{
	      bug(992);
	    }
	    */
	  }
	  else if((edge_overlap(i, newedge) == 0) && (edge_overlap(j,i)==1) && edge_overlap(j,newedge)==1){
	    if(graph[i]==1 && graph[j]==1){
	      return 0;
	    }
	    else if(graph[i]==1 && graph[j]==0){
	      graph[j] = -1;
	      (*fe)++;
	    }
	    else{
	      graph[i] = -1;
	      (*fe)++;
	    }
	    /*
	    else if(graph[i]==0 && graph[j]==1){
	      toforbid[i] = 1;
	    }
	    else{
	      bug(993);
	    }
	    */
	  }
	  else{
	    // else the three edges i,j, newedge overlap in harmless way
	  }
	}
      }
    }
  }

  return 1;
}


void build_graph(int *graph, int ne, int ze, int start){
  /*
   * graph - list of edges
   * ne - number of edges in this graph
   * ze - number of potential edges (total - ne - forbidden)
   * start - only concerned about adding new edges after the index=start
   */ 

  counter++;
  //printarr(graph,E);
  
  if((ze == 0) && (current_max < ne)){
    current_max = ne;
  }

  if(ze > 0){
    
    for(int i=start; i<E; i++){
      if(graph[i] == 0){
	int newgraph[E];
	int fe = 0;
	for(int j=0; j<E; j++){
	  newgraph[j] = graph[j];
	  if((j>=start) && (j<i) && (graph[j]==0)){
	    newgraph[j] = -1;
	    fe++;
	  }
	}
	int addable = can_add(newgraph, &fe, i); // can add edge i?
	if(addable && (MAX_COUNT <= ne+ze-fe)){
	  newgraph[i] = 1;
	  fe++;
	  build_graph(newgraph, ne+1, ze-fe, i+1);
	}
	/*
	else{ // if i not addable
	  //newgraph[i] = 1;
	  //printarr(newgraph,E);
	  //printf("not addable\n");
	  //graph[i] = -1;
	  //ze--;
	}
	*/
      }
    }	
  }
}



int main(){
  genedges();
  //for(int i=0; i<E; i++) {printbits(edges[i][0]); printbits(edges[i][1]); printbits(edges[i][2]); printbits(edges[i][3]); printf("\n");}
  
  int graph[E]; graph[0] = 1; for(int i=1; i<E; i++) graph[i] = 0;
  build_graph(graph, 1, E-1, 1);
  printf("current_max/MAX_COUNT = %d/%d\n",current_max, MAX_COUNT);
  printf("counter = %d\n", counter);
  return 0;
}


/*****************************************
 *
 *  NOTES
 *
 * 1. Rewrite things without using "forbidden edges". 
 * 2. Find out why resulting graphs have plenty of paths!
 *
 *
 *
 */
