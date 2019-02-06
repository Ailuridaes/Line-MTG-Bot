class GetCardError(Exception):
    def __init__(self, message='Unknown error'):
        self.message = message
