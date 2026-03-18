from rich.console import Console
import time

console = Console()

console.print("Booting system...", justify="center")
time.sleep(1)

console.print("Loading modules...", justify="center")
time.sleep(1)

console.print("[bold green]System Ready[/]", justify="center")