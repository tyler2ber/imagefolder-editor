from PIL import Image
from pathlib import Path


print("\n---- IMAGEFOLDER EDITOR ----")
print("provide the images, get them renamed and/or resized\n\n")

folder_path = Path("imagefolder-original")
extensions = [".jpg", ".jpeg", ".png"]

# loop through imagefolder-original
for filepath in folder_path.iterdir():
	if filepath.suffix in extensions:

		print(f"current_filepath: {filepath}")

		with Image.open(filepath) as image:

			image_name = image.filename.split('/')[1]
			image_name_new = image_name # set to change

			image_width, image_height = image.size
			image_width_new = image_width # set to change

			print(f"====> {image_name} ({image_width}x{image_height})")

			# ask about rename
			while True:
				should_rename_image = input("rename image? (y/n): ")
				if should_rename_image == "y":
					print("RENAMING...")
					image_name_new = input(f"Enter new name for {image_name}: ") + "." + image.filename.split(".")[1]
					break
				elif should_rename_image == "n":
					print("skipping rename...")
					break
				else:
					print("ERROR: enter 'y' or 'n'")
			print(f"CONFIRMED: {image_name} ==> {image_name_new}")

			# ask about resize
			while True:
				should_resize_image = input("resize image? (y/n): ")
				if should_resize_image == "y":
					print("RESIZING...")
					image_width_new = input(f"Enter new width for {image_name}({image_width}xheight): ")
					break
				elif should_resize_image == "n":
					print("skipping resize...")
					break
				else:
					print("ERROR: enter 'y' or 'n'")
			print(f"CONFIRMED: {image_width} ==> {image_width_new}")

			# rename and/or resize the image
			print("[insert_done_message]\n\n")
