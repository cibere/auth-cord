<h1 align="center">Auth Cord</h1>
<p align="center">
<a href="https://discord.gg/pP4mKKbRvk"><img src="https://discord.com/api/guilds/986344051110473769/embed.png" alt="discord"></a>
<a href="https://pypi.org/project/auth-cord"><img src="https://img.shields.io/pypi/v/auth-cord.svg" alt="pypi"></a>
<a href="https://github.com/cibere/auth-cord/blob/main/LICENSE"><img src="https://img.shields.io/github/license/cibere/auth-cord" alt="license"></a>
</p>
<p align="center">Python Wrapper for discords oauth2</p>

<h2>Key Features</h2>
Support for the following endpoints<br>
 - exchange code for token<br>
 - refresh token<br>
 - get user connections<br>
 - get user guilds<br>
 - get user info<br>

<h2>Installing</h2>
<span style="font-weight: bold;">Python 3.8 or higher is required</span>
Install from pip

```
python -m pip install -U auth-cord
```

Install from github

```bash
python -m pip install -U git+https://github.com/cibere/auth-cord # requires git to be installed
```

<h2>FAQ</h2>

> Q: I don't have a webserver, can I still use discords oauth?<br>
> A: Yes! You can set the redirect_url to `https://api.cibere.dev/auth_cord`, and tell the user to give your bot the given code.<br>

<h2>Examples</h2>
Get user info

```py
import asyncio

import auth_cord

# creating our authorization object
auth = auth_cord.Authorization(
    client_id=123,
    client_secret="...",
    redirect_url="...",
)

# creating our client instance and passing our authorization
client = auth_cord.Client(authorization=auth)


async def main():
    # starting our client
    async with client:
        # exchanging our code with discord for a token
        token = await client.exchange_code("...")

        # getting the users connections
        user = await client.get_user_info(
            token.token
        )  # 'token' is a 'auth_cord.token.Token' object

        # printing the users id
        print(user.id)


# checking if this file is the one that was run
if __name__ == "__main__":
    # if so, run the main function
    asyncio.run(main())

```

See <a href="https://github.com/cibere/auth-cord/tree/main/examples">the examples folder</a> for a full list of examples
