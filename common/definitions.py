from dataclasses import dataclass, asdict
import random

INDEX_INT_AC = "intac"

__DEFAULT_DB_QUERY_QUESTIONS = [
    'Tell me something about internships?',
    'What are my recommended modules for the second semester?',
    'If I have a question regarding my curriculum, to whom should I reach out?',
]

def rand_q():
    return random.choice(__DEFAULT_DB_QUERY_QUESTIONS)

@dataclass
class MDFile:
    """Dataclass for storing content of a parsed md file."""
    title: str
    resource_path: str
    content: str

    # add a dict method to transfer to json.
    dict = asdict 
