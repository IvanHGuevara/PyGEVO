
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "GEClassify.c"


int Evolved[FitnessCases];

int main() {
	
	FILE *file;

    double Dim[FitnessCases][Variables+1];

    if (!(file = fopen("SampleData.txt", "r"))) {
        printf("Error opening file");
        exit(0);
    }

    for (int i = 0; i < FitnessCases; i++) {
        for (int j = 0; j < Variables+1; j++) {
            fscanf(file, "%lf", &Dim[i][j]);
        }
    }

	fclose(file);
	int i;
	double temp;
	
	for(i=0;i<FitnessCases;i++) {
		printf("%f\n",Dim[i][5]);
		temp=cos(log(Dim[i][5]));
		if(temp < 0 && Dim[i][Variables] == 0){
		 Evolved[i]=1;}
		else if(temp > 0 && Dim[i][Variables] == 1){
		 Evolved[i]=1;}
		else{
		 Evolved[i]=0;}
	}
	printf("%d\n",AssignFitness());
}

