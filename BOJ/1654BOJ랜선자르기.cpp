#include <iostream>
using namespace std;

typedef unsigned long long ll;

int K,N;
ll arr[10001];

int main() {
	cin>>K>>N;
	
	ll left=1;
	ll right=0;
	
	for(int i=1; i<=K; i++)
	{
		cin>>arr[i];
		if(right<arr[i])  right=arr[i];
	}
	ll result = 0;
	
	while(left<=right)
	{
		ll mid=(left+right)/2;
		
		ll sum = 0;
		for(int i=1; i<=K; i++)
		{
			sum+=arr[i]/mid;
		}
		
		if(sum>=N)
		{
			if(result<mid) result = mid;
			left = mid+1;
		}
		else right=mid-1;
	}
	
	cout<<result;
	// your code goes here
	return 0;
}
