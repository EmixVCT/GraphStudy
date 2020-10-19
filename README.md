# GraphStudy
Etude de graphes du Web

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