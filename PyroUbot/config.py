import os

DEVS = [
    940035839,
]

API_ID = int(os.getenv("API_ID", "27087758"))

API_HASH = os.getenv("API_HASH", "2ef578f901d8ab62b58e03db98533747")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6508893003:AAGAlMAutCimwEBachNZOZuaPVPCJgVbB90")

OWNER_ID = int(os.getenv("OWNER_ID",  "1321036212"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002044156039"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001538826310 -1001462256506 -1001812143750 -1002012397923 -1001812143750 -1001964273937 -1002006883687 -1001951721136 -1002045881007 -1001986858575 -1002044156039 -1001974313872 ").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "20"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
)

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://zyric:1234@cluster0.bophvmo.mongodb.net/?retryWrites=true&w=majority",
)

