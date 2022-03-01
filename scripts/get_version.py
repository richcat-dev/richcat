import re

with open('./richcat/__information__.py', 'r') as f:
    init_text = f.read()
    _version = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    print(_version)
