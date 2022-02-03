from ..__information__ import __version__


def print_help():
    return f"# richcat {__version__}"+"""
The `richcat` command supporting various types of files.

## USAGE
```js
richcat <OPTIONS> <FILE>
```

## ARGS
```js
<FILE>                      | 'File to print'
```

## OPTIONS
```js
-h, --help                  | 'Show help in English.'
                            |
-V, --version               | 'Show version.'
                            |
-t, --filetype <STRING>     | 'Specify file type.'
                            | 'e.g. --filetype=python'
                            |
-w, --width <INT or FLOAT>  | 'Set print width.'
                            | 'If width>1, set print width direct.'
                            | 'If width<1, set print width percent.'
                            |
-c, --color-system <STRING> | 'Choose color system.'
                            | ['standard', '256', 'truecolor', 'windows']
                            |
    --style <STRING>        | 'Set styles.'
                            | ['[no]header', '[no]pager']
                            | 'e.g. --style=header,nopager'
```
""", 'md', None
