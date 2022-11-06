class Connection:
    def __init__(self, *, raw_data: dict):
        self.id: int = raw_data["id"]
        self.name: str = raw_data["name"]
        self.type: str = raw_data["type"]
        self.verified: bool = bool(raw_data["verified"])
        self.friend_sync: bool = bool(raw_data["friend_sync"])
        self.show_activity: bool = bool(raw_data["show_activity"])
        self.two_way_link: bool = bool(raw_data["two_way_link"])
        self._visibility: bool = bool(raw_data["visibility"])

    @property
    def visible(self) -> bool:
        """returns true if its visible to everyone
        returns false if its invisible to everyone except the user themselves
        """
        return bool(self._visibility)
