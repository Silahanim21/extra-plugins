# Zorunlu gereklidir. Eklemek istediğin bilgileri burda belirt çekinme 😏

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    TOKEN = os.environ.get("TOKEN", "")