from PIL import Image
import glob, os
import subprocess


def main():
	
	photos = []
	print(glob.glob("characters/*.png"))
	for pic in glob.glob("characters/*.png"):
		photos.append(pic)
	print(photos)
	result = subprocess.run(['exiftool', '-h', '/characters/{}'.format(photos[0])], stdout=subprocess.PIPE)
	print (type(result))
	print ("\n\n",result.stdout)
	normal_string = result.stdout.decode("utf-8")
	print("\n\n", normal_string)


if __name__ == "__main__":
	main()