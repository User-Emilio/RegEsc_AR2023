from app import create_app

app = create_app()

if __name__ == '__main__':
    socketio.run(app,debug=True,host='127.0.0.1')