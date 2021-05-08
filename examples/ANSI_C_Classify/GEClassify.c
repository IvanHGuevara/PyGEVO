

#include <math.h>
#include <stdio.h>
#include "GEClassify.h"

int Evolved[FitnessCases];

int AssignFitness() {
  int i;
  double fit, sum;
  fit=0;
  sum=0;
  for(i=0;i<FitnessCases;i++) {
		sum += Evolved[i];
  }

  fit = sum;
  return fit;
}

double if_cond(double exp1,double exp2,double exp3,double exp4) {
  if(exp1 <= exp2)
    return exp3;
  else
    return exp4;
}

double pdiv(double a1,double a2) {
  if(a2 == 0)
    return 0;
  else
    return a1/a2;
}

double myadd(double a1,double a2) {
  return a1+a2;
}

double mysub(double a1,double a2) {
  return a1-a2;
}

double mymul(double a1,double a2) {
  return (a1*a2);
}

