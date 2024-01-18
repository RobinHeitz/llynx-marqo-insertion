from pathlib import Path
import argparse
from parser.parse_md import parse_md_content
from db.insert import insert_data
from db.query import query_question
from common.definitions import INDEX_INT_AC, rand_q

def insert(**kwargs):
    path = Path(__file__).parent.parent / 'example_data'
    data = parse_md_content(path)
    insert_data(data)
    

def query(**kwargs):
    q = kwargs.get('question')
    result = query_question(q)
    for r in result['hits']:
        print('----')
        print(r)
        print('\n'*2)



    

FUNCTION_MAP = {'insert': insert, 'query': query}

if __name__ == '__main__':
    ...
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=FUNCTION_MAP.keys())
    parser.add_argument('question', nargs='?', help="Question to query for. Only in command 'query'.", type=str, default=rand_q())
    args = parser.parse_args()

    func = FUNCTION_MAP[args.command]
    func(**vars(args))
