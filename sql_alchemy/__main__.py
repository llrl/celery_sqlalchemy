import argparse

from .app import run

parser = argparse.ArgumentParser(description='SQL Alchemy tutor')
parser.add_argument('run_type', type=str, default='run')

args = parser.parse_args()

if __name__ == '__main__':
    run(args)