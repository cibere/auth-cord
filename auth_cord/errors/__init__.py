from .http import *


class InvalidAuthorization(Exception):
    def __init__(self):
        super().__init__("Invalid Authorization was given")


class InvalidRedirectURL(Exception):
    def __init__(self, text: str):
        super().__init__("Invalid redirect_url was given")


ERRORS = {"URL_TYPE_INVALID_URL": InvalidRedirectURL}


async def check_for_errors(data: dict):
    if isinstance(data, list):
        return
    keys = data.keys()

    if "error" in keys:
        raise HTTPError(data["error_description"])

    elif "errors" in keys:
        for error in data["errors"].keys():
            eh = data["errors"][error]["_errors"][0]
            error = ERRORS.get(eh["code"], HTTPError)
            raise error(eh["message"])
    elif data.get("message") == "401: Unauthorized":
        raise HTTPError("401: Unauthorized")
