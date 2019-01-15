#include<cstdio>
#include<vector>
using namespace std;

int N,n;

vector<int> v[101];

bool visited[101];

void DFS(int start=1)
{
	visited[start]=true;
	
	for(unsigned int i=0; i<v[start].size(); ++i)
	{
		int there = v[start][i];
		if(!visited[there])
		{
			DFS(there);
		}
	}
}

int main()
{
	int scan1,scan2;
	scanf("%d %d",&N,&n);
	
	for(int i=0; i<n; ++i)
	{
		scanf("%d %d",&scan1,&scan2);
		v[scan1].push_back(scan2);
		v[scan2].push_back(scan1);
	}
	
	DFS();
	int num=0;
	for(int i=1; i<=N; i++)
	{
		if(visited[i]) num++;
	}
	
	printf("%d",num-1);
	return 0;
}
