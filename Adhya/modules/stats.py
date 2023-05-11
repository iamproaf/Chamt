from pyrogram import filters
from pyrogram.types import Message

from Adhya import OWNER, adhya
from Adhya.database.chats import get_served_chats
from Adhya.database.users import get_served_users


@adhya.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(cli: adhya, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ {(await cli.get_me()).mention} :

➻ **ᴄʜᴀᴛs :** {chats}
➻ **ᴜsᴇʀs :** {users}"""
    )
