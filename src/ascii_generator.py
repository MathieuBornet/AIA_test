from pyfiglet import Figlet
import argparse

def generate_ascii(text: str, font: str = 'standard') -> str:
    f = Figlet(font=font)
    try:
        return f.renderText(text)
    except ValueError as e:
        raise ValueError(f'Font '{font}' not found. Available fonts: {Figlet().getFonts()}') from e

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate ASCII art from text.')
    parser.add_argument('text', type=str, help='The text to convert to ASCII art.')
    parser.add_argument('--font', type=str, default='standard', help='The font to use for the ASCII art (default: standard).')
    args = parser.parse_args()

    try:
        ascii_art = generate_ascii(args.text, args.font)
        print(ascii_art)
    except ValueError as e:
        print(e)