import re


class LogParser:
    def __init__(self, filename):
        self.filename = filename
        self.ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        self.error_pattern = r'\s(200|401|403|404|500)\s'
        self.method_url_pattern = r'"(GET|POST|PUT|DELETE|HEAD|OPTIONS|PATCH)\s([^"]+)\sHTTP/\d\.\d"'
        self.bot_pattern = r'(bot|Bot|BOT)'

    def read_file(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            return f.readlines()

    def extract_ips(self, lines):
        ips = []
        for line in lines:
            match = re.search(self.ip_pattern, line)
            if match:
                ips.append(match.group())
        return ips

    def extract_error_codes(self, lines):
        errors = []
        for line in lines:
            match = re.search(self.error_pattern, line)
            if match:
                errors.append(match.group(1))
        return errors

    def extract_method_url(self, lines):
        requests = []
        for line in lines:
            match = re.search(self.method_url_pattern, line)
            if match:
                requests.append((match.group(1), match.group(2)))
        return requests

    def extract_bot_requests(self, lines):
        bots = []
        for line in lines:
            if re.search(self.bot_pattern, line, re.IGNORECASE):
                bots.append(line.strip())
        return bots

    def print_results(self):
        lines = self.read_file()

        print("=" * 60)
        print("РЕЗУЛЬТАТЫ ПАРСИНГА ЛОГ-ФАЙЛА")
        print("=" * 60)

        ips = self.extract_ips(lines)
        print(f"\n1. IP-адреса ({len(ips)} шт.):")
        for ip in ips:
            print(f"{ip}")

        errors = self.extract_error_codes(lines)
        print(f"\n2. Коды ошибок ({len(errors)} шт.):")
        for error in errors:
            print(f"{error}")

        requests = self.extract_method_url(lines)
        print(f"\n3. Метод и URL ({len(requests)} шт.):")
        for method, url in requests:
            print(f"{method} {url}")

        bots = self.extract_bot_requests(lines)
        print(f"\n4. Запросы от ботов ({len(bots)} шт.):")
        for bot in bots:
            print(f"{bot}")

        print("\n" + "=" * 60)


parser = LogParser("input.txt")
parser.print_results()