from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return ("""
#     <div>
#     Hello, World! <h1>Mensaje añadido</h1>
#     heh
#     """)

# posts = []

# @app.route("/")
# def index():
#     return "{} posts".format(len(posts))

# @app.route("/p/<string:slug>/")
# def show_post(slug):
#     return "Mostrando el post {}".format(slug)

@app.route('/hello/<user>/')
# @app.route('/')
def hello_name(user):
#    return render_template('templates/hello.html')
   return render_template('hello.html', name = user)

if __name__ == '__main__':
   app.run(debug = True)



@app.route("/process")
def process():
    obj = process_obj()
    registrar.add("some-unique-id", obj)
    return render_template("results.html", id="some-unique-id")

@app.route("/kill")
def kill():
    id = request.args.get("id")
    x = registrar.get(id)
    x.close()
    registrar.remove(id)
    return render_template("killed.html")
