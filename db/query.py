import marqo
from common.definitions import INDEX_INT_AC
from common.get_client import get_client

def query_question(q):
    print(f"query_question(): {q=}")
    try:
        mq = get_client()
        results = mq.index(INDEX_INT_AC).search(q)
    except Exception as e:
        print("[ERROR]: The server might not be running or the index does not existst.")
    return results
