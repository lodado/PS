#include <iostream>
#include <vector>
using namespace std;

int parent[51]={0,};
int result=0,n=0,N=0,root=0;
vector<int> v[51];

void swap(int& a,int& b)
{
	int temp=a;
	a=b;
	b=temp;
}

void DFS(int data)
{
	if(v[data].empty())
	{
		 if(n!=data) result++;
	}
	else
	{
		for(int i=0; i<v[data].size(); i++)
		{
			DFS(v[data][i]);
		}
	}
	
}

int main() {
	
	scanf("%d",&N);
	
	for(int i=0; i<N; i++)
	{
		scanf("%d",&parent[i]);
		if(parent[i]==-1) root=i;
		else
		{
			v[parent[i]].emplace_back(i);
		}
	}
	
	scanf("%d",&n);
	
	v[n].clear();
	
	for(int i=0; i<v[parent[n]].size(); i++)
	{
		int there =v[parent[n]][i];
		
		if(there==n)
		{
			if((v[parent[n]].back())!=there) swap(v[parent[n]].back(),v[parent[n]][i]);
			v[parent[n]].pop_back();
			break;
		}
	}
	
	DFS(root);
	
	printf("%d",result);
	// your code goes here
	return 0;
}
