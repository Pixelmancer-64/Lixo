import os

directory = "/home/hugo/dev/stuck_in_the_website/src/pages/generative-art"

for filename in os.listdir(directory):
    try:
        # print(filename)
        # os.create('/home/hugo/dev/stuck_in_the_website/public/generative-art/' + os.path.splitext(filename)[0])
        with open('/home/hugo/dev/stuck_in_the_website/src/content/generative_art/' + os.path.splitext(filename)[0] + '.md', 'w') as f:
            f.write('''
            ---
title: Yggdrasil project
publishDate: 2020-03-02 00:00:00
imgs:
  - /assets/stock-1.jpg
img_alt: Iridescent ripples of a bright blue and pink liquid
description: |
  Arcu dui vivamus arcu felis bibendum ut tristique et egestas. Eget gravida cum sociis natoque penatibus. Cras fermentum odio eu feugiat pretium nibh!
tags:
  - Design
  - Dev
  - User Testing
---


            ''')
    except Exception as e:
        print(e)
