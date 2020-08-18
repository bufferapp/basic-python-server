from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
  print(request.headers)
  print(request.remote_addr)
  if request.method == 'GET':
    print('The request was a get')
    print(request.headers)
    print(request.remote_addr)
  if request.method == 'POST':
    print(request.json)
    print(request.form)
  return {'test': 'it worked'}
