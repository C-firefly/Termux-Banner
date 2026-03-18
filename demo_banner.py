from rich.text import Text
import os
import json
from pathlib import Path
import time
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table


console = Console()

HOME = str(Path.home())
User_file = os.path.join(HOME, ".my_bin/User/user_info.json")

# load username
name = "USER"
banner = "TERMUX"
if os.path.exists(User_file):
    with open(User_file, "r") as f:
        data = json.load(f)
        name = data.get("username", "USER")
        banner = data.get("title", "TERMUX")

os.system("clear")

def print_banner():

    os.system("clear")

    console.print(
        Align.center(
            Panel(BANNER)
        )
    )

