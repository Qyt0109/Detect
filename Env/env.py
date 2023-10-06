from dotenv import dotenv_values

# Load environment variables from .env file
server_env_vars = dotenv_values()

# Access environment variables
# Specify the path and name of the SQLite database file
db_path = server_env_vars.get('DB_PATH')
db_engine = server_env_vars.get('DB_ENGINE')
font_path = server_env_vars.get('FONT_PATH')
server_url = server_env_vars.get('SERVER_URL')
device_id = server_env_vars.get('DEVICE_ID')
api_server_url = server_env_vars.get('API_SERVER_URL')