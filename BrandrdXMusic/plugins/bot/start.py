import time
import asyncio
import io
import sys
import traceback
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

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
from config import BANNED_USERS, SUDO_USERS # Make sure to define SUDO_USERS in your config.py
from strings import get_string

@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    await message.react("❤")
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            await message.reply_sticker("CAACAgUAAxkBAAEQI1RlTLnRAy4h9lOS6jgS5FYsQoruOAAC1gMAAg6ryVcldUr_lhPexzME")
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
            query = f"https://www.youtube.com/watch?v={query}"
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
            lol = await message.reply_text("𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ︎ {}.. ❣️".format(message.from_user.mention))
            await lol.edit_text("𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ {}.. 🥳".format(message.from_user.mention))
            await lol.edit_text("𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ {}.. 💥".format(message.from_user.mention))
            await lol.edit_text("𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ {}.. 🤩".format(message.from_user.mention))
            await lol.edit_text("𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ {}.. 💌".format(message.from_user.mention))
            await lol.edit_text("𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐛𝐲 ꨄ {}.. 💞".format(message.from_user.mention))
               
            await lol.delete()
            lols = await message.reply_text("**⚡️ѕ**")
            await asyncio.sleep(0.1)
            await lols.edit_text("⚡ѕт")        
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтα**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαя**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαят**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαяι**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαятιи**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαятιиg**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ѕтαятιиg.**")

            await lols.edit_text("**⚡ѕтαятιиg....**")

            await lols.edit_text("**⚡ѕтαятιиg.**")
            await lols.edit_text("**⚡ѕтαятιиg....**")
            m = await message.reply_sticker("CAACAgUAAxkBAAEQI1BlTLmx7PtOO3aPNshEU2gCy7iAFgACNQUAApqMuVeA6eJ50VbvmDME")
            if message.chat.photo:

                userss_photo = await app.download_media(
                    message.chat.photo.big_file_id,
                )
            else:
                userss_photo = "assets/nodp.png"
            if userss_photo:
                chat_photo = userss_photo
            chat_photo = userss_photo if userss_photo else config.START_IMG_URL 

        except AttributeError:
            chat_photo = "assets/nodp.png"
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
                            f"https://t.me/{app.username}?start=sudolist",
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


# --- New Functionalities Start Here ---

@app.on_message(filters.command("eval") & filters.user(SUDO_USERS))
async def eval_executor(client, message: Message):
    """
    Executes Python code provided in the message.
    This command is restricted to SUDO_USERS only.
    Usage: /eval print("Hello World")
    """
    if len(message.command) < 2:
        return await message.reply_text("Please provide code to execute.")
    
    try:
        cmd = message.text.split(" ", 1)[1]
    except IndexError:
        return await message.reply_text("Please provide code to execute.")

    if message.from_user.id != (await client.get_me()).id:
        status_message = await message.reply_text("Executing...")
    else:
        status_message = await message.edit("Executing...")
        
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    
    try:
        exec(
            "async def __ex(client, message): "
            + " ".join("\n " + line for line in cmd.split("\n"))
        )
        result = await locals()["__ex"](client, message)
    except Exception:
        e = traceback.format_exc()
        return await status_message.edit(f"**Error:**\n`{e}`")

    stdout = redirected_output.getvalue()
    sys.stdout = old_stdout
    
    output = ""
    if stdout:
        output += f"**Stdout:**\n`{stdout}`\n"
    if result is not None:
        output += f"**Result:**\n`{result}`"
        
    if not output:
        output = "Code executed successfully with no output."
        
    await status_message.edit(output)


@app.on_message(filters.command("keyboard") & ~BANNED_USERS)
@LanguageStart
async def show_keyboard(client, message: Message, _):
    """
    Displays an example inline keyboard with two buttons.
    """
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Button 1",
                    callback_data="button1_pressed"
                ),
                InlineKeyboardButton(
                    text="Button 2 (URL)",
                    url=config.SUPPORT_CHAT
                ),
            ]
        ]
    )
    await message.reply_text(
        "Here is an example keyboard:",
        reply_markup=keyboard,
    )

@app.on_message(filters.command("custompost") & filters.user(SUDO_USERS)) # Restrict to SUDO_USERS
async def custom_post_with_keyboard(client, message: Message):
    """
    Ek custom formatted post inline keyboard ke saath bhejta hai.
    Command format: /custompost <photo_url> | <caption_text> | <group_button_text> | <group_url> | <channel_button_text> | <channel_url>
    Example: /custompost https://example.com/image.jpg | This is a test post. | My Group | https://t.me/my_group | My Channel | https://t.me/my_channel
    """
    if len(message.command) < 2:
        return await message.reply_text(
            "Usage: `/custompost <photo_url> | <caption_text> | <group_button_text> | <group_url> | <channel_button_text> | <channel_url>`"
            "\nExample: `/custompost https://example.com/image.jpg | This is a test post. | My Group | https://t.me/my_group | My Channel | https://t.me/my_channel`"
        )

    try:
        # Split the command arguments by '|'
        parts = message.text.split(" ", 1)[1].split("|")
        if len(parts) != 6:
            return await message.reply_text(
                "Invalid format. Please use: `<photo_url> | <caption_text> | <group_button_text> | <group_url> | <channel_button_text> | <channel_url>`"
            )

        photo_url = parts[0].strip()
        caption_text = parts[1].strip()
        group_button_text = parts[2].strip()
        group_url = parts[3].strip()
        channel_button_text = parts[4].strip()
        channel_url = parts[5].strip()

    except IndexError:
        return await message.reply_text("Invalid command format.")

    # --- Inline Keyboard ---
    keyboard = InlineKeyboardMarkup(
        [
            # Pehli Row (Group Button)
            [
                InlineKeyboardButton(
                    text=group_button_text,
                    url=group_url
                ),
            ],
            # Doosri Row (Channel Button)
            [
                InlineKeyboardButton(
                    text=channel_button_text,
                    url=channel_url
                )
            ]
        ]
    )

    # --- Post Bhejna ---
    try:
        await message.reply_photo(
            photo=photo_url,
            caption=caption_text,
            reply_markup=keyboard,
        )
        await message.reply_text("Custom post sent successfully!")
    except Exception as e:
        await message.reply_text(f"Failed to send custom post: `{e}`")