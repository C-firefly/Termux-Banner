#!/usr/bin/env python3

import os
import time
import json
import shutil
import subprocess

from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table

console = Console()

HOME = str(Path.home())

# -------- PATHS --------

BANNER_DIR = os.path.join(HOME, ".my_bin/Banner")
PY_BANNER_DIR = os.path.join(BANNER_DIR, "python_banners")

MY_BIN = os.path.join(HOME, ".my_bin")

TERMUX_BANNER = os.path.join(BANNER_DIR, "termux-banner.py")

DEMO_BANNER = os.path.join(BANNER_DIR, "demo_banner.py")

BANNER_JSON = os.path.join(BANNER_DIR, "banners.json")

# -------- FOLDER SETUP --------

def create_folders():

    os.makedirs(BANNER_DIR, exist_ok=True)
    os.makedirs(MY_BIN, exist_ok=True)

# এখানে যেসব ফাইল/ফোল্ডার মুভ করতে চাও তাদের নাম রাখো
FILES = [
    "setup-banner.py",
    "banners.json",
    "demo_banner.py",       
    "python_banners"           # ফোল্ডার
]

def move_selected_files():
    current = os.getcwd()

    for item in FILES:
        src = os.path.join(current, item)
        dst = os.path.join(BANNER_DIR, item)

        if not os.path.exists(src):
            console.print(f"[yellow]Skipping {item}, not found in current directory[/yellow]")
            continue
        # যদি আগেই destination থাকে, remove করে তারপর move কর
        if os.path.exists(dst):
            if os.path.isfile(dst) or os.path.islink(dst):
                os.remove(dst)
            else:
                shutil.rmtree(dst)

        shutil.move(src, dst)
        console.print(f"[green]{item} moved successfully[/green]")


# -------- INSTALL RICH --------

def install_packages():

    try:
        import rich
    except ImportError:

        console.print("\n[bold yellow]Installing Rich Library...[/bold yellow]\n")

        subprocess.run(["pip", "install", "rich"])
        subprocess.run(["pkg", "install", "toilet"])
        subprocess.run(["pkg", "install", "figlet"])


# -------- AUTOSTART --------

def activate_banner():

        block = """
        # TERMUX BANNER
        if [ -f ~/.my_bin/Banner/termux-banner.py ]; then
        python ~/.my_bin/Banner/termux-banner.py
        fi
        """

    for rc in [".bashrc", ".zprofile"]:

        path = os.path.join(HOME, rc)

        if os.path.exists(path):

            with open(path) as f:
                content = f.read()

            if "termux-banner.py" not in content:

                with open(path, "a") as f:
                    f.write(block)


# -------- REMOVE --------

def remove_banner():

    if os.path.exists(TERMUX_BANNER):
        os.remove(TERMUX_BANNER)

    block = "python ~/.my_bin/Banner/termux-banner.py"

    for rc in [".bashrc", ".zprofile"]:

        path = os.path.join(HOME, rc)

        if os.path.exists(path):

            with open(path) as f:
                lines = f.readlines()

            with open(path, "w") as f:
                for line in lines:
                    if block not in line:
                        f.write(line)

    console.print("\n[bold red]Banner removed completely[/bold red]\n")


# -------- PYTHON BANNERS --------

def python_banners():

    files = os.listdir(PY_BANNER_DIR)

    banners = [
        f for f in files
        if f.startswith("default_banner_") and f.endswith(".py")
    ]
    
    banners = sorted(
        banners,
        key=lambda x: int(x.split("_")[-1].split(".")[0])
    )

    if not banners:

        console.print("[bold red]No Python banners found[/bold red]")

        return


    console.print(
        Panel.fit(
            "[bold cyan]Python Banner Preview[/bold cyan]"
        )
    )

    for i, banner in enumerate(banners, 1):

        console.print(f"\n[bold yellow]{i}. {banner}[/bold yellow]\n")

        path = os.path.join(PY_BANNER_DIR, banner)

        os.system(f"python {path}")

    console.print("\n[bold green]Select banner number[/bold green]", end=" ")

    choice = input()

    if choice.isdigit():

        index = int(choice) - 1

        if index < len(banners):

            src = os.path.join(PY_BANNER_DIR, banners[index])

            shutil.copy(src, TERMUX_BANNER)

            activate_banner()

            console.print(
                "\n[bold green]Banner Installed Successfully[/bold green]"
            )


# -------- ASCII BANNERS --------

def ascii_banners():

    if not os.path.exists(BANNER_JSON):
        console.print("[bold red]banners.json missing[/bold red]")
        return

    with open(BANNER_JSON) as f:
        data = json.load(f)

    banners = data["banners"]

    console.print(Panel.fit("[bold magenta]ASCII Banner Preview[/bold magenta]"))

    for i, banner in enumerate(banners, 1):
        console.print(f"\n[bold yellow] Banner {i}[/bold yellow]\n")
        console.print(banner)

    console.print("\n[bold green]Select banner number[/bold green]", end=" ")
    choice = input()

    if choice.isdigit():

        index = int(choice) - 1

        if index < len(banners):

            banner_text = banners[index]

            block = f"\nBANNER = r'''{banner_text}'''\nprint_banner()\n"

            shutil.copy(DEMO_BANNER, TERMUX_BANNER)

            with open(TERMUX_BANNER, "a") as f:
                f.write(block)

            activate_banner()

            console.print("\n[bold green]Banner Installed Successfully[/bold green]")


# -------- CUSTOM --------

def custom_banner():

    console.print(
        Panel.fit(
            "[bold cyan]Paste Your ASCII Banner\nPress ENTER twice to finish[/bold cyan]"
        )
    )

    lines = []

    while True:

        line = input()

        if line == "":

            break

        lines.append(line)

    banner = "\n".join(lines)

    block = f"\nBANNER = r'''{banner}'''\nprint_banner()\n"
    
    shutil.copy(DEMO_BANNER, TERMUX_BANNER)

    with open(TERMUX_BANNER, "a") as f:

        f.write(block)

    activate_banner()

    console.print("\n[bold green]Custom Banner Installed[/bold green]")


# -------- UI --------

def banner_menu():

    console.print(
        Align.center(
            Panel.fit("[bold green]TERMUX BANNER MANAGER[/bold green]")
        )
    )

    table = Table(show_header=False)

    table.add_row("1", "Python Creative Banners")
    table.add_row("2", "Colourful ASCII Banners")
    table.add_row("3", "Custom ASCII Banner")
    table.add_row("4", "Remove Banner")
    table.add_row("5", "Exit")

    console.print(table)

    console.print("\n[bold cyan]Select Option[/bold cyan]", end=" ")

    choice = input()

    if choice == "1":
        python_banners()

    elif choice == "2":
        ascii_banners()

    elif choice == "3":
        custom_banner()

    elif choice == "4":
        remove_banner()

    elif choice == "5":
        return False

    return True

# -------- MAIN --------

def main():

    os.system("clear")

    install_packages()
    
    create_folders()
    if not os.path.exists (TERMUX_BANNER):
        move_selected_files()

    while True:

        os.system("clear")

        run = banner_menu()

        if not run:
            break

        console.print("\n[dim]Press Enter to continue...[/dim]")
        input()


if __name__ == "__main__":

    main()
