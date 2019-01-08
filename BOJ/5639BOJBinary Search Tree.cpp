#include <iostream>
#define null 0
using namespace std;

class Tree;

class TreeNode{
	
	friend class Tree;
	int data;
	TreeNode* left;
	TreeNode* right;
	public:
	TreeNode(int data=0, TreeNode* left = null, TreeNode* right = null)
	{
		this->data = data;
		this->left = left;
		this->right= right;
	}
};

class Tree{
		
		TreeNode* root;
		public:
		Tree(int data=0)
		{
			root=new TreeNode(data);
		}
		
		TreeNode* search(int data, TreeNode* now)
		{
			if(now==null) return null;
			
			if(now->data == data) return now;
			else if(now->data > data) return search(data,now->left);
			else return search(data,now->right);
		}
	
		void insert(TreeNode* Node)
		{
			if(search(Node->data,root)==null)
			{
		
			TreeNode* current = root;
			TreeNode* parent  = null;
			
			while(current!=null)
			{
				parent=current;
				
				if(Node->data < parent->data) current= current->left;
				else current= current->right;
			}
				if(parent->data>Node->data) parent->left = Node;
				else parent->right = Node;
			}
		}
		
		TreeNode* getroot()
		{
			return root;
		}
		
		void PostOrder(TreeNode* now)
		{
			if(now!=null)
			{
				PostOrder(now->left);
				PostOrder(now->right);
				printf("%d\n",now->data);
			}
		}
};


int main() {
	
	int n;
	scanf("%d",&n);
	
	Tree tree(n);
	
	while(scanf("%d",&n)!=EOF) tree.insert(new TreeNode(n));
	
	tree.PostOrder(tree.getroot());
	// your code goes here
	return 0;
}
