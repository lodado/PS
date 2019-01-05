#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int N;

int main() {
	
	scanf("%d",&N);
	int scan1,scan2;
	vector<pair<int,int>> v;
	
	v.reserve(N);
	
	for(int i=0; i<N; ++i)
	{
		scanf("%d %d",&scan1,&scan2);
		v.emplace_back(make_pair(scan2,scan1));
	}
	
	sort(v.begin(),v.end());
	
	int head=0,result=0;
	
	for(unsigned int i=0; i<v.size(); i++)
	{
		int end  = v[i].first;
		int start= v[i].second;
		
		if(head<=start)
		{
			head=end;
			result++;
		}
	}
	printf("%d",result);
	
	
	
	return 0;
}
