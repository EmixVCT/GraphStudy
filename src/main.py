#!/usr/bin/python3
# -*- coding: utf-8 -*-

import click
from graph import Graph, utils

# program arguments handling
def handleArgs(gen_graph, method, in_file, out_file):
	print("")
	if gen_graph:
		graph = utils.genRandomGraph(method)
		if graph:
			graph.print_graph()

			if out_file:
				graph.saveToAdjacentListCSV(out_file)

	if in_file:
		graph = Graph(path=in_file.name, name=in_file.name)
		graph.print_graph()
		graph.analisis()
	print("")



@click.command()
@click.option("--gen-graph", is_flag=True, help="Generate a graph (you can specify the method with --method)")
@click.option("--method", default="EG", type=click.Choice(['EG', 'BA'], case_sensitive=False), help="[with --gen-graph] Name if the generation method (EG for Edgar Gilbert, BA for Barabàsi-Albert)")
@click.option("--out", type=click.File('w', lazy=False), help="[with --gen-graph] Path to the file of the generated graph")

@click.option("--analyze", type=click.File('rb', lazy=False), help="Path to the file of the graph")

def main(gen_graph, method, analyze, out):
    """ Main program """

    handleArgs(gen_graph, method, analyze, out)

    return 0

if __name__ == "__main__":
    main()