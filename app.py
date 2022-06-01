

from flask import Flask , render_template , request , redirect , url_for

app = Flask(__name__)
from flask_modus import Modus

from snacks import Snack
modus = Modus(app)

busicut = Snack(name="cabin", kind="currywing")
fry = Snack(name="bread", kind="flouring")
sweet = Snack(name="lopipo", kind="flavouring")
css = Snack(name="wingi" , kind="wizpop")
option= Snack(name="magarine", kind="clina")
optional= Snack(name="rinemaga", kind="lcina")



data_snack=[busicut,fry,sweet,css, option,optional]

def find_snack(snacks_id):
	return [snack for snack in data_snack if snack.id == snacks_id][0]

@app.route('/', methods=["GET","POST"])
def index():
	if request.method =='POST':
		new_snacks = Snack(request.form['name'], request.form['kind'])
		data_snack.append(new_snacks)
	return render_template("index.html", data_snack = data_snack)



@app.route('/snacks/new')
def new():
	return render_template("new.html")


@app.route('/snacks/<int:id>', methods=['GET','PATCH','DELETE'])
def show(id):
	found_stack = find_snack(id)
	if request.method == b"PATCH":
		found_stack.name=request.form['name']
		found_stack.kind=request.form['kind']
		return redirect(url_for('index'))

	if request.method == b'DELETE':
		data_snack.remove(found_stack)
		return redirect(url_for('index'))

	return render_template('show.html', snack = found_stack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
	found_stack = find_snack(id)
	return render_template('edit.html', snack = found_stack)



# if __name__=='__main__':
# 	app.run(debug=True, port=5000)






























