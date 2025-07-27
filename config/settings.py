
from pydantic import BaseSettings

class Settings(BaseSettings):
    base_url: str
    ssh_host: str
    ssh_user: str
    ssh_password: str

    class Config:
        env_file = ".env"
