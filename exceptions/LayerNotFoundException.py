class LayerNotFoundException(Exception):
    def __init__(self):
        message = "Layer not found"
        print(message)
        super().__init__(message)
