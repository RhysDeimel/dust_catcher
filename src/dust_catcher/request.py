class Request:
    def __init__(self, data):
        self.method = None
        self.headers = None

        self._parse_message(data)

    def _parse_message(self, data):
        d = [str(line, "utf-8").strip() for line in data]

        self.method = d[0].split(" ")[0]

        headers = [line.split(": ", maxsplit=1) for line in d[1:-1]]
        self.headers = dict(headers)
