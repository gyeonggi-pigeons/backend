from os import getenv
import json

OPENAI_API_KEY = getenv("OPENAI_API_KEY")
OPENAI_ASSISTANT_ID = getenv("OPENAI_ASSISTANT_ID")

# Database Config
USE_CUSTOM_DB = bool(getenv("USE_CUSTOM_DB", False))
CUSTOM_DB_ENGINE = getenv(
    "CUSTOM_DB_ENGINE", "django.db.backends.mysql")
CUSTOM_DB_NAME = getenv("CUSTOM_DB_NAME", "django")
CUSTOM_DB_USER = getenv("CUSTOM_DB_USER", "django")
CUSTOM_DB_PASSWORD = getenv("CUSTOM_DB_PASSWORD", "django")
CUSTOM_DB_HOST = getenv("CUSTOM_DB_HOST", "db")
CUSTOM_DB_PORT = getenv("CUSTOM_DB_PORT", "3306")
CUSTOM_DB_OPTIONS = json.loads(
    getenv(
        "CUSTOM_DB_OPTIONS",
        '{"charset":"utf8mb4","ssl_mode":"DISABLED"}'))

# CSRF Config
CSRF_TRUSTED_ORIGINS = getenv(
    "CSRF_TRUSTED_ORIGINS", "http://localhost:8000").split(",")
