#include <iostream>
#include <deque> 
using namespace std;

void printKMax(int arr[], int n, int k) {
	if (n == 0) {return;}
  if (n == 1 && k == 1) {cout << arr[1] << "\n";}
  deque<int> maxs;
  for(int i = 0; i < n; i++) {    
    while(!maxs.empty() && arr[i] > arr[maxs.back()]) {maxs.pop_back();}
    maxs.push_back(i);
    while(!maxs.empty() && maxs.front() <= (i - k)) {maxs.pop_front();}
    if (i >= k-1) {cout << arr[maxs.front()] << " ";}
  }
  cout << "\n";
}

int main() {
	int t;
	cin >> t;
	while(t>0) {
		int n,k;
    cin >> n >> k;
    int i;
    int arr[n];
    for(i=0;i<n;i++)
    	cin >> arr[i];
    printKMax(arr, n, k);
    t--;
  }
  return 0;
}