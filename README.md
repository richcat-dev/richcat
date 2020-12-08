[![Downloads](https://pepy.tech/badge/richcat)](https://pepy.tech/project/richcat)
# richcat
- `richcat` is a `cat` command decorated by [rich](https://github.com/willmcgugan/rich) which is Python library.
- Working on Python.

## Features

### Syntax hilighting
![](doc/img/index-html.jpg)

### Support viewer

#### Markdown
![](doc/img/sample-md.jpg)

#### CSV
![](doc/img/table-csv.jpg)

### Automatic paging
By default, `richcat` pipes its own output to a pager. If you wouldn't rather pager, use `--disable-pager` option.

## Installation
```
$ pip install richcat
```

## Usage
Display a file contents on the terminal.
```
$ richcat README.md
```

Use `-t` option, you can choose highlight.
```
$ richcat README.md -t text
```

# Contributors!
- [@yamamoto-yuta](https://github.com/yamamoto-yuta) (Maintainer, **main contributor!**)
- [@ShotaroKataoka](https://github.com/ShotaroKataoka) (Maintainer)
