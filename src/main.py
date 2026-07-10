from PIL import Image
import os


print("\n---- IMAGEFOLDER EDITOR ----")
print("provide the images, get them renamed and/or resized\n\n")

folderpath_original = "imagefolder-original"
folderpath_new = "imagefolder-new"

for file in os.listdir(folderpath_original):
	if file.split(".")[1] in ["jpg", "jpeg", "png"]:

		# image

		image = Image.open(f"{folderpath_original}/{file}")

		image_name = image.filename.split("/")[1]
		image_width, image_height = image.size

		print(f"current: {folderpath_original}/{file}")
		print(f"====> {image_name}({image_width}x{image_height})")

		# image_new

		image_name_new = image_name # set to change
		image_width_new = image_width # set to change

		# RENAMING
		while True:
			should_rename = input("rename image? (y/n): ")
			if should_rename == "y":
				print("RENAMING...")
				image_name_new = input(f"enter new name for {image_name}: ") + "." + image_name.split(".")[1]
				break
			elif should_rename == "n":
				print("skipping rename...")
				break
			else:
				print("ERROR: enter 'y' or 'n'")

		# RESIZING
		while True:
			should_resize = input("resize image? (y/n): ")
			if should_resize == "y":
				print("RESIZING...")
				image_width_new = int(input(f"enter new width for {image_name}({image_width}x{image_height}): "))
				image_height = int((image_width_new/image_width) * image_height)
				break
			elif should_resize == "n":
				print("skipping resize...")
				break
			else:
				print("ERROR: enter 'y' or 'n'")

		image_new = image.resize((image_width_new, image_height))
		image_new.save(f"{folderpath_new}/{image_name_new}")
		print(f"====> {image_name_new}({image_width_new}x{image_height})\n")
