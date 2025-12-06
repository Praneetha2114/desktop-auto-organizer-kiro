import os
import shutil

DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")

FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Archives": [".zip", ".rar"]
}

def organize_desktop():
    for file in os.listdir(DESKTOP):
        filepath = os.path.join(DESKTOP, file)

        if os.path.isfile(filepath):
            ext = os.path.splitext(file)[1].lower()

            moved = False
            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    dest_folder = os.path.join(DESKTOP, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(filepath, dest_folder)
                    moved = True
                    break

            if not moved:
                misc = os.path.join(DESKTOP, "Misc")
                os.makedirs(misc, exist_ok=True)
                shutil.move(filepath, misc)

if __name__ == "__main__":
    organize_desktop()
    print("Desktop organized successfully!")
