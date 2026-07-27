from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    app_name : str
    app_env : str
    debug : bool
   
    database_host : str 
    database_name : str
    database_port : int
    database_user : str
    database_password : str
    database_url : str
    
    model_config = SettingsConfigDict(
        env_file  = '.env',
        env_file_encoding = 'utf-8',
        case_sensitive =  False,
        extra = 'ignore'
    )

@lru_cache
def get_Settings() -> Settings:
    return Settings()

Settings = get_Settings()