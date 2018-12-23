#include <cstdio>
#include <queue>
#include <tuple>
#define INF 987654321
using namespace std;

int row,col;
int miro[101][101]; // row,col
int dist[101][101];

int dx[]={1,-1,0,0};
int dy[]={0,0,1,-1};

void djikstra(int startx,int starty)
{
	priority_queue<tuple<int,int,int>> pq;
	dist[startx][starty]=0;
	pq.push(make_tuple(0,startx,starty));  //dist,row,col
	
	while(!pq.empty())
	{
		int cost,herex,herey;
		tie(cost,herex,herey)=pq.top();
		cost=-cost;
		pq.pop();
		if(cost>dist[herex][herey]) continue;
		
		for(int i=0; i<4; ++i)
		{
			int newx=herex+dx[i];
			int newy=herey+dy[i];
			
			if(newx<=0||newy<=0||newx>row||newy>col) continue;
			
			int via = cost + miro[newx][newy];
			
			if(via<dist[newx][newy])
			{
				dist[newx][newy]=via;
				pq.push(make_tuple(-via,newx,newy));
			}
		}
	}
	printf("%d",dist[row][col]);
}

int main() {
	
	scanf("%d %d",&row,&col);
	
	for(int i=1; i<=col; ++i)
	{
		for(int j=1; j<=row; ++j)
		{
			scanf("%1d",&miro[j][i]);
			dist[j][i]=INF;
		}
	}
	
	djikstra(1,1);
	// your code goes here
	return 0;
}
