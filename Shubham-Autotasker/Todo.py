from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Define the Todo model after creating the db object
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return "<Task %r>" % self.id

# Function to create tables within app context
def create_tables():
    with app.app_context():
        db.create_all()

# Call the create_tables function
create_tables()

@app.route('/todo', methods=["POST", "GET"])
def todo():
    if request.method == "POST":
        task_content = request.form["task"]
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('todo.todo'))
        except Exception as e:
            return f"There was an issue adding your task: {str(e)}"
    else:
        tasks = Todo.query.order_by(Todo.pub_date).all()
        return render_template("todo.html", tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task = Todo.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('todo.todo'))
    except Exception as e:
        return f"There was an issue deleting the task: {str(e)}"

@app.route('/update/<int:id>', methods=["POST", "GET"])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form["task"]
        try:
            db.session.commit()
            return redirect(url_for('todo.todo'))
        except Exception as e:
            return f"There was an issue updating the task: {str(e)}"
    else:
        tasks = Todo.query.order_by(Todo.pub_date).all()
        return render_template("todo.html", update_task=task, tasks=tasks)

# Example route in Autotasker for your other functionality
@app.route('/execute', methods=['POST'])
def handle_execute():
    # Implement your command execution logic here
    pass

# Example route to start listening for voice commands
@app.route('/start_listening', methods=['POST'])
def start_listening():
    # Implement your voice recognition logic here
    pass

# Example route to stop listening for voice commands
@app.route('/stop_listening', methods=['POST'])
def stop_listening():
    # Implement logic to stop voice recognition
    pass

if __name__ == '__main__':
    app.run(debug=True)
