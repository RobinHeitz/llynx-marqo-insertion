import marqo
from dotenv import load_dotenv
import os 

def get_client() -> marqo.Client:
    load_dotenv()
    url = os.getenv("MARQO_DB_URL")
    client = marqo.Client(url=url)
    return client
   
    