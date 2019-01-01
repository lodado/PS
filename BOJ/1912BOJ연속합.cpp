#include <iostream>
using namespace std;

int isitmax(int a,int b)
{
	return a>b?a:b;	
}
int main() {
    
long long int max=-1,dp[100001]={0,};
int n,scan,minimum=-987654321;
scanf("%d",&n);

for(int i=1; i<=n; i++)
{
	scanf("%d",&scan);
	
	if(scan<=0) minimum=isitmax(minimum,scan);
	dp[i]=dp[i-1]+scan;
	
	if(dp[i]>0)
	{
		max=isitmax(max,dp[i]);
	}
	else dp[i]=0;
}

	printf("%d",max>0?max:minimum);
	return 0;
}
