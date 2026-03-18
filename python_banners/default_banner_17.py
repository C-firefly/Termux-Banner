from rich.console import Console
import pyfiglet

console = Console()

banner = pyfiglet.figlet_format("HACKER")

console.print(banner, style="bold green", justify="center")
console.print("[red]Access Granted[/]", justify="center")