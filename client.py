import json
import click
from rev_ai import apiclient
from decimal import getcontext, Decimal

def connect(access_token):
    return apiclient.RevAiAPIClient(access_token)

def get_jobs(revai, limit=1000, last_job='', per_minute=0.035):
    getcontext().prec = 2
    while True:
        jobs = revai.get_list_of_jobs(limit=2, starting_after = last_job)
        if not jobs:
            break
        for job in jobs:
            cost = Decimal(job.duration_seconds) / Decimal(60) * Decimal(per_minute)
            cost = float(cost)
            yield {
                'name': job.name,
                'id': job.id,
                'created_on': job.created_on,
                'duration_seconds': job.duration_seconds,
                'cost': cost
            }
            last_job = job.id
