from pyrogram.types import Chat


def get_chat_id(chat: Chat):
    if chat.title.startswith("Channel Music: ") and chat.title[1:].isnumeric():
        return int(chat.title[1:])
    return chat.id
