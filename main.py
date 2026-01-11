import os
import shutil
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DOWNLOADS_PATH: str
    DESTINATION_PATH_VIDS: str
    DESTINATION_PATH_PICS: str
    DESTINATION_PATH_DOCS: str
    DESTINATION_PATH_AUDIO: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()  # ty:ignore[missing-argument]

my_path = settings.DOWNLOADS_PATH
move_to_vids = settings.DESTINATION_PATH_VIDS
move_to_pics = settings.DESTINATION_PATH_PICS
move_to_docs = settings.DESTINATION_PATH_DOCS
move_to_audio = settings.DESTINATION_PATH_AUDIO


def move_files():
    file = os.listdir(my_path)
    for f in file:
        dst = ""
        src = os.path.join(my_path, f)
        ext = os.path.splitext(f)[1].lower()
        if os.path.isdir(src):
            continue
        if ext in (".mp4", ".mov", ".avi", ".flv"):
            dst = os.path.join(move_to_vids, f)

        elif ext in (".jpeg", ".png", ".webp", "jpg"):
            dst = os.path.join(move_to_pics, f)

        elif ext in (".docx", ".txt", ".json", ".iso", ".pdf"):
            dst = os.path.join(move_to_docs, f)

        elif ext in (".mp3", ".wav", ".flac", ".ogg"):
            dst = os.path.join(move_to_audio, f)

        else:
            os.remove(src)

        try:
            shutil.move(src, dst)
        except Exception as e:
            print(e)

    print("Done")


move_files()
