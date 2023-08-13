import os

# In case we are not in the production environment, load the environment variables
try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    pass
else:
    load_dotenv()

# Notion API
NOTION_API_TOKEN = os.getenv('NOTION_API_TOKEN')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

# Weather API
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

# Google Calendar API
# You might have more complex configuration for Google's API, such as client ID and secret
GOOGLE_CALENDAR_CREDENTIALS = os.getenv('GOOGLE_CALENDAR_CREDENTIALS')

# Other configuration settings can be added as needed
