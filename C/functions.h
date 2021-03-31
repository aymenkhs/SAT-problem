#ifndef base
#define base

// structur to store the results of the time execution
typedef struct StoreTime StoreTime;
struct StoreTime
{
	int n; // the number of clauses
	int m; // the number of booleans
    double time_execution; // time to execute the verification
    int value; // true if the SAT is verified, false elsewhere
};

// time measurement functions
StoreTime * tab_execution(int * (* function)(int**, int*, int, int), int n, int m_min, int m_max, int pas);
double execution_time(int * (* function)(int**, int*, int, int), int **SAT, int* V, int n, int m, StoreTime *result);

// tables generation
int * genererV(int m);
int ** genererSAT(int n, int m);

void print_SAT(int **SAT, int n, int m);
void print_V(int *V, int n);

int **allocate_2D_array(int rows, int columns);

// ecrire les resultats dans un fichier csv
int writeCSV(StoreTime * results, int taille);

#endif // base
