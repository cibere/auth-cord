from typing import Union


class Email:
    def __init__(self, *, verified: bool, email: str):
        self.verified: bool = verified
        self.email: str = email

    def __str__(self):
        return self.email


class PartialUser:
    email: Union[Email, None]

    def __init__(self, *, raw_data: dict):
        self.id: int = int(raw_data["id"])
        self.name: str = raw_data["username"]
        self.discriminator: int = int(raw_data["discriminator"])
        self.locale: Union[str, None] = raw_data.get("locale")

        self.bot: bool = bool(raw_data.get("bot", False))
        self.system: bool = bool(raw_data.get("system", False))
        self.mfa_enabled: bool = bool(raw_data.get("mfa_enabled", False))

        self._banner_id: str = raw_data.get("banner", None)
        self._avatar_id: str = raw_data.get("avatar", None)
        self._accent_color: Union[int, None] = raw_data.get("accent_color")
        if raw_data.get("email") is not None:
            self.email = Email(
                verified=raw_data.get("verified", False), email=raw_data["email"]
            )
        else:
            self.email = None

        self._premium_type: int = raw_data.get("premium_type", 0)
        self.nitro_type = self.premium_type

    @property
    def premium_type(self):
        x = {0: None, 1: "Classic", 2: "Regular", 3: "Basic"}
        return x[self._premium_type]

    @property
    def banner_url(self):
        return f"https://cdn.discordapp.com/banners/{self.id}/{self._banner_id}.png"

    @property
    def accent_color(self):
        if self._accent_color:
            return int(self._accent_color)
        else:
            return None

    @property
    def avatar_url(self):
        return f"https://cdn.discordapp.com/avatars/{self.id}/{self._avatar_id}.png"

    @property
    def username(self):
        return self.name

    def __str__(self):
        return f"{self.name}#{self.discriminator}"
