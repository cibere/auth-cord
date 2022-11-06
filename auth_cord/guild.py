class PartialGuild:
    def __init__(self, *, raw_data: dict):
        self.id: int = raw_data["id"]
        self.name: str = raw_data["name"]
        self.permissions: int = raw_data["permissions"]
        self.features: list[str] = raw_data["features"]

    def __str__(self):
        return self.name
