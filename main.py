from colorama import Back, Fore, Style


def abort(message: str) -> None:
    print(f'{Back.BLACK}{Fore.RED}[ABORT] {message}{Style.RESET_ALL}')


def error(message: str) -> None:
    print(f'{Back.RED}{Fore.BLACK}[ERROR] {message}{Style.RESET_ALL}')


def system(message: str, end: str=' ') -> None:
    print(f'{Fore.CYAN}[SYSTEM] {message}{Style.RESET_ALL}{end}')


def warn(message: str) -> None:
    print(f'{Fore.LIGHTYELLOW_EX}[WARNING] {message}{Style.RESET_ALL}')


def done(end: str=' ') -> None:
    print(f'{Back.WHITE}{Fore.BLACK}[DONE]{Style.RESET_ALL}{end}')


def false() -> None:
    print(f'{Back.RED}{Fore.BLACK}[FALSE]{Style.RESET_ALL}')


def true() -> None:
    print(f'{Back.GREEN}{Fore.BLACK}[TRUE]{Style.RESET_ALL}')


if __name__ == '__main__':
    import sys
    if (len(sys.argv) == 4):
        locals()[sys.argv[1]](sys.argv[2], sys.argv[3])
    elif (len(sys.argv) == 3):
        locals()[sys.argv[1]](sys.argv[2])
    else:
        locals()[sys.argv[1]]()