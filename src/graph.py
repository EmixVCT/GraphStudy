
class Graph:

	def __init__(self, vertices=None, path=""):
		if vertices:
			self.vertices = vertices
			self.graph = [None] * self.vertices

		elif path:
			self.loadFromAdjacentListCSV(path)


	#### private methods
	def add_edge(self, src, dest):
		if self.graph[src] == None:
			self.graph[src] = [];
		if dest not in self.graph[src]: self.graph[src].append(dest)

		if self.graph[dest] == None:
			self.graph[dest] = [];
		if src not in self.graph[dest]: self.graph[dest].append(src) # Adding the node to the source node 

	# Function to print the graph 
	def print_graph(self):
		for i in range(self.vertices): 
			print("[ {} ] : ".format(i), end='')
			print(*self.graph[i], sep = ", ")



	### public static methods
	def loadFromAdjacentListCSV(self, path):
		import csv

		print(" * Loading graph from file", path)

		with open(path, 'r') as f:
			reader = csv.reader(f)

			self.vertices = len(list(reader))
			self.graph = [None] * self.vertices

			f.seek(0) # reset pointer at start of the file

			index = 0
			for row in reader:

				print(index,':', ', '.join(row))

				for entry in row:
					print('	-> insterting', entry, 'in', index)
					self.add_edge(index, int(entry))

				index+=1


	def saveToFile(self, path):
		import sys
		original_stdout = sys.stdout

		print(" * Saving graph to file", path.name)

		with open(path.name, 'w') as f:
			sys.stdout = f # Change the standard output to the file we created.
			for i in range(self.vertices):
				print(*self.graph[i], sep = ",")
			sys.stdout = original_stdout



	##### graph analisis
	def analize(file):
		print("### Analyzing graph ", file)




class utils: 
	##### graph generation
	def genRandom_EG(vertices):
		import random

		graph = Graph(vertices=vertices)
		
		for i in range(graph.vertices):
			for j in range(i+1, graph.vertices):
				if random.choice([True, False]):
					graph.add_edge(i, j)
	  
		return graph;

	def genRandom_BA(vertices):
		print("Not avaliable for the moment.")

	def genRandomGraph(method):
		if (method == "EG"):
			print("### Generating a graph using Edgar Gilbert algorithm")
			return utils.genRandom_EG(5);

		elif (method == "BA"):
			print("### Generating a graph using Barabàsi-Albert algorithm")
			return utils.genRandom_BA(5);

		else:
			print("### BEEEZRAZE")