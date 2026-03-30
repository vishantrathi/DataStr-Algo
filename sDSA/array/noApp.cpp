//Q: find the no appreaing  once and   in an twice array
#include<bits/stdc++.h>
using namespace std;

int noAppOnce(int arr[], int n){
    for(int i=0;i<n;i++){
        int index=0;

        for(int j=0;j<n;j++){
        if(arr[i]==arr[j]){
            index++;
        }
    }
    if(index == 1){
        return arr[i];
    }
}
    return -1;
}

int main(){
    int arr[]={1,1,2,3,3,4,4,5,5};
    int n=9;
    noAppOnce(arr,n);
    cout << noAppOnce(arr,n);
}