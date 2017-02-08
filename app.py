from flask import Flask, render_template, request, url_for, redirect
from flask_modus import Modus
from toy import Toy

app = Flask(__name__)
modus = Modus(app)

lego_batman = Toy('lego batman','https://s-media-cache-ak0.pinimg.com/736x/16/a0/1a/16a01acb08dc08543fe55bbe5d79f337.jpg')

bear = Toy('lotso bear','http://vignette1.wikia.nocookie.net/pixar/images/3/38/Toy-story-3-definitive-collection-lotso-512x600.jpg/revision/latest?cb=20100910222854')

hot_wheel = Toy("orange hot wheel", "https://assets.wired.com/photos/w_1210/wp-content/uploads/2016/09/HotwheelsTA.jpg")

gi_joe = Toy("G I Joe", "https://s-media-cache-ak0.pinimg.com/564x/f0/d9/74/f0d97456131bccc233733561cd812f56.jpg")

toys = [lego_batman,bear,hot_wheel, gi_joe]

def get_toy(id):
	return [toy for toy in toys if toy.id == id][0]


@app.route('/toys', methods=["GET","POST"])
def show_toys():
	if request.method == "POST":
		new_toy = Toy(request.form['toyname'], request.form['image_url'])
		toys.append(new_toy)
		return redirect(url_for('show_toys'))
	else:	
		return render_template('index.html', toys = toys)



@app.route('/toys/new')
def submit():
	return render_template('add.html')	


@app.route('/toys/<int:id>', methods = ["GET","PATCH","DELETE"])
def show_individual_toy(id):
	found_toy = next(toy for toy in toys if toy.id == id)
	if request.method == b"PATCH":
		found_toy.name = request.form['toyname']
		found_toy.image_url = request.form['image_url']
		return redirect(url_for('show_toys'))
	if request.method == b"DELETE":
		idx = toys.index(found_toy)
		toys.pop(idx)	
		return redirect(url_for('show_toys'))
	return render_template('individual_toy.html', toy = found_toy)	


@app.route('/toys/<int:id>/edit')
def edit_toy(id):
	return render_template('edit.html', toy = get_toy(id))			




if __name__ == '__main__':
	app.run(port=3000, debug=True)