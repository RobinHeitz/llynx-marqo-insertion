import pathlib
from common.definitions import MDFile

def parse_md_content(data_path:pathlib.Path) -> list[MDFile]:
    """Parses content from all md files within a sub-dir."""
    files = _search_md_files(data_path)
    md_files = []
    
    for f in files:
        title, content = _read_md_files(f)
        md_file = MDFile(title, str(f), content)
        md_files.append(md_file)
    return md_files


def _read_md_files(p:pathlib.Path):
    title = _parse_md_doc_title(p)
    text = _parse_md_file(p)
    return title, text


def _parse_md_doc_title(path:pathlib.Path):
    with open(path, 'r') as f:
        for line in f:
            if 'title' in line:
                return line.split(':')[1].strip()


def _parse_md_file(path:pathlib.Path) -> str:
    with open(path, 'r') as f:
        lines = f.readlines()
        lines = lines[5:]
        lines = [l.strip() for l in lines]
        lines = [l.replace('*', '') for l in lines]
        lines = [l for l in lines if l != '']
        lines = [l for l in lines if l != '\n']
        lines = [l for l in lines if l[0] != '#']
        lines = [l for l in lines if l[0] != '-']
        lines = [l for l in lines if l[0] != '>']
        lines = [l.strip() for l in lines]
    return ' '.join(lines).strip()


def _search_md_files(search_path: pathlib.Path):
    for p in search_path.rglob('*.md'):
        yield p
