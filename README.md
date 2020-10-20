# GraphStudy
Etude de graphes du Web

## Instructions
- Install dependencies
	`pip3 install -r requirements.txt`
- You can now run the program
	`python3 ./src/main.py [OPTIONS]`
### Options
`python3 ./src/main.py --help` To show all options :
```bash
	--gen-graph         Generate a graph (you can specify the method with
						--method, default EG)
	--method [EG|BA]	[with --gen-graph] Name if the generation method (EG for
						Edgar Gilbert, BA for Barabàsi-Albert)
	--out FILENAME		[with --gen-graph] Path to the file of the generated
						graph

	--analyze FILENAME	Path to the file of the graph to analyze

	--help				Show this message and exit.
```

### Examples
- Generate a graph with Barabàsi-Albert method and store it :
`python3 ./src/main.py --gen-graph --method BA --out ba_graph.csv`
- Analyse it :
`python3 ./src/main.py --analyze ./ba_graph.csv`
Informations on the graph should be printed on your terminal, and you can find more results in the pdf report generated for you (for this example it should be ./ba_graph-report.pdf)


## Stockage d'un graphe
(https://www.wikiwand.com/en/Graph_(abstract_data_type)#/Representations)
with |V | the number of vertices and |E | the number of edges

							|	Adjacency list		|Adjacency matrix	|Incidence matrix
===========================================================================================
Store graph 				|	O(|V|+|E|)			|O(|V|^{2}) 		|O(|V|\cdot |E|)
Add vertex 					|	O(1)				|O(|V|^{2})			|O(|V|\cdot |E|)
Add edge 					|	O(1) 				|O(1) 				|O(|V|\cdot |E|)
Remove vertex 				|	O(|E|) 				|O(|V|^{2}) 		|O(|V|\cdot |E|)
Remove edge 				|	O(|V|) 				|O(1) 				|O(|V|\cdot |E|)
Are vertices x and y adjacent| 	O(|V|) 				|O(1) 				|O(|E|)
Remarks 					|	Slow to remove vertices and edges, because it needs to find all vertices or edges | Slow to add or remove vertices, because matrix must be resized/copied | Slow to add or remove vertices and edges, because matrix must be resized/copied 

On utilisera la liste d'adjacence pour sa rapidité à l'insertion.