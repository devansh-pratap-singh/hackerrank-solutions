#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  int n,i,j,x,a,b;
  vector<int>arr;
  cin>>n;
  for(i=0;i<n;i++) {
    cin>>j;
    arr.push_back(j);
  }
  cin>>x>>a>>b;
  arr.erase(arr.begin()+(x-1));
  arr.erase(arr.begin()+(a-1),arr.begin()+(b-1));
  cout<<arr.size()<<endl;
  for(i=0;i<arr.size();i++)
    cout<<arr.at(i)<<" ";
  return 0;
}