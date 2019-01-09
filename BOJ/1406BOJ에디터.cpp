#include<cstdio>
using namespace std;

struct Node{
	
	char data;
	struct Node* head;
	struct Node* tail;
	
	Node(){}
	Node(char data)
	{
		this->data=data;
		head=tail=NULL;
	}
};

class linkedList : public Node
{

	Node* front;
	Node* back;
	Node* iter;	
	
	public:
		linkedList()
		{
			front = new Node('!');
			back  = new Node('@');
			
			front->head=back;
			back->tail=front;
			iter=back;
		}
	
		void push_back(char data)
		{
			Node* newNode = new Node(data);
			
			if((front->head)==(back))
			{
				newNode->head=back;
				newNode->tail=front;
				back->tail=newNode;
				front->head=newNode;
				
				//printf("push %c!\n",data);
			}
			else
			{
				newNode->head=back;
				newNode->tail=back->tail;
				back->tail->head=newNode;
				back->tail=newNode;
				//printf("push %c..\n",data);
			}
		}
		
		void check()
		{
			Node* current=front->head;
			while(current!=back)
			{
				printf("%c",current->data);
				current=current->head;
			}
			//printf("          cursor : %c  \n",iter->data);
		}
		
		void L()
		{
			if(iter!=front && iter->tail!=front)	iter=iter->tail;
		}
		
		void D()
		{
			if(iter!=back)	iter=iter->head;
		}
		
		void B()
		{
			if(iter!=front && iter->tail!=front)
			{
				if(iter!=back)
				{
					Node* delNode =iter->tail;
				
					delNode->tail->head=iter;
					iter->tail=delNode->tail;
				
					delete delNode;
				}
				else
				{
					Node* delNode=iter->tail;
					
					delNode->tail->head=back;
					back->tail=delNode->tail;
					
					delete delNode;
				}
			}
		}
		
		void P(char data)
		{
			if(iter==back)
			{
				push_back(data);
			}
			else
			{
				Node* newNode = new Node(data);
				
				Node* iterator = iter;
				newNode->head=iterator;
				newNode->tail=iterator->tail;
				
				iterator->tail->head=newNode;
				iterator->tail=newNode;
				
			}
		}
};


int main()
{
	linkedList list;
	int N;
	char scan,Data,b;
	
	while(1)
	{
		scanf("%c",&scan);
		if(scan=='\n') break;
		list.push_back(scan);
	}
	
	scanf("%d%c",&N,&b);
	
	for(int i=0; i<N; ++i)
	{
		scanf("%c%c",&scan,&b);
		switch(scan)
		{
			case 'L':
				list.L();
				break;
			case 'D':
				list.D();
				break;
			case 'B':
				list.B();
				break;
			case 'P':
				scanf("%c%c",&Data,&b);
				list.P(Data);
				break;
		}	
	}
	
	list.check();
	
	return 0;
}
