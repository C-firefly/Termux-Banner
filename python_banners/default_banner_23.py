from rich.console import Console
import platform

console = Console()

console.print("SYSTEM DASHBOARD", style="bold blue", justify="center")

console.print(f"OS : {platform.system()}", justify="center")
console.print(f"Arch : {platform.machine()}", justify="center")
console.print(f"Python : {platform.python_version()}", justify="center")