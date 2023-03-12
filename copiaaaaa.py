import os
import shutil

directory = "/home/hugo/dev/Sotiris64.github.io/animations"

for x in os.walk(directory):
    try:
        shutil.copy(f"{x[0]}/scripts.js",
                        f"/home/hugo/dev/stuck_in_the_website/public/generative-art/{x[0].split('/')[-1].lower()}.js")
    except Exception as e:
        print(e)
