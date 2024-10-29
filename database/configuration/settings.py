from pydantic_settings import BaseSettings


class ServerDBSettings(BaseSettings):
    PUBLIC_URL: str = "postgresql://postgres:CDeZtnMWtFNwHLLzfBpluTdPtbcjUirY@junction.proxy.rlwy.net:11495/railway"
