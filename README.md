# LLYNX MARQO INSERTION

This is a util package for the llynx project (llm). These scripts can parse data from .md files & insert them into the `marqo` database.

Currently, we use the version 1.5.1 of the database (docker image) and version 2.1.0 of the marqo python client.

Might be necessary to update to version 2.0 in the future, but it seems that slightly changes to the python scripts need to be done.

The database url is contained in .env file which is loaded as env variable before executing db interactions.

## Installation

Create a python venv named 'env'

    python3 -m venv env

Activate:

    source env/bin/activate

Install requirements (mainly marqo from PyPI)

    pip install -r requirements.txt

In a terminal window, start the docker container & wait a few minutes until its finished:

    docker-compose -f docker-compose.marqo.yaml up

Then parse the files + insert them:

    python3 -m db insert 


## Query the db

### Python script

With activated python env, execute

    python3 -m db query "Here is my question"

It will return a list of entries from the db that matches to that question with a score between 1.0 and 0.0.


### curl (http request) 

Use curl to query in the database

```
curl -X POST 'http://localhost:8882/indexes/intac/search' -H 'Content-type:application/json' -d '
{
    "q": "what is the best outfit to wear on the moon?",
    "searchableAttributes": ["title", "content"],
    "limit": 10,
    "offset": 0,
    "showHighlights": true,
    "searchMethod": "TENSOR",
    "attributesToRetrieve": ["Title", "Description"]
}'
```