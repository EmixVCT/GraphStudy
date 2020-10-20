
from collections import defaultdict
from report import makePDF as makeReportPDF

class Graph:

	def __init__(self, path="", name="unnamed"):
		
		self.graph = defaultdict(list)
		self.name = name

		if path:
			self.loadFromAdjacentListCSV(path)


	#### private methods
	def add_edge(self, src, dest):
		if self.graph[src] == None:
			self.graph[src] = [];
		if dest not in self.graph[src]: self.graph[src].append(dest)

	# Function to print the graph 
	def print_graph(self):
		print(" * Graph : ", self.name)
		for i in self.graph.items():
			print(i)


	### public static methods
	def loadFromAdjacentListCSV(self, path):
		import csv

		print(" * Loading graph from file", path)

		with open(path, 'r') as f:

			dialect = csv.Sniffer().sniff(f.read(1024)) # detect the syntax of the csv file
			f.seek(0)

			reader = csv.reader(f, dialect)

			f.seek(0) # reset pointer at start of the file

			for row in reader:
				if row:
					self.add_edge(int(row[0]), int(int(row[1])))


	def saveToAdjacentListCSV(self, path):
		import sys
		original_stdout = sys.stdout

		print(" * Saving graph to file", path.name)

		with open(path.name, 'w') as f:
			sys.stdout = f # Change the standard output to the file we created.
			for i in self.graph:
				for j in range(len(self.graph[i])):
					print(i, self.graph[i][j])
			sys.stdout = original_stdout



	##### graph analisis
	def analisis(self):
		print("\n### Analyzing graph ", self.name)

		nVertices = self.compute_nVertices()
		print("- Nombre de sommets :", nVertices);

		nEdges = self.compute_nEdges()
		print("- Nombre d’arêtes :", nEdges);

		maxValency = self.compute_maxValency()
		print("- Degré maximal :", maxValency);

		avgValency = self.compute_avgValency()
		print("- Degré moyen :", avgValency);

		dict = self.computeValenceDistributionData()
		dict = {k: v for k, v in sorted(dict.items())}
		curve = {'x': [i for i in dict], 'y': [dict[i] for i in dict] };
		print(curve)

		# (bonus) Le diamètre du graphe (le plus long plus court chemin entre n’importe quelle paire
		# de sommets). Vous décrirez l’algorithme utilisé, ainsi que sa complexité.

		pdf = makeReportPDF(name=self.name, nVertices=nVertices, nEdges=nEdges, maxValency=maxValency, avgValency=avgValency, curve=curve)
		print(f'Full report saved at : @reports/{pdf}')

	def compute_nVertices(self):
		self.vertices = set(self.graph.keys())
		for i in self.graph:
			for j in self.graph[i]:
				self.vertices.add(j)

		return len(self.vertices)


	def compute_nEdges(self):
		edgesCount = 0
		for i in self.graph:
			for j in self.graph[i]:
				edgesCount+=1

		return edgesCount;

	def compute_maxValency(self):
		maxValency = 0
		for i in self.graph:
			maxValency = len(self.graph[i]) if len(self.graph[i]) > maxValency else maxValency

		return maxValency;

	def compute_avgValency(self):
		nValency = 0
		for i in self.graph:
			nValency += len(self.graph[i])

		return nValency // len(self.vertices);

	def computeValenceDistributionData(self):	### DIRTY CODE

		# compute valence of every vertex {vertex: valence, ...}
		valencePerVertex = defaultdict(int)
		for i in self.graph:
			valencePerVertex[i] +=1
			print('valencePerVertex', valencePerVertex.items())

			for j in self.graph[i]:
				if i not in valencePerVertex:
					valencePerVertex.add(i)
					valencePerVertex[i] = 0
				valencePerVertex[i] +=1
			print('valencePerVertex', valencePerVertex.items())


		# compute number of apparence for every valence {valence: # apparition, ...}
		valenceDistData = defaultdict(int)
		for i in valencePerVertex:
			valenceDistData[valencePerVertex[i]] += 1
		print('valenceDistData', valenceDistData.items())


		# compute frequency of every valence {valence: # frequency, ...}
		valenceDistPercentage = defaultdict(int)
		count = 0
		for i in valenceDistData:
			count += valenceDistData[i];

		for i in valenceDistData:
			valenceDistPercentage[i] += valenceDistData[i]/count*100;

		return valenceDistPercentage


class utils: 
	##### graph generation
	def genRandom_EG(vertices):
		import random

		graph = Graph()
		
		for i in range(vertices):
			for j in range(i+1, vertices):
				if random.choice([True, False]):
					graph.add_edge(i, j)
	  
		return graph;

	def genRandom_BA(vertices):
		print("Not avaliable for the moment.")

	def genRandomGraph(method):
		if (method == "EG"):
			print("\n### Generating a graph using Edgar Gilbert algorithm")
			return utils.genRandom_EG(5);

		elif (method == "BA"):
			print("\n### Generating a graph using Barabàsi-Albert algorithm")
			return utils.genRandom_BA(5);

		else:
			print("\n### BEEEZRAZE")