from PIL import Image
import glob, os


def main():
	photos = []
	print(glob.glob("characters/*.png"))
	for pic in glob.glob("characters/*.png"):
		photos.append(pic)
	os.chdir("characters")
	f = Image.open(pic[0]).show()

if __name__ == "__main__":
	main()