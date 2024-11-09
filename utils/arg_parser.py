import argparse

def create_parser():
    parser = argparse.ArgumentParser(prog='github-activity', description='Simple CLI to get Git-hub user activity')
    parser.add_argument('github-activity', help='Get a Git-hub user activity')
    return parser