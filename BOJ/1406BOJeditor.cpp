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
		// init
	
		void push_back(char data)
		{
			Node* newNode = new Node(data);
			newNode->head=back;

			if((front->head)==(back))	
			{
				
				newNode->tail=front;
				back->tail=newNode;
				front->head=newNode;
				
				//printf("push %c!\n",data);
			}
			else
			{
				newNode->tail=back->tail;
				back->tail->head=newNode;
				back->tail=newNode;
				//printf("push %c..\n",data);
			}
		}
		//I should have been changed or removed front but i am lazy zz..
		//push data(char) between front and back
		
		void check()
		{
			Node* current=front->head;
			Node* forFree=current;
			while(current!=back)
			{
				printf("%c",current->data);
				current=current->head;
				free(forFree);
				forFree=current;
			}
			
			free(front);
			free(back);
			//printf(" cursor : %c  \n",iter->data);
		}
		// print data
		
		void L()
		{
			if(iter!=front && iter->tail!=front)	iter=iter->tail;
		}
		// move cursor to left
		
		
		void D()
		{
			if(iter!=back)	iter=iter->head;
		}
		//move cursor to right

		void B()
		{
			if(iter!=front && iter->tail!=front)
			{
				Node* delNode =iter->tail;
				
				if(iter!=back)
				{
					delNode->tail->head=iter;
					iter->tail=delNode->tail;
				}
				else
				{	
					delNode->tail->head=back;
					back->tail=delNode->tail;
				}
					delete delNode;
			}
		}
		// delete 
		
		void P(char data)
		{
			if(iter==back)
			{
				push_back(data);
			}
			else
			{
				Node* newNode = new Node(data);
			
				newNode->head=iter;
				newNode->tail=iter->tail;
				
				iter->tail->head=newNode;
				iter->tail=newNode;
				
			}
		}
		//push 
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
