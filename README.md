#  Desktop Auto Organizer — Kiro Lazy Automation Challenge (Week 2)

A simple automation that cleans and organizes a messy Windows Desktop in seconds.  
Built as part of the **Kiro Heroes Week 2 Challenge — Lazy Automation**.

---

##  Problem

My desktop gets cluttered every single day with screenshots, images, PDFs, and random files.  
Cleaning it manually wastes time and quickly becomes frustrating.

So I decided:

> **"I hate organizing my messy desktop, so I built this automation."**

---

## Solution

A Python automation script that:

- Scans the Windows Desktop  
- Detects file types  
- Automatically creates folders like:  
  - `Images/`  
  - `Documents/`  
  - `Videos/`  
  - `Archives/`  
  - `Misc/`  
- Moves files into the right categories  
- Cleans the entire desktop in seconds  

---

##  How Kiro Helped

Kiro made development faster and simpler by helping me:

- Validate the file-system logic step by step  
- Quickly fix bugs during testing  
- Avoid manually building boilerplate code  
- Experiment with extensions and conditions easily  
- Run the workflow directly inside the Kiro environment  

This reduced development time and helped me focus purely on the automation logic.

---

## How It Works

Run this in Command Prompt:

```bash
cd Desktop
python organize_desktop.py
```

Or:

```bash
py organize_desktop.py
```

After execution, your desktop automatically organizes itself into clean folders.

---

## Script (organize_desktop.py)

```python
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
```

---

## Demo Screenshots

###  Before Automation (Messy Desktop)
*File: `demo/before_desktop.png`*

### Kiro Script View
*File: `demo/kiro_script.png`*

### After Automation (Organized Desktop)
*File: `demo/after_desktop.png`*

---

##  Project Structure

```
desktop-auto-organizer-kiro/
 ├── .kiro/
 │     └── .gitkeep
 ├── demo/
 │     ├── before_desktop.png
 │     ├── kiro_script.png
 │     └── after_desktop.png
 ├── organize_desktop.py
 └── README.md
```

---

##  Final Notes

This automation demonstrates how Kiro simplifies scripting and accelerates real-world automation workflows.  
A boring daily chore becomes a single command — clean, organized, and efficient.

---

##  AWS Builder Center Blog

Blog Link: https://builder.aws.com/content/36T34DKXHeGez94jPNfi52qbljx/i-hate-organizing-my-messy-desktop-so-i-built-this-automation-using-kiro

