from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

I am the Master of Whisperers (like Varys in Game of Thrones).

You can use me to send whispers to your friend in groups and channels (even if I'm not there).
Only that friend and you will be able to read the message even though others are in same group. 

Use help command to know how to use me

By @Tellybotzz
    """

    home_buttons = [
        [
        InlineKeyboardButton('🔒 Send a Whisper 🔒', switch_inline_query=""),
        InlineKeyboardButton('🚴‍♂️ About', callback_data='about'),
        InlineKeyboardButton('♨️ Close', callback_data='close')
        ]
        ]

    # Rest Buttons
    buttons = [
        [
        InlineKeyboardButton('♻️ Update Channel', url='https://telegram.me/tellybotzz'),
        InlineKeyboardButton('💬 Developer', url='https://telegram.me/NitinSahay')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('♨️ Close', callback_data='close')
        ]
        ]


    # Help Message
    HELP = """
Just type the message in below format in any chat.

@Telly_WhisperBot your_message friend_username/id`
    """

    # About Message
    ABOUT = """
**About This Bot** 

Designed by @Tellybotzz

Source Code : [Click Here](https://t.me/tellybotzz)

Hosted on  : Vps

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @Tellybotzz
    """
