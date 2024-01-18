import marqo
from marqo.errors import MarqoWebError

from common.definitions import MDFile, INDEX_INT_AC
from common.get_client import get_client


def insert_data(data: list[MDFile]):
    mq = get_client()
    try:
        mq.delete_index(INDEX_INT_AC)
    except Exception as e:
        print("[ERROR]: Cannot delete index.", e)
    finally:
        mq.create_index(INDEX_INT_AC)
        print("Added new index: ", INDEX_INT_AC)
    try:

        mq.index(INDEX_INT_AC).add_documents([d.dict() for d in data], tensor_fields=['title', 'resource_path', 'content'])

    except MarqoWebError as e:
        print(f"[WebError]: ", e.status_code, "Is the server running?", type(e))
        return
