<h1 align="center">Discord Oauth</h1>
<p align="center">
<a href="https://discord.gg/pP4mKKbRvk"><img src="https://discord.com/api/guilds/986344051110473769/embed.png" alt="discord"></a>
<a href="https://pypi.org/project/ciberedev.py"><img src="https://img.shields.io/pypi/v/ciberedev.py.svg" alt="pypi"></a>
<a href="https://github.com/cibere/ciberedev.py/blob/main/LICENSE"><img src="https://img.shields.io/github/license/cibere/ciberedev.py" alt="license"></a>
</p>
<p align="center">Python Wrapper for discords oauth2</p>

<h2>Key Features</h2>
Support for the following endpoints<br>
 - exchange code for token
 - refresh token
 - get user connections
 - get user guilds
 - get user info

<h2>Installing</h2>
<span style="font-weight: bold;">Python 3.8 or higher is required</span>
Install from pip

```
python -m pip install -U discord-oauth
```

Install from github

```bash
python -m pip install -U git+https://github.com/cibere/discord-oauth # requires git to be installed
```

<h2>FAQ</h2>

> Q: I don't have a webserver, can I still use discords oauth?
> A: Yes! You can set the redirect_url to `https://api.cibere.dev/discord_oauth`, and tell the user to give your bot the given code.

<h2>Examples</h2>
Get user info

```py
import asyncio
import ciberedev

client = ciberedev.Client()

async def main():
  async with client:
    paste = await client.create_paste("my_paste_text")
    print(paste.url)

if __name__ == "__main__":
  asyncio.run(main())
```

See <a href="https://github.com/cibere/ciberedev.py/tree/main/examples">the examples folder</a> for a full list of examples
