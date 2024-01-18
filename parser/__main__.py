import pathlib
from parser.parse_md import parse_md_content
from common.definitions import MDFile

if __name__ == "__main__":
    data_path = pathlib.Path(__file__).parent.parent.parent / 'example_data' 
    
    md_files = parse_md_content(data_path)

    for d in md_files:
        print(d.dict())