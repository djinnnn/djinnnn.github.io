#!/usr/bin/env python3
import sys
import re
import yaml

def parse_bibtex(content):
    entries = []
    # split entries by @ (skip leading text)
    parts = re.split(r"@(\w+)\s*\{", content)
    # parts: ['', type1, rest1, type2, rest2, ...] — not ideal; use finditer
    pattern = re.compile(r"@(?P<type>\w+)\s*\{\s*(?P<key>[^,]+),(?P<body>.*?)\n\}\s*", re.S)
    for m in pattern.finditer(content):
        entry_type = m.group('type')
        key = m.group('key').strip()
        body = m.group('body')
        fields = {}
        # find key = {value} or key = "value"
        field_pattern = re.compile(r"(?P<k>\w+)\s*=\s*(?:\{(?P<v1>.*?)\}|\"(?P<v2>.*?)\")\s*,?\s*\n", re.S)
        for fm in field_pattern.finditer(body + "\n"):
            k = fm.group('k').lower()
            v = fm.group('v1') if fm.group('v1') is not None else fm.group('v2')
            v = v.strip()
            fields[k] = v
        entries.append({'key': key, 'type': entry_type, **fields})
    return entries


def authors_to_string(a):
    # BibTeX authors often separated by ' and '
    return ' and '.join([x.strip() for x in re.split(r'\s+and\s+', a)])


def to_yaml_entries(entries):
    out = []
    for e in entries:
        title = e.get('title', '').strip('{}')
        authors = e.get('author', '')
        if authors:
            authors = authors_to_string(authors)
        year = e.get('year', '')
        venue = e.get('journal') or e.get('booktitle') or e.get('conference') or ''
        url = e.get('url') or e.get('doi') or ''
        out.append({
            'key': e.get('key',''),
            'title': title,
            'authors': authors,
            'year': year,
            'venue': venue,
            'url': url
        })
    # sort by year desc if possible
    try:
        out.sort(key=lambda x: int(x.get('year') or 0), reverse=True)
    except Exception:
        pass
    return out


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: bibtex_to_yaml.py input.bib output.yml")
        sys.exit(2)
    infile = sys.argv[1]
    outfile = sys.argv[2]
    with open(infile, 'r', encoding='utf-8') as f:
        c = f.read()
    entries = parse_bibtex(c)
    yaml_entries = to_yaml_entries(entries)
    with open(outfile, 'w', encoding='utf-8') as f:
        yaml.safe_dump(yaml_entries, f, allow_unicode=True, sort_keys=False)
    print(f"Wrote {len(yaml_entries)} entries to {outfile}")
