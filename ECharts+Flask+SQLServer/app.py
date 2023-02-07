

# use ASGI instead of WSGI
from asgiref.wsgi import WsgiToAsgi
from flask import Flask, render_template
from static.py.dataops import updateOverall


# start service
app = Flask(__name__)

@app.route('/api')
def getChart():
    return render_template('index.html')

@app.route('/api/async')
def getChartAsync():
    return render_template('async_index.html')

@app.route('/api/async/draw')
def draw():
    return updateOverall()


# execute in cmd: uvicorn app:asgi_app --host host_name --port 9002 --reload
# execute in cmd: uvicorn app:asgi_app --host ip --port 9002 --reload
asgi_app = WsgiToAsgi(app)
print('Server listening...')


if __name__ == "__main__":
    pass
    #app.run(host='127.0.0.1', port=9002, debug = True)