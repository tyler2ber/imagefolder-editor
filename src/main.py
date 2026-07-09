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
			image_width, image_height = image.size
			print(f"====> {image_name} ({image_width}x{image_height})")

			# ask about rename
			while True:
				should_rename_file = input("rename file? (y/n): ")
				if should_rename_file == "y":
					print("RENAMING FILE")
					break
				elif should_rename_file == "n":
					print("NOT RENAMING FILE")
					break
				else:
					print("ERROR: enter 'y' or 'n'")

			# ask about resize
			while True:
				should_resize_file = input("resize file? (y/n): ")
				if should_resize_file == "y":
					print("RESIZING FILE")
					break
				elif should_resize_file == "n":
					print("NOT RESIZING FILE")
					break
				else:
					print("ERROR: enter 'y' or 'n'")
			print("[insert_done_message]\n\n")
