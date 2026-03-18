from rich.console import Console
from rich.text import Text
import os
import json
from pathlib import Path
import time

console = Console()

HOME = str(Path.home())
User_file = os.path.join(HOME, ".my_bin/User/user_info.json")

# load username
name = "User"
if os.path.exists(User_file):
    with open(User_file, "r") as f:
        data = json.load(f)
        name = data.get("username", "User")

os.system("clear")

# banner text with Rich markup
banner_lines = [
    "[bold red]╔════════════════════════════════════╗[/bold red]",
    "[bold orange1]║        TERMUX SECURE SYSTEM        ║[/bold orange1]",
    f"[bold yellow]║          USERNAME : {name}         ║[/bold yellow]",
    "[bold green]╚════════════════════════════════════╝[/bold green]",
]

# animate banner line by line
for line in banner_lines:
    console.print(line, justify="center")
    time.sleep(0.05)

console.print("\n[bold red][+] Security Layer Active[/bold red]\n")
console.print(f"[bold cyan][+] Welcome Back, {name}[/bold cyan]\n")