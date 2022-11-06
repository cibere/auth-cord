import asyncio

import discord_oauth

# creating our authorization object
auth = discord_oauth.Authorization(
    client_id=123,
    client_secret="...",
    redirect_url="...",
)

# creating our client instance and passing our authorization
client = discord_oauth.Client(authorization=auth)


async def main():
    # starting our client
    async with client:
        # exchanging our code with discord for a token
        old_token = await client.exchange_code("...")

        # refreshing the token
        new_token = await old_token.refresh()

        # printing the new token
        print(new_token.token)


# checking if this file is the one that was run
if __name__ == "__main__":
    # if so, run the main function
    asyncio.run(main())
