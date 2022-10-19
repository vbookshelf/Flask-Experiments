
import os

image_list = os.listdir('static/tb_all_images/')

# Remove the '.DS_Store' file.
# Keep only the .png files
image_list = [x for x in image_list if x.split('.')[1] == 'png']



print(image_list)
print(len(image_list))




