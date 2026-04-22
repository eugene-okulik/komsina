import os
import argparse
from datetime import datetime
from colorama import init, Fore, Style

# python3 analyzer.py /Users/tanya/PycharmProjects/komsina/homework/eugene_okulik/data/logs --text WARN
# python3 analyzer.py /Users/tanya/PycharmProjects/komsina/homework/eugene_okulik/data/logs --text WARN --first
# python3 analyzer.py /Users/tanya/PycharmProjects/komsina/homework/eugene_okulik/data/logs --text "Sql exception for geometry"

init(autoreset=True)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Full path to the directory or file with logs')
    parser.add_argument('--text', required=True, help='Text to find in logs')
    parser.add_argument('--first', action='store_true', help='Show only first match')
    return parser.parse_args()


def get_date_from_line(line):
    if len(line) >= 23:
        try:
            datetime.fromisoformat(line[:23].replace(',', '.'))
            return line[:23]
        except ValueError:
            pass
    return None


def get_context(text, search_text, words_around=5):
    words = text.split()
    search_lower = search_text.lower()
    idx = next((i for i, w in enumerate(words) if search_lower in w.lower()), None)
    if idx is None:
        return text[:50] + '...'
    start = max(0, idx - words_around)
    end = min(len(words), idx + words_around + 1)
    snippet = words[start:end]
    highlighted = [
        Fore.RED + w + Style.RESET_ALL if search_lower in w.lower() else w
        for w in snippet
    ]
    return ' '.join(highlighted)


def main():
    args = parse_args()
    search_text = args.text

    if os.path.isdir(args.path):
        files = sorted([
            os.path.join(args.path, f)
            for f in os.listdir(args.path)
            if os.path.isfile(os.path.join(args.path, f))
        ])
    elif os.path.isfile(args.path):
        files = [args.path]
    else:
        print(f'Ошибка: путь не найден: {args.path}')
        return

    found = False
    for file in files:
        data = {}
        current_key = None
        try:
            with open(file, encoding='utf-8', errors='replace') as f:
                for line in f:
                    date = get_date_from_line(line)
                    if date:
                        current_key = date
                        data[current_key] = line.strip()
                    elif current_key:
                        data[current_key] += ' ' + line.strip()

            for timestamp, block in data.items():
                if search_text.lower() in block.lower():
                    context = get_context(block, search_text)
                    print(
                        f'В файле {os.path.basename(file)}, время создания: {timestamp}')
                    print(f'найдено: ...{context}...')
                    print('-' * 40)
                    found = True
                    if args.first:
                        return

        except Exception as e:
            print(f'Не удалось прочитать файл {file}: {e}')

    if not found:
        print(f'Текст "{search_text}" не найден.')


main()
