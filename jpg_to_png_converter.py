import os
import sys
from PIL import Image


# this is the location of the folder of images that are to be converted 
img_location = sys.argv[1]  
# this is the location of the folder that stores the converted images 
converted_img_location = sys.argv[2]


try:
	# checking if folder that stores the converted images exists
	def check_folder():
		"""This function checks if folder exists and if does not exist it creates a new folder"""
		if os.path.exists(converted_img_location):
			converted_img_folder = converted_img_location
		else:
			# creating the folder to store converted images in the path provided by the user
			converted_img_folder = os.mkdir(converted_img_location)


	def image_conversion():
		"""This function converts the images and saves them to folder provided by user"""
		# listing all the images to be converted
		images = os.listdir(img_location)
		# retrieving each image and converting them to png
		for img in images:
			# path of the image to be converted
			img_path = os.path.join(img_location, img) 
			# name of the converted image
			img_name = (os.path.splitext(img)[0] + '.png')
			# opening the img to be converted
			img = Image.open(img_path)
			# path of the converted image
			converted_img_path = os.path.join(converted_img_location, img_name)
			# saving the converted image as png
			img.save(converted_img_path, 'png')

except:
	print('Error ')


if __name__ == '__main__':
	check_folder()
	image_conversion()

