![Python package](https://github.com/richcat-dev/richcat/workflows/Python%20package/badge.svg)
[![codecov](https://codecov.io/gh/richcat-dev/richcat/branch/main/graph/badge.svg?token=X3MXTFVWD5)](https://codecov.io/gh/richcat-dev/richcat)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4e61b411095d4d3292e2a3e169aa0f35)](https://app.codacy.com/gh/richcat-dev/richcat?utm_source=github.com&utm_medium=referral&utm_content=richcat-dev/richcat&utm_campaign=Badge_Grade)
[![Downloads](https://pepy.tech/badge/richcat)](https://pepy.tech/project/richcat)

# richcat

- `richcat` is a `cat` command decorated by [rich](https://github.com/willmcgugan/rich) which is Python library.
- Working on Python.

## Features

### Syntax hilighting

![image](https://user-images.githubusercontent.com/55144709/152114834-9172b501-269a-4044-9889-94c92346c5ff.png)

### Support viewer

| Markdown                                                                                                        | CSV                                                                                                             | Jupyter Notebook                                                                                                |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| ![image](https://user-images.githubusercontent.com/55144709/152116094-d20ea35a-5dbd-441c-b668-2a3f408caaaf.png) | ![image](https://user-images.githubusercontent.com/55144709/152116330-e9a391a0-0491-4b3b-82f9-7a56e789a273.png) | ![image](https://user-images.githubusercontent.com/55144709/154985162-d177e0ac-4f26-47e2-a49b-5008883e541f.png) |

### Automatic paging

By default, `richcat` pipes its own output to a pager. If you wouldn't rather pager, use `--style=nopager` option.

![image](https://user-images.githubusercontent.com/55144709/152116597-fdaca73f-9c0d-4b56-894c-e384dba84d96.png)

### Support Python import

Import on Python console:

![image](https://user-images.githubusercontent.com/55144709/154991230-006518c7-f5a4-43c4-82f4-3390d84eb64d.png)

Import on Jupyter Lab:

![image](https://user-images.githubusercontent.com/55144709/154992180-07477488-c2d5-4e72-acbe-1954171d589a.png)

## Installation

```
pip install richcat
```

## Usage

Display a file contents on the terminal.

example:

```
richcat table.csv
```

Use `-t` option, you can choose highlight.

example:

```
richcat table.csv -t text
```

Use `--style=header` option if you use the header in a CSV file.

example:

```sh
richcat table.csv --style=header
```

| `--style=noheader` (default)                                                                                    | `--style=header`                                                                                                |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| ![image](https://user-images.githubusercontent.com/55144709/152151519-a95c262d-9074-47f2-ada8-b5dae6a4866c.png) | ![image](https://user-images.githubusercontent.com/55144709/152151220-9e7e8829-109e-42ed-ad78-96f145fbf222.png) |

If you want to use `richcat` in Python, you can use the following example.

example:

```python
>>> from richcat import richcat
>>> richcat("table.csv")
```

## Options

The options that can be specified in `richcat` are as follows:

| option                          | explanation                                                                                          | example                     |
| ------------------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------- |
| `-h`, `--help`                  | Show help in English.                                                                                |
| `-V`, `--version`               | Show version.                                                                                        |
| `-t`, `--filetype <STRING>`     | Specify file type.                                                                                   | `--filetype python`         |
| `-w`, `--width <INT or FLOAT>`  | Set print width. <br> If width>1, set print width direct. <br> If width<1, set print width percent.' | `--width 80`, `--width 0.5` |
| `-c`, `--color-system <STRING>` | Choose color system. <br> ['standard', '256', 'truecolor', 'windows']                                |
| `--style <STRING>`              | Set styles. <br> ['[no]header', '[no]pager']                                                         | `--style=header,nopager`    |

## Development

If you want to develop richcat, please follow the steps below.

1. Build the development environment.

```
$ git clone git@github.com:richcat-dev/richcat.git
$ docker-compose build
```

2. Start the development environment.

```
$ docker-compose up -d
```

3. Go inside the launched Docker container to develop.

```
$ docker exec -it <CONTAINER_ID> /bin/bash
```

You can view the API document of richcat under development at the following URL.

- http://localhost:8000/

You can update `richcat` API documentation with the following command.

```
$ cd ~
$ make sphinx-apidoc
```

## Contributors

- [@yamamoto-yuta](https://github.com/yamamoto-yuta) (Maintainer, **main contributor!**)
- [@ShotaroKataoka](https://github.com/ShotaroKataoka) (Maintainer)
