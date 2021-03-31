#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "functions.h"

#define TRUE 1
#define FALSE 0

int SAT_Ver(int **SAT, int* V, int n, int m);


int main(){
    srand(time(NULL));

    char function_name[20] = "SAT_ver";

    int (* fonction)(int**, int*, int, int) = SAT_Ver;

    int n = 10000, m_min = 2000, m_max = 32000, pas = 2000;

    StoreTime* results = tab_execution(fonction, n, m_min, m_max, pas);

    writeCSV(results, (int)((m_max - m_min)/pas));

    printf("%s done.\n\n", function_name);

    return EXIT_SUCCESS;
}


int SAT_Ver(int **SAT, int* V, int n, int m){

	int satisfiable = TRUE;

	int i = 0;
	int clause;

	while(satisfiable && i < n){
		clause = FALSE;

		for(int j = 0; j < m; j++){
			if ( SAT[i][j] == V[j] ){
				clause = TRUE;
                break;
			}
		}

		if(clause == FALSE) {
            satisfiable = FALSE;
        }
		i++;
	}

	if(satisfiable)
		printf("L'instance resout le probleme. \n");
	else
		printf("L'instance ne resout pas le probleme. \n");

	return satisfiable;
}
