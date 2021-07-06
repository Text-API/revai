#!/usr/bin/env python3

import os
import json
import click
import client
from dotenv import load_dotenv

load_dotenv()

@click.command()
@click.argument('access_token', envvar='REVAI_ACCESS_TOKEN')
def cli(access_token):
    api = client.connect(access_token)
    data  = list(client.get_jobs(api))
    print(json.dumps(data))

if __name__ == '__main__':
    cli()
