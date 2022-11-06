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
        token = await client.exchange_code("...")

        # getting the users connections
        user = await client.get_user_info(
            token.token
        )  # 'token' is a 'discord_oauth.token.Token' object

        # printing the users id
        print(user.id)


# checking if this file is the one that was run
if __name__ == "__main__":
    # if so, run the main function
    asyncio.run(main())
