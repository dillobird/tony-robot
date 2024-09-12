import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# STEP 1: LOAD TOKEN
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

# STEP 2: BOT SETUP
intents = Intents.default()
intents.message_content = True # NOQA
client = Client(intents=intents)


# STEP 3: START UP
@client.event
async def on_ready() -> None:
    print(f'{client.user} is running!')


# STEP 4: HANDLE INCOMING MESSAGES
@client.event
async def on_message(message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = str(message.content)
    channel: str = str(message.channel)

    if not user_message:
        print('Message cannot be empty')
        return

    print(f'[{channel}] {username}: "{user_message}"')

    bot_message = get_response(user_message)

    await send_message(message, bot_message)


# STEP 5: MESSAGE
async def send_message(message, bot_message) -> None:
    try:
        await message.channel.send(bot_message)
    except Exception as e:
        print(e)

# STEP 6: MAIN ENTRY POINT
def main() -> None:
    client.run(TOKEN)

if __name__ == '__main__':
    main()