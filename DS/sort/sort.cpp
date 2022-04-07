#include<iostream>
using namespace std;
typedef int ElemType;
void InsertSort(ElemType R[],int n){
    int i,j;
    ElemType temp;
    for(i = 1; i < n; i++){
        temp = R[i];
        for ( j = i-1; j >= 0 && temp < R[j]; j--){
            R[j+1] = R[j];
        }
        R[j+1] = temp;
    }
}
int main(){
    int a[10] = {1,4,8,1,2,30,9,12,7,6}
    InsertSort(a,10);
    for( int i = 0; i < 10; i++)
    cout << a[i] << ' ';
    return 0;
}