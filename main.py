
import glob, os
import random

@app.route('/route_name')
def script_output():
    output = random_pic()
    return render_template('template_name.html',output=output)

def random_pic():
	photos = []
	print(glob.glob("characters/*.png"))
	for pic in glob.glob("characters/*.png"):
		photos.append(pic)
	file = random.choice(photos)

	return file

def main():

	script_output()


if __name__ == "__main__":
	main()