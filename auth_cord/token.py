from aiohttp import ClientSession
from typing_extensions import Self

from .authorization import Authorization


class Token:
    def __init__(self, *, raw_data: dict, auth: Authorization, session: ClientSession):
        self._authorization = auth
        self._session = session
        self.token: str = raw_data["access_token"]
        self._refresh_token: str = raw_data["refresh_token"]
        self.expires: int = raw_data["expires_in"]
        self.scopes: list[str] = raw_data["scope"].split(" ")

    def __str__(self):
        return self.token

    async def refresh(self):
        """refreshes the token"""
        data = {
            "client_id": str(self._authorization.client_id),
            "client_secret": self._authorization.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": self._refresh_token,
            "redirect_uri": self._authorization.redirect_url,
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        res = await self._session.post(
            self._authorization.api_endpoint + "/oauth2/token",
            data=data,
            headers=headers,
        )

        raw_data = await res.json()
        token = raw_data["access_token"]

        token = Token(
            raw_data=raw_data, auth=self._authorization, session=self._session
        )
        return token
