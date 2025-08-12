from flask import Flask, render_template, request, jsonify
from disney_coordinator_agent import DisneyCoordinatorAgent
import threading
import time

app = Flask(__name__)
coordinator = DisneyCoordinatorAgent()

@app.route('/')
def index():
    return render_template('coordinator_index.html')

# Individual Agent Management
@app.route('/api/mickey/<action>', methods=['POST'])
def mickey_action(action):
    data = request.get_json() or {}
    
    def perform_action():
        result = coordinator.ask_mickey_to_perform(action, **data)
        print(result)
    
    thread = threading.Thread(target=perform_action)
    thread.start()
    
    return jsonify({
        'status': 'success',
        'message': f'Mickey is performing {action}!',
        'action': action
    })

@app.route('/api/donald/<action>', methods=['POST'])
def donald_action(action):
    data = request.get_json() or {}
    
    def perform_action():
        result = coordinator.ask_donald_to_perform(action, **data)
        print(result)
    
    thread = threading.Thread(target=perform_action)
    thread.start()
    
    return jsonify({
        'status': 'success',
        'message': f'Donald is performing {action}!',
        'action': action
    })

# Duet Performances
@app.route('/api/duet/song', methods=['POST'])
def duet_song():
    data = request.get_json() or {}
    song_name = data.get('song_name')
    
    def perform_duet():
        result = coordinator.perform_duet_song(song_name)
        print(result)
    
    thread = threading.Thread(target=perform_duet)
    thread.start()
    
    return jsonify({
        'status': 'success',
        'message': f'Mickey and Donald are performing a duet song!',
        'song_name': song_name
    })

@app.route('/api/duet/dance', methods=['POST'])
def duet_dance():
    data = request.get_json() or {}
    dance_name = data.get('dance_name')
    
    def perform_duet():
        result = coordinator.perform_duet_dance(dance_name)
        print(result)
    
    thread = threading.Thread(target=perform_duet)
    thread.start()
    
    return jsonify({
        'status': 'success',
        'message': f'Mickey and Donald are performing a duet dance!',
        'dance_name': dance_name
    })

@app.route('/api/ensemble/show', methods=['POST'])
def ensemble_show():
    def perform_ensemble():
        result = coordinator.perform_ensemble_show()
        print(result)
    
    thread = threading.Thread(target=perform_ensemble)
    thread.start()
    
    return jsonify({
        'status': 'success',
        'message': 'Mickey and Donald are putting on an ensemble show!'
    })

# Management Functions
@app.route('/api/status')
def get_status():
    return jsonify({
        'coordinator': coordinator.get_coordinator_status(),
        'agents': coordinator.get_agent_status()
    })

@app.route('/api/energy')
def check_energy():
    def check():
        result = coordinator.check_energy_levels()
        print(result)
    
    thread = threading.Thread(target=check)
    thread.start()
    
    return jsonify({
        'status': 'success',
        'message': 'Checking energy levels of both agents!'
    })

@app.route('/api/rest/both', methods=['POST'])
def rest_both():
    def rest():
        result = coordinator.rest_both_agents()
        print(result)
    
    thread = threading.Thread(target=rest)
    thread.start()
    
    return jsonify({
        'status': 'success',
        'message': 'Both agents are taking a rest!'
    })

@app.route('/api/available')
def get_available():
    return jsonify(coordinator.get_available_performances())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)