
from collections import defaultdict
from report import makePDF as makeReportPDF
from utils import debug

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
		debug(" * Graph : ", self.name)
		for i in self.graph.items():
			debug(i)


	### public static methods
	def loadFromAdjacentListCSV(self, path):
		import csv

		debug(" * Loading graph from file", path)
		n = 0

		with open(path, 'r') as f:

			dialect = csv.Sniffer().sniff(f.read(1024)) # detect the syntax of the csv file
			f.seek(0)

			reader = csv.reader(f, dialect)

			f.seek(0) # reset pointer at start of the file

			print("Importing CSV file..")
			reader = list(reader);

			for row in reader:
				if row:
					self.add_edge(int(row[0]), int(int(row[1])))
				n+=1
				print(" loadFromAdjacentListCSV : ",round((n*100)/len(reader)),"%", end='\r')

			print("")



	def saveToAdjacentListCSV(self, path):
		import sys
		original_stdout = sys.stdout

		debug(" * Saving graph to file", path.name)

		with open(path.name, 'w') as f:
			sys.stdout = f # Change the standard output to the file we created.
			for i in self.graph:
				for j in range(len(self.graph[i])):
					debug(i, self.graph[i][j])
			sys.stdout = original_stdout



	##### graph analisis
	def analisis(self):
		debug("\n### Analyzing graph ", self.name)

		nVertices = self.compute_nVertices()
		debug("- Nombre de sommets :", nVertices);

		nEdges = self.compute_nEdges()
		debug("- Nombre d’arêtes :", nEdges);

		maxValency = self.compute_maxValency()
		debug("- Degré maximal :", maxValency);

		avgValency = self.compute_avgValency()
		debug("- Degré moyen :", avgValency);

		dict = self.computeValenceDistributionData()
		dict = {k: v for k, v in sorted(dict.items())}
		curve = {'x': [i for i in dict], 'y': [dict[i] for i in dict] };
		debug(curve)

		# (bonus) Le diamètre du graphe (le plus long plus court chemin entre n’importe quelle paire
		# de sommets). Vous décrirez l’algorithme utilisé, ainsi que sa complexité.
		pdf = makeReportPDF(name=self.name, nVertices=nVertices, nEdges=nEdges, maxValency=maxValency, avgValency=avgValency, curve=curve)
		debug(f'Full report saved at : @reports/{pdf}')

	def compute_nVertices(self):
		n = 0
		self.vertices = set(self.graph.keys())
		for i in self.graph:
			for j in self.graph[i]:
				self.vertices.add(j)
			n+=1
			print(" compute_nVertices : ",round((n*100)/len(self.graph)),"%", end='\r')
		print("")
		return len(self.vertices)


	def compute_nEdges(self):
		edgesCount = 0
		n = 0
		for i in self.graph:
			for j in self.graph[i]:
				edgesCount+=1
			n+=1
			print(" compute_nEdges : ",round((n*100)/len(self.graph)),"%", end='\r')
		print("")
		return edgesCount;

	def compute_maxValency(self):
		maxValency = 0
		n = 0
		for i in self.graph:
			maxValency = len(self.graph[i]) if len(self.graph[i]) > maxValency else maxValency
			n+=1
			print(" compute_maxValency : ",round((n*100)/len(self.graph)),"%", end='\r')

		print("")
		return maxValency;

	def compute_avgValency(self):
		nValency = 0
		n = 0
		for i in self.graph:
			nValency += len(self.graph[i])
			n+=1
			print(" compute_avgValency : ",round((n*100)/len(self.graph)),"%", end='\r')

		print("")
		return nValency // len(self.vertices);

	def computeValenceDistributionData(self):	### DIRTY CODE
		n = 0

		# compute valence of every vertex {vertex: valence, ...}
		valencePerVertex = defaultdict(int)
		for i in self.graph:
			valencePerVertex[i] +=1
			debug('valencePerVertex', valencePerVertex.items())

			for j in self.graph[i]:
				if i not in valencePerVertex:
					valencePerVertex.add(i)
					valencePerVertex[i] = 0
				valencePerVertex[i] +=1
			debug('valencePerVertex', valencePerVertex.items())
			n+=1
			print(" computeValenceDistributionData : ",round((n*100)/len(self.graph)),"%", end='\r')

		print("")
		# compute number of apparence for every valence {valence: # apparition, ...}
		valenceDistData = defaultdict(int)
		for i in valencePerVertex:
			valenceDistData[valencePerVertex[i]] += 1
		debug('valenceDistData', valenceDistData.items())


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
		debug("Not avaliable for the moment.")

	def genRandomGraph(method):
		if (method == "EG"):
			debug("\n### Generating a graph using Edgar Gilbert algorithm")
			return utils.genRandom_EG(5);

		elif (method == "BA"):
			debug("\n### Generating a graph using Barabàsi-Albert algorithm")
			return utils.genRandom_BA(5);

		else:
			debug("\n### BEEEZRAZE")