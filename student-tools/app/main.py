from rich.console import Console

from app.services.calculater import calculate_average
from app.utils.formatter import format_average


def main() -> None:
    values = [5, 4, 5, 3, 5]
    average = calculate_average(values)

    console = Console()
    console.print(f"[bold green]{format_average(average)}[/bold green]")


if __name__ == "__main__":
    main()
