from flask import Flask, render_template, request, jsonify
from donald_duck_agent import DonaldDuckAgent
import threading
import time

app = Flask(__name__)
donald = DonaldDuckAgent()

@app.route('/')
def index():
    return render_template('donald_index.html')

@app.route('/api/sing', methods=['POST'])
def sing():
    data = request.get_json()
    song_name = data.get('song_name') if data else None
    
    def perform_sing():
        result = donald.sing(song_name)
        print(result)
    
    thread = threading.Thread(target=perform_sing)
    thread.start()
    
    return jsonify({
        'status': 'success',
        'message': f'Donald is singing {song_name or "a random song"}!',
        'song_name': song_name
    })

@app.route('/api/wave', methods=['POST'])
def wave():
    data = request.get_json()
    style = data.get('style', 'friendly') if data else 'friendly'
    
    def perform_wave():
        result = donald.wave(style)
        print(result)
    
    thread = threading.Thread(target=perform_wave)
    thread.start()
    
    return jsonify({
        'status': 'success',
        'message': f'Donald is waving {style}ly!',
        'style': style
    })

@app.route('/api/dance', methods=['POST'])
def dance():
    data = request.get_json()
    dance_move = data.get('dance_move') if data else None
    
    def perform_dance():
        result = donald.dance(dance_move)
        print(result)
    
    thread = threading.Thread(target=perform_dance)
    thread.start()
    
    return jsonify({
        'status': 'success',
        'message': f'Donald is dancing {dance_move or "a random dance"}!',
        'dance_move': dance_move
    })

@app.route('/api/show', methods=['POST'])
def perform_show():
    def perform_full_show():
        result = donald.perform_show()
        print(result)
    
    thread = threading.Thread(target=perform_full_show)
    thread.start()
    
    return jsonify({
        'status': 'success',
        'message': 'Donald is putting on a spectacular show!'
    })

@app.route('/api/status')
def get_status():
    return jsonify(donald.get_status())

@app.route('/api/rest', methods=['POST'])
def rest():
    def perform_rest():
        result = donald.rest()
        print(result)
    
    thread = threading.Thread(target=perform_rest)
    thread.start()
    
    return jsonify({
        'status': 'success',
        'message': 'Donald is taking a rest!'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)