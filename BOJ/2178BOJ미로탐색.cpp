#include <cstdio>
#include <deque>
using namespace std;

int N,M,path[101][101];
int depth[101][101]={0,};

int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};

void BFS(int starty,int startx)
{
	deque<pair<int,int>> dq;
	dq.emplace_back(make_pair(starty,startx));
	
	depth[starty][startx] = 1;
	
	while(!dq.empty())
	{
		int y = dq.front().first;
		int x = dq.front().second;
		dq.pop_front();
		int dist = depth[y][x];
		
		for(int i=0; i<4; ++i)
		{
			int newx=x+dx[i], newy=y+dy[i];
			
			if(path[newy][newx] && !depth[newy][newx]&& newy<=N && newx<=M)
			{
				dq.emplace_back(make_pair(newy,newx));
				depth[newy][newx] = dist+1;
			}
			
		}
		
		if(depth[N][M]) {
			printf("%d",depth[N][M]);
			return;
		}
	}
	
}

int main() 
{
	
	scanf("%d %d",&N,&M);
	
	int i,j;
	for(i=1; i<=N; ++i)
	{
		for(j=1; j<=M; ++j) scanf("%1d",&path[i][j]); // [세로][가로]
	}
	BFS(1,1);
	return 0;
}
