from datetime import timedelta

from .constants import DIVIDER


def print_header(title: str):
    """Imprime um cabeçalho padronizado."""

    print()
    print(DIVIDER)
    print(title)
    print(DIVIDER)


def format_duration(milliseconds: int) -> str:
    """
    Converte milissegundos para um formato legível.

    Exemplo:
    189477 -> 3m 09s
    """

    total_seconds = int(milliseconds / 1000)

    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)

    if hours:
        return f"{hours}h {minutes}m {seconds}s"

    return f"{minutes}m {seconds}s"


def format_total_time(milliseconds: int) -> str:
    """
    Converte muitos milissegundos para:

    40 dias 23 horas 21 minutos
    """

    seconds = int(milliseconds / 1000)

    td = timedelta(seconds=seconds)

    days = td.days

    hours, remainder = divmod(td.seconds, 3600)

    minutes, _ = divmod(remainder, 60)

    return f"{days} dias {hours} horas {minutes} minutos"


def format_date(timestamp):
    """
    Formata um Timestamp do pandas.
    """

    return timestamp.strftime("%d/%m/%Y %H:%M:%S")