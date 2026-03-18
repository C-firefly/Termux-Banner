from rich.console import Console
import time

console = Console()

frames = [
"[bold green]Loading .[/]",
"[bold green]Loading ..[/]",
"[bold green]Loading ...[/]"
]

for i in range(3):
    for frame in frames:
        console.print(frame, justify="center")
        time.sleep(0.4)
        #console.clear()

console.print("[bold cyan]SYSTEM READY[/]", justify="center")