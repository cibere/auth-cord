from typing import Optional


class Authorization:
    def __init__(
        self,
        *,
        client_id: Optional[int] = None,
        client_secret: Optional[str] = None,
        redirect_url: Optional[str] = None,
        discord_api_version: Optional[int] = 10,
    ):
        self.api_endpoint = f"https://discord.com/api/v{discord_api_version}"
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_url = redirect_url
