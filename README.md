![Python package](https://github.com/richcat-dev/richcat/workflows/Python%20package/badge.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4e61b411095d4d3292e2a3e169aa0f35)](https://app.codacy.com/gh/richcat-dev/richcat?utm_source=github.com&utm_medium=referral&utm_content=richcat-dev/richcat&utm_campaign=Badge_Grade)
[![Downloads](https://pepy.tech/badge/richcat)](https://pepy.tech/project/richcat)
# richcat
-   `richcat` is a `cat` command decorated by [rich](https://github.com/willmcgugan/rich) which is Python library.
-   Working on Python.

## Features

### Syntax hilighting
![image](https://user-images.githubusercontent.com/55144709/152114834-9172b501-269a-4044-9889-94c92346c5ff.png)

### Support viewer

#### Markdown
![image](https://user-images.githubusercontent.com/55144709/152116094-d20ea35a-5dbd-441c-b668-2a3f408caaaf.png)

#### CSV
![image](https://user-images.githubusercontent.com/55144709/152116330-e9a391a0-0491-4b3b-82f9-7a56e789a273.png)

### Automatic paging
By default, `richcat` pipes its own output to a pager. If you wouldn't rather pager, use `--style=nopager` option.

![image](https://user-images.githubusercontent.com/55144709/152116597-fdaca73f-9c0d-4b56-894c-e384dba84d96.png)
## Installation
```sh
pip install richcat
```

## Usage
Display a file contents on the terminal.
example:
```sh
richcat table.csv
```

Use `-t` option, you can choose highlight.
example:
```sh
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

## Contributors
-   [@yamamoto-yuta](https://github.com/yamamoto-yuta) (Maintainer, **main contributor!**)
-   [@ShotaroKataoka](https://github.com/ShotaroKataoka) (Maintainer)
