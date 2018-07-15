import better_exceptions
import os
import glob
from PIL import Image

files = glob.glob('crawled_images/ISSEY_MIYAKE_femme/*.jpg')
a = 0
for f in files:
    a += 1
    img = Image.open(f)
    # img_resize = img.resize((183, 275))
    # img_resize = img.resize((100, 150))
    # img_resize = img.resize((70, 105))
    # img_resize = img.resize((70, 70))
    img_resize = img.resize((128, 128))
    # img_resize = img.resize((683, 1024))
    ftitle, fext = os.path.splitext(f)
    # img_resize.save('resized_images/20180714_183x275/' + str(a) + '_(183x275)' + fext)
    # img_resize.save('resized_images/20180714_70x105/' + str(a) + '_(70x105)' + fext)
    # img_resize.save('resized_images/20180714_70x70/' + str(a) + '_(70x70)' + fext)
    img_resize.save('resized_images/20180714_128x128/' + str(a) + '_(128x128)' + fext)
    # img_resize.save('resized_images/20180715_683x1024/' + str(a) + '_(683x1024)' + fext)
    print(a, end=", ")

