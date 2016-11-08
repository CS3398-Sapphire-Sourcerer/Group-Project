from init import app, socketio
import views, api


if __name__ == '__main__':
    # app.run(debug=True)
    socketio.run(app, debug=True)
