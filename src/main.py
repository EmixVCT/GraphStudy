#!/usr/bin/python3
# -*- coding: utf-8 -*-

import click
from graph import Graph, utils
from utils import debug,set_debug



# program arguments handling
def handleArgs(gen_graph, method, in_file, out_file,diameter,vertices,m):
	print("")

	if gen_graph:
		graph = utils.genRandomGraph(method,vertices,m)
		if graph:
			graph.print_graph()

			if out_file:
				graph.saveToAdjacentListCSV(out_file)

	if in_file:
		graph = Graph(path=in_file.name, name=in_file.name)
		if debug:
			graph.print_graph()
		graph.analisis(diameter)
	print("")



@click.command()
@click.option("--gen-graph", is_flag=True, help="Generate a graph (you can specify the method with --method)")
@click.option("--method", default="EG", type=click.Choice(['EG', 'BA'], case_sensitive=False), help="[with --gen-graph] Name if the generation method (EG for Edgar Gilbert, BA for Barabàsi-Albert)")
@click.option("--vertices", default=5, show_default=True, type=click.IntRange(2, 10000), help="[with --gen-graph] The numbers of vertices")
@click.option("--m", default=2, show_default=True, type=click.IntRange(2, 10000), help="[with --gen-graph] The numbers 'm' for Barabàsi-Albert graph generation")
@click.option("--out", type=click.File('w', lazy=False), help="[with --gen-graph] Path to the file of the generated graph")

@click.option("--debug", is_flag=True, help="[with --debug] Info will be print into the console")
@click.option("--diameter", is_flag=True, help="[with --diameter] analyze calcul the diameter of the graph")

@click.option("--analyze", type=click.File('rb', lazy=False), help="Path to the file of the graph")

def main(gen_graph, method, analyze, out,debug,diameter,vertices,m):
    """ Main program """
    
    set_debug(debug)
    handleArgs(gen_graph, method, analyze, out, diameter,vertices,m)

    return 0

if __name__ == "__main__":
    main()