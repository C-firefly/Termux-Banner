from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="TOOL STATUS")

table.add_column("Module", justify="center")
table.add_column("Status", justify="center")

table.add_row("Scanner", "Ready")
table.add_row("Network", "Online")
table.add_row("System", "Active")

console.print(table, justify="center")