from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

"""q:what are the most common uses for python?"""
"""a:web development, data science, machine learning, and system scripting"""

"""create a function that takes a string and returns it backwards"""
def reverse_string(string):
    return string[::-1]


"""test the function"""
print(reverse_string("hello world"))