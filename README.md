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
	--method [EG|BA]	  [with --gen-graph] Name if the generation method (EG for
						Edgar Gilbert, BA for Barabàsi-Albert)
	--out FILENAME		   [with --gen-graph] Path to the file of the generated
						graph

	--debug              Info will be print into the console

	--analyze FILENAME	Path to the file of the graph to analyze

	--diameter           [with --analyze] Compute the diameter of the graph

	--help			      Show this message and exit.
```

### Examples
- Generate a graph with Barabàsi-Albert method and store it :
`python3 ./src/main.py --gen-graph --method BA --out ba_graph.csv`
- Analyse it :
`python3 ./src/main.py --analyze ./ba_graph.csv`
Informations on the graph should be printed on your terminal, and you can find more results in the pdf report generated for you (for this example it should be ./ba_graph-report.pdf)

- To see debug message in your console :
`python3 ./src/main.py --analyze ./ba_graph.csv --debug`

- If you want to calculate the diameter of the graph :
`python3 ./src/main.py --analyze ./ba_graph.csv --diameter`
Be careful this operation can take a lot of time

## About the storage of the generated graphs

(https://www.wikiwand.com/en/Graph_(abstract_data_type)#/Representations)
with |V | the number of vertices and |E | the number of edges

								|	Adjacency list	|Adjacency matrix	|Incidence matrix
------------------------|-----------------|-----------------|----------------
Store graph 				|	O(|V|+|E|)		|	O(|V|^2) 		|O(|V|·|E|)
Add vertex 					|	O(1)				|	O(|V|^2)			|O(|V|·|E|)
Add edge 					|	O(1) 				|	O(1) 				|O(|V|·|E|)
Remove vertex 				|	O(|E|) 			|	O(|V|^2) 		|O(|V|·|E|)
Remove edge 				|	O(|V|) 			|	O(1) 				|O(|V|·|E|)
Are vertices x and y adjacent| 	O(|V|) 	|	O(1) 				|O(|E|)
Remarks 						|	Slow to remove vertices and edges, because it needs to find all vertices or edges | Slow to add or remove vertices, because matrix must be resized/copied | Slow to add or remove vertices and edges, because matrix must be resized/copied

We will use an adjacency list for it's insertion operation efficiency.
