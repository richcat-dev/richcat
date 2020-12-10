from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.panel import Panel
from rich.console import RenderGroup

console = Console()

text1 = """
import numpy as np
a = np.array([1,2,3,4,5])
a
"""
text1 = Panel(Syntax(text1, 'python', line_numbers=True))


text2 = """
```
array([1, 2, 3, 4, 5])
```
"""
text2 = Markdown(text2)


text3 = """
b
"""
text3 = Panel(Syntax(text3, 'python', line_numbers=True))


text4 = """
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-2-89e6c98d9288> in <module>
----> 1 b

NameError: name 'b' is not defined
"""
#  text4 = Markdown(text4)
text4 = Panel(Syntax(text4, 'python', line_numbers=True))

code1 = RenderGroup(
        "code:[1]",
        text1,
        "output:[1]",
        text2
        )
console.print(Panel(code1))
print()
code2 = RenderGroup(
        "code:[2]",
        text3,
        "output:[2]",
        text4
        )
console.print(Panel(code2))
