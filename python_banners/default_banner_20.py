from rich.console import Console
import random
import time

console = Console()

chars = "01"

for i in range(15):
    line = "".join(random.choice(chars) for _ in range(40))
    console.print(line, style="green", justify="center")
    time.sleep(0.05)