from sys import stdin

class Node:
	def __init__(self, key, data=None):
		self.key = key
		self.data = data
		self.children = {}
		
class Trie:
	def __init__(self):
		self.head = Node(None)
	
	def insert(self, string):
		currentNode = self.head
		
		for now in string:
			if(now not in currentNode.children):
				currentNode.children[now] = Node(now)
			currentNode = currentNode.children[now]
		currentNode.data = string
	
	def search(self, string):
		currentNode = self.head
		
		for now in string:
			if(now in currentNode.children):
				currentNode = currentNode.children[now]
			else:
				return False
		
		if(currentNode.key):
			return True
		else:
			return False
	
		
def scan():
	return stdin.readline().strip()
	
T=int(scan())
		
for _ in range(T):
	
	trie = Trie()
	
	N = int(scan())
	arr = [scan() for _ in range(N)]
	flag = False
	
	for data in sorted(arr, reverse=True):
		if not(trie.search(data)):
			trie.insert(data)
		else:
			flag=True
			break
			
	if(flag):
		print('NO')
	else:
		print('YES')
