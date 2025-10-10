import os, shutil
from dotenv import load_dotenv

load_dotenv()

my_path = os.getenv("DOWNLOADS_PATH")
move_to_vids = os.getenv("DESTINATION_PATH_VIDS")
move_to_pics = os.getenv("DESTINATION_PATH_PICS")
move_to_docs = os.getenv("DESTINATION_PATH_DOCS")
move_to_audio = os.getenv("DESTINATION_PATH_AUDIO")

os.makedirs(move_to_vids, exist_ok=True)


def move_files():
    file = os.listdir(my_path)
    for f in file:
        dst = ""
        src = os.path.join(my_path, f)
        ext = os.path.splitext(f)[1].lower()
        if os.path.isdir(src):
            continue
        if ext in (".mp4", ".mov", ".avi"):
            dst = os.path.join(move_to_vids, f)

        elif ext in (".jpeg", ".png", ".webp", "jpg"):
            dst = os.path.join(move_to_pics, f)

        elif ext in (".docx", ".txt", ".json"):
            dst = os.path.join(move_to_docs, f)

        elif ext in (".mp3", ".wav", ".flac", ".ogg"):
            dst = os.path.join(move_to_audio, f)

        else:
            os.remove(src)

        try:
            shutil.move(src, dst)
        except Exception as e:
            print(e)


try:
    move_files()
    print("Done")

except Exception as e:
    print(e)
