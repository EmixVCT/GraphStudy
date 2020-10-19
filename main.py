#!/usr/bin/env python
# -*- coding: utf-8 -*-

@click.command()
@click.option("--gen-random-graph", default=1, help="Name if the generation method (EG for Edgar Gilbert, BA for Barabàsi-Albert)")
@click.option("--analyze", help="Path to the file of the generated graph")
def main():
    """ Main program """

    handleArgs()

    return 0

if __name__ == "__main__":
    main()