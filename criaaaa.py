import os

directory = "/home/hugo/dev/stuck_in_the_website/src/pages/generative-art"

for filename in os.listdir(directory):
    try:
        # print(filename)
        os.create('/home/hugo/dev/stuck_in_the_website/public/generative-art/' + os.path.splitext(filename)[0])
        # with open('/home/hugo/dev/stuck_in_the_website/src/content/generative_art/' + os.path.splitext(filename)[0] +'.md', 'w') as f:
            # pass
    except Exception as e:
        print(e)
