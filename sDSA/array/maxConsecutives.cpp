#include<bits/stdc++.h>
using namespace std;
//Q:  max consecutive no
int maccon(int arr[],int n){
    int total=n*(n+1)/2;
    int count=0;
    int maxi=0;

    for(int i=0;i<n;i++){
        if(arr[i]==1){
            count +=1;
            maxi=max(maxi,count);
        }else{
            count =0;
        }
    }
    return maxi;

}
int main(){
    int arr[]={1,1,0,0,0,1,1,1,1};
    int n=9;
    maccon(arr,n);
    cout<<maccon(arr,n);

}