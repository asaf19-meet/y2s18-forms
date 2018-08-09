from databases import *
from flask import Flask, render_template, url_for, request , redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

@app.route('/student/<int:student_id>',methods = ['POST'])
def delete_student_by_id(student_id):
	if request.method == 'POST':
		delete_student_id(student_id)
		return redirect(url_for('home'))

@app.route('/edit/<int:student_id>',methods = ['GET','POST'])
def edit_student_lab_status(student_id):
	if request.method == 'GET':
		return render_template('edit.html', student=query_by_id(student_id))
	else:
		student = query_by_id(student_id)
		lab_status =request.form['updated_lab_status']
		update_lab_status(student.name,lab_status)
		return render_template('home.html')

@app.route('/add',methods=['GET', 'POST'])
def add_student_route():
	if request.method == 'GET':
		return render_template('add.html')
	else:
		name = request.form['student_name']
		year = request.form['student_year']
		lab = request.form['lab_status']
		add_student(name,year,lab)
		return render_template('add.html')


app.run(debug=True)
