from flask import Flask, render_template


app=Flask(__name__)
@app.route('/')
def blog():
    return render_template('user_list.html')

if __name__=='__main__':
    app.run(debug=True)
