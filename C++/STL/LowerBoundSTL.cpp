#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  int n,q,num;
  cin>>n;
  vector<int>arr;
  for(int i=0;i<n;i++) {
    cin>>num;
    arr.push_back(num);
  }
  cin>>q;
  for(int i=0;i<q;i++) {
    cin>>num;
    vector<int>::iterator low=lower_bound(arr.begin(),arr.end(),num);
    if (arr[low - arr.begin()]==num)
      cout<<"Yes "<<(low-arr.begin()+1)<<endl;
    else
      cout<<"No "<<(low-arr.begin()+1)<<endl;
  }
  return 0;
}