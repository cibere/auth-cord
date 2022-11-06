class HTTPError(Exception):
    def __init__(self, text: str):
        super().__init__(text)
