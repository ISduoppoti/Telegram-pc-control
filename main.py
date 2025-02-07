import os

import telebot

# Info field --

BOT_API_KEY = "api_key"

with open("access.txt", "r") as file:
    CHAT_ID = [line.strip() for line in file]

bot = telebot.TeleBot(BOT_API_KEY)

# Bot notify on startup --

bot.send_message(chat_id=CHAT_ID, text=f"I am awake")

# Bot commands --


@bot.message_handler(commands=["id"])
def show_id(message):
    bot.send_message(message.chat.id, f"Ur chat_id: {message.chat.id}")


@bot.message_handler(commands=["shutdown", "shtdwn", "shd", "sd", "sh", "s"])
def shutdown(message):
    if not check_acces(message):
        bot.send_message(message.chat.id, "You dont have acces")
        return 0

    bot.send_message(message.chat.id, "Proceeding")
    execute_command("shutdown")


def check_acces(message):
    global CHAT_ID
    return True if message.chat.id in CHAT_ID else False


# Main functions --


def execute_command(action):
    if action == "shutdown":
        os.system("shutdown -s -t 1")

    else:
        result = subprocess.run(action, shell=True, capture_output=True, text=True)
        return f"Cmd: {result.stdout}" if result.stdout else f"CmdErr: {result.stderr}"


def server_program():
    bot.polling(none_stop=True)


if __name__ == "__main__":
    server_program()
