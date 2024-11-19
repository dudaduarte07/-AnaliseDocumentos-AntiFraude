import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPPPOINT = os.getenv("ENDPOINT")
    KEY = os.getenv("SUBUSCRIPTION_KEY")
    AZURE_STORAGE_CONNECTION_STRING = os.getenv ("AZURE_STORAGE_CONNECTION_STRING")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")

    