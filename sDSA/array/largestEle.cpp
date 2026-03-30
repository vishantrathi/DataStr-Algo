//q: find the largest element from  array
//so, the solution is brute force, better, optimal
#include<bits/stdc++.h>
using namespace std;


// brute force=> sort the array and print the last element

// optimal=> assume the first element is the largest and iterate over rest of the array if any value is bigger than the element stored as largest element than replace the element as the itration find the largest element than the stord ones.

//brute force
int arrayS(int arr[], int n){
    int largest = arr[0];

    for(int i=0;i<n;i++){
        if(arr[i]>largest){
            largest=arr[i];
        }
    }
    return largest;
}


int main(){

    int arr[]={1,2,3,7,5,4,8};
    int n=7;
    int ans=arrayS(arr,n);
    cout<<ans;

}