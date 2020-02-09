#!/usr/bin/env python

import click

@click.command()
@click.option('--name', help='print things that do not begin with p')

def namep(name):
    if not name.startswith('p'):
        print(f"{name}")

if __name__ == '__main__':
    namep()


