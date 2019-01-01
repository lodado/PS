#include <stdio.h>
#define INF 987654321
typedef unsigned long long int lli;
int arr[100001];
int min(int a,int b)
{
	return a>b?b:a;	
}
int main() {
	int N,S,scan;
	lli sum=0;
	int max = INF;
	scanf("%d %d",&N,&S);
	int head=0,tail=0;
	while(head<N && tail!=N)
	{
		scanf("%d",&scan);
		sum+=scan;
		arr[tail++]=scan;
		while(sum>=S)
		{
			sum-=arr[head++];
			max=min(tail-head+1,max);
		}
	}
	printf("%d",max!=INF?max:0);
	return 0;
}
