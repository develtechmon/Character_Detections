import keras_ocr
import matplotlib.pyplot as plt
import os

path = os.getcwd() + "/Keras_OCR_Text_Detections/Images/"

pipeline = keras_ocr.pipeline.Pipeline()

'''Using Local Image Type'''
images = [
    keras_ocr.tools.read(img) for img in [path + 'image_2.jpg',
                                          path + 'image_1.jpg',]
]

'''Using URL Type'''
# images = [
#     keras_ocr.tools.read(url) for url in [
#         'https://storage.googleapis.com/gcptutorials.com/examples/keras-ocr-img-1.jpg',        
#         'https://storage.googleapis.com/gcptutorials.com/examples/keras-ocr-img-2.png'
#     ]
# ]

print(images[0])
print(images[1])
                           
prediction_groups = pipeline.recognize(images)

fig, axs = plt.subplots(nrows=len(images), figsize=(10, 20))

for ax, image, predictions in zip(axs, images, prediction_groups):
    keras_ocr.tools.drawAnnotations(image=image, 
                                    predictions=predictions, 
                                    ax=ax)
predicted_image_1 = prediction_groups[0]
for text, box in predicted_image_1:
    print(text)

predicted_image_2 = prediction_groups[1]
for text, box in predicted_image_2:
    print(text)
