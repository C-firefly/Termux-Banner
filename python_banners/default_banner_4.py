from rich.console import Console
import os

console = Console()

console.print("SYSTEM INFO", style="bold red", justify="center")

console.print(f"User : {os.getenv('USER')}", style="green", justify="center")
console.print(f"Home : {os.getenv('HOME')}", style="green", justify="center")