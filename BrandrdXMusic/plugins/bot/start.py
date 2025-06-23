import time
import asyncio
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from BrandrdXMusic import app
from BrandrdXMusic.misc import _boot_
from BrandrdXMusic.plugins.sudo.sudoers import sudoers_list
from BrandrdXMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from BrandrdXMusic.utils.decorators.language import LanguageStart
from BrandrdXMusic.utils.formatters import get_readable_time
from BrandrdXMusic.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string

# --- NEW STICKER FILE IDS ---
# Replace these with your desired sticker file IDs
WELCOME_STICKER_1 = "CAACAgUAAxkBAAEQI1RlTLnRAy4h9lOS6jgS5FYsQoruOAAC1gMAAg6ryVcldUr_lhPexzME" # Example existing, replace with yours
WELCOME_STICKER_2 = "CAACAgUAAxkBAAKktGhZgVvKBcruKFO1vrlyJyJ92u0BAAIPCQACSErxVkH9JWQPmfaoHgQ" # Placeholder, replace with actual
STARTING_STICKER_1 = "CAACAgUAAxkBAAKkw2hZgbt8t_FQU38s_k_8RZR3gsIiAAINFgAC0QyQVrqrLQzU13foHgQ" # Example existing, replace with yours
STARTING_STICKER_2 = "CAACAgUAAxkBAAKkyGhZghOqGIGtgP5HkY1Nyk_vfugyAAJ5CgACQgZwVTVo2eQqCh15HgQ" # Placeholder, replace with actual

@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    # Changed reaction to something more dynamic
    await message.react("✨") 
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            # Changed sticker to a new one for help
            await message.reply_sticker(WELCOME_STICKER_2) 
            return await message.reply_photo(
                photo=config.START_IMG_URL,
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"[https://www.youtube.com/watch?v=](https://www.youtube.com/watch?v=){query}"
            # This part uses `VideosSearch` which is not directly available here.
            # Assuming `VideosSearch` works as intended based on the original code.
            from youtubesearchpython.__future__ import VideosSearch # Ensure this import is available if not global
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
    else:
        try:
            out = private_panel(_)
            
            # --- Enhanced Welcome Animation ---
            welcome_messages = [
                "💫 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ︎ {}.. ❣️",
                "✨ 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ {}.. 🥳",
                "🎉 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ {}.. 💥",
                "🌟 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ {}.. 🤩",
                "💖 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ {}.. 💌",
                "💞 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ {}.. 🥰",
                "🎶 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ {}.. Enjoy!",
            ]
            
            # Send initial welcome message and animate
            lol = await message.reply_text(welcome_messages[0].format(message.from_user.mention))
            for i in range(1, len(welcome_messages)):
                await asyncio.sleep(0.3) # Slower animation for better readability
                await lol.edit_text(welcome_messages[i].format(message.from_user.mention))
            
            await asyncio.sleep(0.5) # Pause before starting animation
            await lol.delete() # Delete the animated welcome message

            # --- Dynamic Starting Text Animation ---
            starting_messages = [
                "⚡️ѕ", "⚡️ѕт", "⚡️ѕтα", "⚡️ѕтαя", "⚡️ѕтαят", "⚡️ѕтαятι", "⚡️ѕтαятιи", "⚡️ѕтαятιиg",
                "⚡️ѕтαятιиg.", "⚡️ѕтαятιиg..", "⚡️ѕтαятιиg...", "⚡️ѕтαятιиg....",
                "🎵 𝙻𝚘𝚊𝚍𝚒𝚗𝚐 𝙿𝚕𝚊𝚢𝚕𝚒𝚜𝚝𝚜...", "🚀 𝙱𝚘𝚘𝚝𝚒𝚗𝚐 𝚂𝚢𝚜𝚝𝚎𝚖𝚜...", "✅ 𝚁𝚎𝚊𝚍𝚢 𝚝𝚘 𝚁𝚘𝚌𝚔!"
            ]
            
            lols = await message.reply_text(starting_messages[0])
            for i in range(1, len(starting_messages)):
                await asyncio.sleep(0.15) # Slightly slower for more impact
                await lols.edit_text(starting_messages[i])

            await asyncio.sleep(0.5) # Pause after starting animation

            # --- Changed Sticker for starting animation ---
            m = await message.reply_sticker(STARTING_STICKER_2) # Using the new sticker ID
            
            userss_photo = None
            if message.chat.photo:
                try:
                    userss_photo = await app.download_media(
                        message.chat.photo.big_file_id,
                    )
                except Exception as e:
                    print(f"Error downloading chat photo: {e}")
                    userss_photo = None # Fallback if download fails
            
            chat_photo = userss_photo if userss_photo else config.START_IMG_URL # Use config.START_IMG_URL for global default

        except AttributeError:
            chat_photo = config.START_IMG_URL # Ensure it falls back to the configured URL

        await lols.delete()
        await m.delete()
        await message.reply_photo(
            photo=chat_photo,
            caption=_["start_2"].format(message.from_user.mention, app.mention),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.first_name
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} ʜᴀs sᴛᴀʀᴛᴇᴅ ʙᴏᴛ. \n\n**ᴜsᴇʀ ɪᴅ :** {sender_id}\n**ᴜsᴇʀ ɴᴀᴍᴇ:** {sender_name}",
            )

@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"[https://t.me/](https://t.me/){app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_3"].format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)







