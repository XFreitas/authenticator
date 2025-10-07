import time, pyotp, os
from dotenv import load_dotenv
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, BarColumn
from rich.console import Group
from rich.text import Text

load_dotenv()

SECRET_HCPA = str(os.getenv("SECRET_HCPA"))

console = Console()
totp = pyotp.TOTP(SECRET_HCPA)


def make_panel():
    """Cria o painel com o código atual e a barra de progresso."""
    current_code = totp.now()
    time_remaining = totp.interval - int(time.time()) % totp.interval

    progress = Progress(
        "[progress.description]{task.description}",
        BarColumn(),
        f"[progress.remaining]{time_remaining:>3.0f}s",
        console=console,
        transient=True,
    )

    progress.add_task(
        "Tempo restante", total=totp.interval, completed=totp.interval - time_remaining
    )

    text = Text.from_markup(
        f"[bold green]Código TOTP:[/bold green] [bold yellow]{current_code}[/bold yellow]"
    )

    render_group = Group(text, progress)

    panel = Panel(
        render_group,
        title="Autenticador HCPA",
        border_style="cyan",
    )
    return panel


def display_totp():
    """Atualiza o painel sem limpar o terminal."""
    with Live(make_panel(), console=console, refresh_per_second=4) as live:
        while True:
            time.sleep(0.25)
            live.update(make_panel())  # Atualiza o conteúdo do painel


def main():
    os.system("cls" if os.name == "nt" else "clear")
    try:
        display_totp()
    except KeyboardInterrupt:
        console.print("\n[bold red]Encerrado pelo usuário.[/bold red]")


if __name__ == "__main__":
    main()
