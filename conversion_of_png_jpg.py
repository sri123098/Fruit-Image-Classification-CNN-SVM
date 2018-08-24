from PIL import Image
import os
import glob

for fruit_dir_path in glob.glob("/Users/sriramreddy/Downloads/523/train/*"):
    fruit_label = fruit_dir_path.split("/")[-1]
    count=0
    for image_path in glob.glob(os.path.join(fruit_dir_path, "*.png")):
        im = Image.open(image_path)
        count+=1
        output=str(fruit_label)+"/"+str(count)+".jpg"
        if not im.mode == 'RGB':
            im = im.convert('RGB')
        im.save(output)
