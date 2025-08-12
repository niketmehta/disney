#!/usr/bin/env python3
"""
Simple Web Server for Disney Coordinator with Working Audio
Serves HTML interface and connects to the working audio coordinator
"""

import http.server
import socketserver
import json
import threading
import time
import os
import sys
from urllib.parse import urlparse, parse_qs
from disney_coordinator_working_audio import DisneyCoordinatorWorkingAudio

# Create global coordinator instance
coordinator = DisneyCoordinatorWorkingAudio()

class DisneyCoordinatorHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP handler for Disney Coordinator with audio."""
    
    def do_GET(self):
        """Handle GET requests."""
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/':
            # Serve the main HTML page
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html_content = self.get_html_content()
            self.wfile.write(html_content.encode())
            
        elif parsed_path.path == '/api/status':
            # Return coordinator status
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            status = {
                'coordinator': coordinator.get_coordinator_status(),
                'agents': coordinator.get_agent_status()
            }
            self.wfile.write(json.dumps(status).encode())
            
        else:
            # Serve static files
            super().do_GET()
    
    def do_POST(self):
        """Handle POST requests for coordinator actions."""
        parsed_path = urlparse(self.path)
        
        # Read request body
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode('utf-8'))
        except:
            data = {}
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {'status': 'success', 'message': 'Action completed'}
        
        if parsed_path.path == '/api/mickey/sing':
            def perform_action():
                result = coordinator.ask_mickey_to_perform("sing", song_name=data.get('song_name', 'Disney Song'))
                print(f"Mickey sing: {result}")
            
            thread = threading.Thread(target=perform_action)
            thread.start()
            response['message'] = 'Mickey is singing with audio!'
            
        elif parsed_path.path == '/api/mickey/dance':
            def perform_action():
                result = coordinator.ask_mickey_to_perform("dance", dance_move=data.get('dance_move', 'Mickey Shuffle'))
                print(f"Mickey dance: {result}")
            
            thread = threading.Thread(target=perform_action)
            thread.start()
            response['message'] = 'Mickey is dancing with audio!'
            
        elif parsed_path.path == '/api/mickey/wave':
            def perform_action():
                result = coordinator.ask_mickey_to_perform("wave", style=data.get('style', 'friendly'))
                print(f"Mickey wave: {result}")
            
            thread = threading.Thread(target=perform_action)
            thread.start()
            response['message'] = 'Mickey is waving with audio!'
            
        elif parsed_path.path == '/api/mickey/show':
            def perform_action():
                result = coordinator.ask_mickey_to_perform("show")
                print(f"Mickey show: {result}")
            
            thread = threading.Thread(target=perform_action)
            thread.start()
            response['message'] = 'Mickey is performing a show with audio!'
            
        elif parsed_path.path == '/api/mickey/rest':
            def perform_action():
                result = coordinator.ask_mickey_to_perform("rest")
                print(f"Mickey rest: {result}")
            
            thread = threading.Thread(target=perform_action)
            thread.start()
            response['message'] = 'Mickey is resting with audio!'
            
        elif parsed_path.path == '/api/donald/sing':
            def perform_action():
                result = coordinator.ask_donald_to_perform("sing", song_name=data.get('song_name', 'Donald Song'))
                print(f"Donald sing: {result}")
            
            thread = threading.Thread(target=perform_action)
            thread.start()
            response['message'] = 'Donald is singing with audio!'
            
        elif parsed_path.path == '/api/donald/dance':
            def perform_action():
                result = coordinator.ask_donald_to_perform("dance", dance_move=data.get('dance_move', 'Quack Attack'))
                print(f"Donald dance: {result}")
            
            thread = threading.Thread(target=perform_action)
            thread.start()
            response['message'] = 'Donald is dancing with audio!'
            
        elif parsed_path.path == '/api/donald/wave':
            def perform_action():
                result = coordinator.ask_donald_to_perform("wave", style=data.get('style', 'friendly'))
                print(f"Donald wave: {result}")
            
            thread = threading.Thread(target=perform_action)
            thread.start()
            response['message'] = 'Donald is waving with audio!'
            
        elif parsed_path.path == '/api/donald/show':
            def perform_action():
                result = coordinator.ask_donald_to_perform("show")
                print(f"Donald show: {result}")
            
            thread = threading.Thread(target=perform_action)
            thread.start()
            response['message'] = 'Donald is performing a show with audio!'
            
        elif parsed_path.path == '/api/donald/rest':
            def perform_action():
                result = coordinator.ask_donald_to_perform("rest")
                print(f"Donald rest: {result}")
            
            thread = threading.Thread(target=perform_action)
            thread.start()
            response['message'] = 'Donald is resting with audio!'
            
        elif parsed_path.path == '/api/duet/song':
            def perform_action():
                result = coordinator.perform_duet_song(data.get('song_name'))
                print(f"Duet song: {result}")
            
            thread = threading.Thread(target=perform_action)
            thread.start()
            response['message'] = 'Mickey and Donald are performing a duet song with audio!'
            
        elif parsed_path.path == '/api/duet/dance':
            def perform_action():
                result = coordinator.perform_duet_dance(data.get('dance_name'))
                print(f"Duet dance: {result}")
            
            thread = threading.Thread(target=perform_action)
            thread.start()
            response['message'] = 'Mickey and Donald are performing a duet dance with audio!'
            
        elif parsed_path.path == '/api/ensemble/show':
            def perform_action():
                result = coordinator.perform_ensemble_show()
                print(f"Ensemble show: {result}")
            
            thread = threading.Thread(target=perform_action)
            thread.start()
            response['message'] = 'Mickey and Donald are putting on an ensemble show with audio!'
            
        elif parsed_path.path == '/api/energy':
            def perform_action():
                result = coordinator.check_energy_levels()
                print(f"Energy check: {result}")
            
            thread = threading.Thread(target=perform_action)
            thread.start()
            response['message'] = 'Checking energy levels with audio!'
            
        elif parsed_path.path == '/api/rest/both':
            def perform_action():
                result = coordinator.rest_both_agents()
                print(f"Rest both: {result}")
            
            thread = threading.Thread(target=perform_action)
            thread.start()
            response['message'] = 'Both agents are taking a rest with audio!'
            
        else:
            response = {'status': 'error', 'message': 'Unknown endpoint'}
        
        self.wfile.write(json.dumps(response).encode())
    
    def get_html_content(self):
        """Generate the HTML content for the web interface."""
        return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Disney Coordinator Agent - Working Audio Web Interface</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            background-image: 
                radial-gradient(circle at 20% 80%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(255, 255, 255, 0.05) 0%, transparent 50%);
            min-height: 100vh;
            padding: 20px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        }}

        .header {{
            text-align: center;
            margin-bottom: 40px;
        }}

        .title {{
            font-size: 3rem;
            color: #e74c3c;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }}

        .subtitle {{
            font-size: 1.2rem;
            color: #666;
            margin-bottom: 10px;
        }}

        .magic-text {{
            font-size: 1rem;
            color: #e74c3c;
            font-weight: bold;
            animation: sparkle 2s infinite;
        }}

        @keyframes sparkle {{
            0%, 100% {{ opacity: 1; transform: scale(1); }}
            50% {{ opacity: 0.8; transform: scale(1.05); }}
        }}

        .audio-notice {{
            background: #d4edda;
            border: 1px solid #c3e6cb;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 30px;
            text-align: center;
            color: #155724;
        }}

        .agents-container {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 40px;
        }}

        .agent-card {{
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }}

        .agent-card:hover {{
            transform: translateY(-5px);
        }}

        .agent-avatar {{
            font-size: 4rem;
            margin-bottom: 20px;
            animation: bounce 2s infinite;
        }}

        .mickey-avatar {{
            color: #e74c3c;
        }}

        .donald-avatar {{
            color: #f39c12;
        }}

        @keyframes bounce {{
            0%, 20%, 50%, 80%, 100% {{ transform: translateY(0); }}
            40% {{ transform: translateY(-10px); }}
            60% {{ transform: translateY(-5px); }}
        }}

        .agent-name {{
            font-size: 1.8rem;
            font-weight: bold;
            margin-bottom: 15px;
            color: #333;
        }}

        .agent-status {{
            background: #fff;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            font-size: 0.9rem;
        }}

        .status-item {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 5px;
        }}

        .action-buttons {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
        }}

        .btn {{
            padding: 12px 20px;
            border: none;
            border-radius: 8px;
            font-size: 0.9rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .btn-primary {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }}

        .btn-success {{
            background: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%);
            color: white;
        }}

        .btn-warning {{
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
        }}

        .btn-info {{
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
        }}

        .btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }}

        .btn:disabled {{
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }}

        .duet-section {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            color: white;
            text-align: center;
        }}

        .duet-title {{
            font-size: 2rem;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }}

        .duet-avatars {{
            font-size: 3rem;
            margin-bottom: 20px;
        }}

        .duet-buttons {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }}

        .management-section {{
            background: #f8f9fa;
            border-radius: 15px;
            padding: 30px;
            text-align: center;
        }}

        .management-title {{
            font-size: 1.5rem;
            color: #333;
            margin-bottom: 20px;
        }}

        .management-buttons {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
        }}

        .status-display {{
            background: #fff;
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
            font-family: monospace;
            font-size: 0.9rem;
            max-height: 200px;
            overflow-y: auto;
        }}

        .notification {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: #28a745;
            color: white;
            padding: 15px 20px;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            transform: translateX(400px);
            transition: transform 0.3s ease;
            z-index: 1000;
        }}

        .notification.show {{
            transform: translateX(0);
        }}

        @media (max-width: 768px) {{
            .agents-container {{
                grid-template-columns: 1fr;
            }}
            
            .action-buttons {{
                grid-template-columns: 1fr;
            }}
            
            .duet-buttons {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="audio-notice">
            <h3>🎵 Disney Coordinator Agent - Working Audio Web Interface!</h3>
            <p>This interface connects to the Python coordinator with REAL audio capabilities!</p>
            <p>🔊 Audio System: System Beep (Working!)</p>
            <p>🎭 Click the buttons below to hear actual audio from Mickey and Donald!</p>
        </div>

        <div class="header">
            <h1 class="title">🎭 Disney Coordinator Agent</h1>
            <p class="subtitle">Managing Mickey Mouse and Donald Duck with Working Audio!</p>
            <p class="magic-text">✨ Orchestrating Disney Magic with Real Audio! ✨</p>
        </div>

        <div class="agents-container">
            <!-- Mickey Mouse Card -->
            <div class="agent-card" id="mickey-card">
                <div class="agent-avatar mickey-avatar" id="mickey-avatar">🐭</div>
                <h2 class="agent-name">Mickey Mouse</h2>
                <div class="agent-status" id="mickey-status">
                    <div class="status-item">
                        <span>Energy:</span>
                        <span id="mickey-energy">100%</span>
                    </div>
                    <div class="status-item">
                        <span>Status:</span>
                        <span id="mickey-performing">Available</span>
                    </div>
                </div>
                <div class="action-buttons">
                    <button class="btn btn-primary" onclick="performAction('mickey', 'sing')">🎤 Sing</button>
                    <button class="btn btn-success" onclick="performAction('mickey', 'dance')">💃 Dance</button>
                    <button class="btn btn-warning" onclick="performAction('mickey', 'wave')">👋 Wave</button>
                    <button class="btn btn-info" onclick="performAction('mickey', 'show')">🎭 Show</button>
                    <button class="btn btn-warning" onclick="performAction('mickey', 'rest')">😴 Rest</button>
                </div>
            </div>

            <!-- Donald Duck Card -->
            <div class="agent-card" id="donald-card">
                <div class="agent-avatar donald-avatar" id="donald-avatar">🦆</div>
                <h2 class="agent-name">Donald Duck</h2>
                <div class="agent-status" id="donald-status">
                    <div class="status-item">
                        <span>Energy:</span>
                        <span id="donald-energy">100%</span>
                    </div>
                    <div class="status-item">
                        <span>Status:</span>
                        <span id="donald-performing">Available</span>
                    </div>
                </div>
                <div class="action-buttons">
                    <button class="btn btn-primary" onclick="performAction('donald', 'sing')">🎤 Sing</button>
                    <button class="btn btn-success" onclick="performAction('donald', 'dance')">💃 Dance</button>
                    <button class="btn btn-warning" onclick="performAction('donald', 'wave')">👋 Wave</button>
                    <button class="btn btn-info" onclick="performAction('donald', 'show')">🎭 Show</button>
                    <button class="btn btn-warning" onclick="performAction('donald', 'rest')">😴 Rest</button>
                </div>
            </div>
        </div>

        <!-- Duet Section -->
        <div class="duet-section">
            <h2 class="duet-title">🎵 Duet Performances with Working Audio!</h2>
            <div class="duet-avatars">🐭🎵🦆</div>
            <p>Watch Mickey and Donald perform together with REAL audio beeps!</p>
            <div class="duet-buttons">
                <button class="btn btn-primary" onclick="performDuet('song')">🎵 Duet Song</button>
                <button class="btn btn-success" onclick="performDuet('dance')">💃 Duet Dance</button>
                <button class="btn btn-info" onclick="performEnsemble()">🎭 Ensemble Show</button>
            </div>
        </div>

        <!-- Management Section -->
        <div class="management-section">
            <h2 class="management-title">⚙️ Management</h2>
            <div class="management-buttons">
                <button class="btn btn-info" onclick="checkStatus()">📊 Status</button>
                <button class="btn btn-warning" onclick="checkEnergy()">🔋 Energy</button>
                <button class="btn btn-success" onclick="restBoth()">😴 Rest Both</button>
            </div>
            <div class="status-display" id="status-display">
                <p>Status information will appear here...</p>
            </div>
        </div>
    </div>

    <div class="notification" id="notification"></div>

    <script>
        // Global state
        let isPerforming = false;

        // Utility functions
        function showNotification(message, type = 'success') {{
            const notification = document.getElementById('notification');
            notification.textContent = message;
            notification.className = `notification show ${{type}}`;
            setTimeout(() => {{
                notification.classList.remove('show');
            }}, 3000);
        }}

        function setLoading(agent, loading) {{
            const card = document.getElementById(`${{agent}}-card`);
            const avatar = document.getElementById(`${{agent}}-avatar`);
            
            if (loading) {{
                card.classList.add('loading');
                avatar.style.animation = 'bounce 0.5s infinite';
            }} else {{
                card.classList.remove('loading');
                avatar.style.animation = 'bounce 2s infinite';
            }}
        }}

        // Individual agent actions with working audio
        function performAction(agent, action) {{
            if (isPerforming) {{
                showNotification('Another performance is in progress!', 'warning');
                return;
            }}

            setLoading(agent, true);
            isPerforming = true;

            // Show immediate feedback
            showNotification(`${{agent.charAt(0).toUpperCase() + agent.slice(1)}} is performing ${{action}} with working audio!`);

            // Make API call to the Python coordinator
            fetch(`/api/${{agent}}/${{action}}`, {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                }},
                body: JSON.stringify({{}})
            }})
            .then(response => response.json())
            .then(data => {{
                console.log('Response:', data);
                showNotification(`${{data.message}} Check console for audio output!`);
            }})
            .catch(error => {{
                console.error('Error:', error);
                showNotification('Error performing action!', 'error');
            }})
            .finally(() => {{
                setTimeout(() => {{
                    setLoading(agent, false);
                    isPerforming = false;
                }}, 3000);
            }});
        }}

        // Duet performances with working audio
        function performDuet(type) {{
            if (isPerforming) {{
                showNotification('Another performance is in progress!', 'warning');
                return;
            }}

            isPerforming = true;
            setLoading('mickey', true);
            setLoading('donald', true);

            showNotification(`Mickey and Donald are performing a duet ${{type}} with working audio!`);

            // Make API call to the Python coordinator
            fetch(`/api/duet/${{type}}`, {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                }},
                body: JSON.stringify({{}})
            }})
            .then(response => response.json())
            .then(data => {{
                console.log('Response:', data);
                showNotification(`${{data.message}} Check console for audio output!`);
            }})
            .catch(error => {{
                console.error('Error:', error);
                showNotification('Error performing duet!', 'error');
            }})
            .finally(() => {{
                setTimeout(() => {{
                    setLoading('mickey', false);
                    setLoading('donald', false);
                    isPerforming = false;
                }}, 5000);
            }});
        }}

        function performEnsemble() {{
            if (isPerforming) {{
                showNotification('Another performance is in progress!', 'warning');
                return;
            }}

            isPerforming = true;
            setLoading('mickey', true);
            setLoading('donald', true);

            showNotification('Mickey and Donald are putting on an ensemble show with working audio!');

            // Make API call to the Python coordinator
            fetch('/api/ensemble/show', {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                }},
                body: JSON.stringify({{}})
            }})
            .then(response => response.json())
            .then(data => {{
                console.log('Response:', data);
                showNotification(`${{data.message}} Check console for audio output!`);
            }})
            .catch(error => {{
                console.error('Error:', error);
                showNotification('Error performing ensemble!', 'error');
            }})
            .finally(() => {{
                setTimeout(() => {{
                    setLoading('mickey', false);
                    setLoading('donald', false);
                    isPerforming = false;
                }}, 8000);
            }});
        }}

        // Management functions
        function checkStatus() {{
            showNotification('Checking status of all agents...');
            
            fetch('/api/status')
            .then(response => response.json())
            .then(data => {{
                console.log('Status:', data);
                document.getElementById('status-display').innerHTML = `
                    <strong>Working Audio Coordinator Status:</strong><br>
                    Coordinator: ${{data.coordinator.coordinator_name}}<br>
                    Audio System: ${{data.coordinator.audio_system}}<br>
                    Mickey: ${{data.agents.mickey.status}}, Energy ${{data.agents.mickey.energy}}%<br>
                    Donald: ${{data.agents.donald.status}}, Energy ${{data.agents.donald.energy}}%<br>
                    Duet Songs Available: ${{data.coordinator.available_duet_songs}}<br>
                    Duet Dances Available: ${{data.coordinator.available_duet_dances}}
                `;
            }})
            .catch(error => {{
                console.error('Error:', error);
                showNotification('Error checking status!', 'error');
            }});
        }}

        function checkEnergy() {{
            showNotification('Checking energy levels...');
            
            fetch('/api/energy', {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                }},
                body: JSON.stringify({{}})
            }})
            .then(response => response.json())
            .then(data => {{
                console.log('Energy check:', data);
                showNotification(`${{data.message}} Check console for details!`);
            }})
            .catch(error => {{
                console.error('Error:', error);
                showNotification('Error checking energy!', 'error');
            }});
        }}

        function restBoth() {{
            if (isPerforming) {{
                showNotification('Cannot rest while performing!', 'warning');
                return;
            }}

            setLoading('mickey', true);
            setLoading('donald', true);

            showNotification('Both agents are taking a rest with audio!');

            fetch('/api/rest/both', {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                }},
                body: JSON.stringify({{}})
            }})
            .then(response => response.json())
            .then(data => {{
                console.log('Rest both:', data);
                showNotification(`${{data.message}} Check console for details!`);
            }})
            .catch(error => {{
                console.error('Error:', error);
                showNotification('Error resting agents!', 'error');
            }})
            .finally(() => {{
                setTimeout(() => {{
                    setLoading('mickey', false);
                    setLoading('donald', false);
                }}, 3000);
            }});
        }}

        // Initialize
        document.addEventListener('DOMContentLoaded', function() {{
            showNotification('🎵 Working audio Disney Coordinator loaded!');
            checkStatus();
        }});
    </script>
</body>
</html>
"""

def main():
    """Start the web server."""
    PORT = 8080
    
    with socketserver.TCPServer(("", PORT), DisneyCoordinatorHandler) as httpd:
        print("🎭🎵🦆🐭")
        print("=" * 60)
        print("    DISNEY COORDINATOR WEB SERVER")
        print("=" * 60)
        print("🎭🎵🦆🐭")
        print()
        print(f"🎉 Disney Coordinator Web Server is running!")
        print(f"🔊 Audio System: Working (System Beep)")
        print(f"🌐 Open http://localhost:{PORT} in your browser")
        print(f"🎵 Click the buttons to hear actual audio!")
        print()
        print("🎭 Available Features:")
        print("   • Individual performances with audio")
        print("   • Duet songs with harmonies")
        print("   • Duet dances with rhythm")
        print("   • Ensemble shows with fanfares")
        print("   • Real system beeps for all actions")
        print()
        print("Press Ctrl+C to stop the server")
        print()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🎭 Shutting down Disney Coordinator Web Server...")
            print("🎵 Thanks for using the working audio system!")

if __name__ == "__main__":
    main()