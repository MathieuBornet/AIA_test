import pyfiglet
from argparse import ArgumentParser, Namespace


def generate_ascii_art(text: str, font: str = "standard") -> str:
    if not text:
        raise ValueError("Le texte ne peut pas être vide.")
    try:
        return pyfiglet.figlet_format(text, font=font)
    except pyfiglet.FontNotFound as e:
        raise ValueError(f"La police '{font}' n'existe pas.") from e

if __name__ == "__main__":
    parser = ArgumentParser(description="Générateur d'ASCII Art")
    parser.add_argument("text", type=str, help="Le texte à convertir en ASCII Art")
    parser.add_argument("--font", type=str, default="standard", help="La police de caractères à utiliser (par défaut : standard)")
    args: Namespace = parser.parse_args()

    try:
        ascii_art = generate_ascii_art(args.text, args.font)
        print(ascii_art)
    except ValueError as e:
        print(e)