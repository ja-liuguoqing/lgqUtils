from main import app, socketio

@socketio.on('message')
def handle_message(data):
    print(f"received_message : {data}")

@socketio.on('json')
def handle_json(json):
    print(f"received_json : {json}")

@socketio.on('my event')
def handle_my_custom_event(json):
    print(f"received_json : {json}")

@socketio.on('my event')
def handle_my_custom_event(arg1, arg2, arg3):
    print(f"received_json : {arg1}, {arg2}, {arg3}")

def my_function_handler(data):
    pass

socketio.on_event("my event", my_function_handler, namespace='/test')