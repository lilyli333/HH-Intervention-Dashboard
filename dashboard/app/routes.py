from flask import render_template
from app import app
import numpy as np
import glob

@app.route('/')
@app.route('/index')

# def load_images():
#     path = glob.glob("/static/")
#     images = []
#     for file in path:   
#         image = np.load(file)
#         image = image['x']
#         image = image.astype(np.float32)
#         img_max = np.amax(image)
#         img_min = np.amin(image)
#         image = (image-img_min)/(img_max-img_min)
#         image = skimage.transform.resize(image,(image_size, image_size),order=3)
#         image = image.reshape(image.shape[0],image.shape[1],1)
#         images.append(image)
#         label = np.zeros(len(classes))
#         label[index] = 1.0
#         labels.append(label)
#         flbase = os.path.basename(fl)
#         img_names.append(flbase)
#     images = np.array(images)
#     return images

def index():
    images = [
        "http://content.presspage.com/uploads/1763/1920_year-of-the-bird-george-grall.jpg?10000",
        "https://upload.wikimedia.org/wikipedia/commons/3/32/House_sparrow04.jpg",
        "http://content.presspage.com/uploads/1763/1920_year-of-the-bird-george-grall.jpg?10000",
        "https://upload.wikimedia.org/wikipedia/commons/3/32/House_sparrow04.jpg"
    ]
    # images = load_images()
    return render_template('index.html', title='Home', images=images)