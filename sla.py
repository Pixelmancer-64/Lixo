from PIL import Image, ImageDraw

use_luminosity = True

dim = (1920,1080)

img = Image.new('RGB', dim)
draw = ImageDraw.Draw(img)

xstart = -.776707
ystart = -.134663

a = []

xd = 1.6 / 8192 / dim[0]
yd = 0.9 / 8192 / dim[1]

for x in range(dim[0]):
  for y in range(dim[1]):
    z = d = complex(xstart + x*xd, ystart + y*yd)
    c = 0
    while abs(z) < 2 and c < 5000:
      z = z*z + d
      c += 1
    a += [(c, -abs(z), x, y)]

a = a[1:]
a.sort(reverse = True)

t = [(i>>16, 255&i>>8, 255&i) for i in range(1, dim[0]*dim[1])]
if use_luminosity:
  t.sort(key = lambda c: c[0]*3 + c[1]*10 + c[2], reverse = True)

r = 0
for c,d,x,y in a:
  draw.point((x,y), t[r])
  r += 1

img.save('sla.png')