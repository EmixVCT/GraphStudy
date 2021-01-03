
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

		print(" * Loading graph from file", path)
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

		print(" * Saving graph to file", path.name)

		with open(path.name, 'w') as f:
			sys.stdout = f # Change the standard output to the file we created.
			for i in self.graph:
				for j in range(len(self.graph[i])):
					print(i, self.graph[i][j])
			sys.stdout = original_stdout



	##### graph analisis
	def analisis(self,diameter):
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

		if diameter:
			diameter = self.compute_diameter()
			debug(diameter)

		# (bonus) Le diamètre du graphe (le plus long plus court chemin entre n’importe quelle paire
		# de sommets). Vous décrirez l’algorithme utilisé, ainsi que sa complexité.
		pdf = makeReportPDF(name=self.name, nVertices=nVertices, nEdges=nEdges, maxValency=maxValency, avgValency=avgValency, curve=curve)
		print(f'Full report saved at : @reports/{pdf}')

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

	def compute_diameter(self):
		longest = 0
		n = 0
		#print(self.dijkstra(2034,1939))
		
		for i in self.graph:
			print(" compute_diameter : ",round((n*100)/(len(self.graph))),"%", end='\r')
			n += 1
			debug("")
			shorter = self.dijkstra(i)
			max_value = max(shorter.values())  # maximum value
			if (float('inf') != longest and max_value > longest):
				longest = max_value
				
		print(" compute_diameter : ",round((n*100)/(len(self.graph))),"%")
		return longest

	def dijkstra(self, src, dst=None):
		nodes = []
		for n in self.graph:
			nodes.append(n)

		q = set(nodes)
		debug(q)

		nodes = list(q)
		dist = dict()
		for n in nodes:
			dist[n] = float('inf')

		dist[src] = 0



		while q:
			u = min(q, key=dist.get)
			q.remove(u)

			if dst is not None and u == dst:
				debug(u, "dist: ",dist[dst]," entre ",src," et ",dst)
				return dist[dst]

			for v in self.graph[u]:
				alt = dist[u] + 1
				if v in dist and alt < dist[v]:
					dist[v] = alt

		debug("dist: ",dist," entre ",src," et le reste")

		return dist

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

	def genRandom_BA(vertices, m):

		if m < 1 or  m >= vertices:
			print(f'Barabási–Albert network must have m >= 1 and m < n, m = {m}, n = {n}')

		graph = Graph()

		targets=list(range(m))	# Target nodes for new edges
		repeated_nodes=[]		# List of existing nodes, with nodes repeated once for each adjacent edge
		source=m				# Start adding the other n-m nodes. The first node is m.

		while source < vertices:
			for target in targets:
				graph.add_edge(source, target) 		# Add edges to m nodes from the source.

			repeated_nodes.extend(targets) 			# Add one node to the list for each new edge just created.
			repeated_nodes.extend(range(m)) 		# And the new node "source" has m edges to add to the list.

			# Now choose m unique nodes from the existing nodes
			# Pick uniformly from repeated_nodes (preferential attachement)
			targets = utils.random_subset(repeated_nodes, m)
			source += 1

		return graph;


	def random_subset(repeated_nodes, m):
		import random

		rand_index = [ random.randrange(len(repeated_nodes)) for i in range(m) ]
		res = [repeated_nodes[r] for r in rand_index]
		return res


	def genRandomGraph(method):
		if (method == "EG"):
			print("\n### Generating a graph using Edgar Gilbert algorithm")
			return utils.genRandom_EG(5);

		elif (method == "BA"):
			print("\n### Generating a graph using Barabàsi-Albert algorithm")
			return utils.genRandom_BA(5, 2);

		else:
			print("\n### BEEEZRAZE")
