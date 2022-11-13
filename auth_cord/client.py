from typing import Optional

from aiohttp import ClientSession
from typing_extensions import Self

from .authorization import Authorization
from .connection import Connection
from .errors import HTTPError, check_for_errors
from .guild import PartialGuild
from .token import Token
from .user import PartialUser


class Client:
    _session: ClientSession
    _authorization: Authorization

    def __init__(self, authorization: Authorization):
        """Lets you create a client instance

        :authorization: an authorization object
        """
        self._authorization = authorization

    async def __aenter__(self) -> Self:
        await self.start()
        return self

    async def __aexit__(
        self, exception_type, exception_value, exception_traceback
    ) -> None:
        await self.close()

    async def start(self) -> None:
        """Starts the client"""

        self._session = ClientSession()

    async def close(self) -> None:
        """Closes the client"""

        await self._session.close()

    async def exchange_code(self, code: str) -> Token:
        """Exchanges an oauth2 code for a token

        :code: the code you got from oauth2
        """
        data = {
            "client_id": str(self._authorization.client_id),
            "client_secret": self._authorization.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self._authorization.redirect_url,
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        res = await self._session.post(
            self._authorization.api_endpoint + "/oauth2/token",
            data=data,
            headers=headers,
        )
        raw_data = await res.json()
        await check_for_errors(raw_data)
        token = raw_data["access_token"]

        token = Token(
            raw_data=raw_data, auth=self._authorization, session=self._session
        )
        return token

    async def get_user_connections(self, token: str) -> list[Connection]:
        """Get a users connections

        :token: the token you got from exchanging the oauth2 code
        """
        res = await self._session.get(
            f"{self._authorization.api_endpoint}/users/@me/connections",
            headers={"Authorization": f"Bearer {token}"},
        )
        data = await res.json()
        await check_for_errors(data)
        cons = []
        for con in data:
            cons.append(Connection(raw_data=con))
        return cons

    async def get_user_guilds(self, token: str) -> list[PartialGuild]:
        """Get a users guilds

        :token: the token you got from exchanging the oauth2 code
        """
        res = await self._session.get(
            f"{self._authorization.api_endpoint}/users/@me/guilds",
            headers={"Authorization": f"Bearer {token}"},
        )
        data = await res.json()

        await check_for_errors(data)
        guilds = []
        for guild in data:
            guilds.append(PartialGuild(raw_data=guild))
        return guilds

    async def get_user_info(self, token: str) -> PartialUser:
        """Get a users info

        :token: the token you got from exchanging the oauth2 code
        """
        res = await self._session.get(
            f"{self._authorization.api_endpoint}/users/@me",
            headers={"Authorization": f"Bearer {token}"},
        )
        data = await res.json()

        await check_for_errors(data)
        user = PartialUser(raw_data=data)
        return user
