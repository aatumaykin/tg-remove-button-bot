from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')

LOG_LEVEL = env.log_level("LOG_LEVEL")
ADMIN_USER = env.int('ADMIN_USER')
