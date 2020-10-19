#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

def handleArgs(method, analyze):
	print(method)

@click.command()
@click.option("--gen-random-graph", default="EG", help="Name if the generation method (EG for Edgar Gilbert, BA for Barabàsi-Albert)")
@click.option("--analyze", help="Path to the file of the generated graph")
def main(gen_random_graph, analyze):
    """ Main program """

    handleArgs(gen_random_graph, analyze)

    return 0

if __name__ == "__main__":
    main()