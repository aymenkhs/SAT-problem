#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <math.h>

#include "functions.h"


//  Fonction  qui  prend en parametre une fonction est entier n
// et qui retourne le temps d'execution de chaque iteration sur une
//SAT et un Vecteur V generer aleatoirement dans un autre tableau d'enregistrements
StoreTime * tab_execution(int * (* function)(int**, int*, int, int), int n, int m_min, int m_max, int pas){

    int **SAT, *V, m, taille = (int)((m_max - m_min)/pas);
    StoreTime *results = malloc(taille * sizeof(StoreTime));

    for(int i=0; i<taille; i++){
        m = m_min + (i*pas);

        results[i].n = n;
        results[i].m = m;
        printf("nombre n:%d m:%d\n\n", n, m);

        SAT = genererSAT(n, m);
        V = genererV(m);

        execution_time(function, SAT, V, n, m, &results[i]);

        printf("temps d'execution:%f\n\n\n", results[i].time_execution);

    }
    return results;
}

//  Fonction  qui  retourne  le  temps d’execution de la fonction donner en parametre
double execution_time(int * (* function)(int**, int*, int, int), int **SAT, int* V, int n, int m, StoreTime *result){
    clock_t t1 , t2;

    int boolean;

    t1 = clock ();
    boolean = function(SAT, V, n, m);
    t2 = clock ();

    double temps_exe = (double) (t2 -t1)/CLOCKS_PER_SEC;

    result->value = boolean;
    result->time_execution = temps_exe;

    return temps_exe;
}

// fonction qui genere un Tableau de boolean
int * genererV(int m){
    int *V = malloc(m * sizeof(int));
    for(int i=0; i<m; i++){
        V[i] = rand() % 2;
    }
    return V;
}

// fonction qui genere une matrice SAT
int ** genererSAT(int n, int m){
    int random_number;
    int **SAT = allocate_2D_array(n, m);
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            random_number = rand() % 3;
            if(random_number == 2){
                random_number = -1;
            }
            SAT[i][j] = random_number;
        }
    }
    return SAT;
}

void print_SAT(int **SAT, int n, int m){

    printf("La matrice SAT: \n");

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if (SAT[i][j] == -1){
                printf("%d ", SAT[i][j]);
            } else {
                printf(" %d ", SAT[i][j]);
            }
        }
        printf("\n");
    }
    printf("\n\n");
}

void print_V(int *V, int n){

    printf("Le Vecteur de boolean Solution generer V: \n");

    for(int i=0; i<n; i++){
        printf("%d ", V[i]);
    }
    printf("\n\n");
}

int **allocate_2D_array(int rows, int columns){
    int k = 0;
    int **array = malloc(rows * sizeof (int *) );

    array[0] = malloc(columns * rows * sizeof (int) );
    for (k=1; k < rows; k++){
        array[k] = array[0] + columns*k;
        bzero(array[k], columns * sizeof (int) );
    }

    bzero(array[0], columns * sizeof (int) );

    return array;
}

// fonction qui ecris dans un fichier csv les resultats des mesures de temps
int writeCSV(StoreTime * results, int taille){

    FILE* fp = NULL;

    fp= fopen("SAT_C.csv","w+");

    if (fp == NULL){
        printf("Fichier inexistant\n");
        return 0;
    }

    fprintf(fp,"n,m,value,time_exe");
    for(int i=0; i<taille; i++){
        fprintf(fp,"\n%d,%d,%d,%.10lf", results[i].n, results[i].m, results[i].value, results[i].time_execution);
    }

    fclose(fp);

    return 1;
}
