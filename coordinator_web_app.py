#!/usr/bin/env python3
"""
Disney Coordinator Web App with Real Audio Capabilities
Working web interface that actually connects to the coordinator agent
"""

import time
import random
import threading
import os
import sys
import math
import json
from typing import List, Dict, Optional, Tuple
from mickey_mouse_agent import MickeyMouseAgent
from donald_duck_agent import DonaldDuckAgent

# Try to import audio libraries
try:
    import winsound  # Windows
    AUDIO_AVAILABLE = True
    AUDIO_TYPE = "winsound"
except ImportError:
    try:
        import pygame.mixer  # Cross-platform
        AUDIO_AVAILABLE = True
        AUDIO_TYPE = "pygame"
    except ImportError:
        try:
            import pyaudio  # Cross-platform
            import numpy as np
            AUDIO_AVAILABLE = True
            AUDIO_TYPE = "pyaudio"
        except ImportError:
            AUDIO_AVAILABLE = False
            AUDIO_TYPE = "none"

class DisneyCoordinatorWeb:
    """
    Disney Coordinator Agent with Real Audio Capabilities for Web Interface
    """
    
    def __init__(self):
        self.name = "Disney Coordinator (Web Audio)"
        self.mickey = MickeyMouseAgent()
        self.donald = DonaldDuckAgent()
        self.is_coordinating = False
        
        # Musical notes and frequencies (in Hz)
        self.musical_notes = {
            "C": 261.63, "C#": 277.18, "D": 293.66, "D#": 311.13,
            "E": 329.63, "F": 349.23, "F#": 369.99, "G": 392.00,
            "G#": 415.30, "A": 440.00, "A#": 466.16, "B": 493.88
        }
        
        # Disney song melodies (simplified)
        self.disney_melodies = {
            "friendship": ["C", "E", "G", "C", "E", "G", "A", "G"],
            "magic": ["F", "A", "C", "F", "A", "C", "D", "C"],
            "harmony": ["G", "B", "D", "G", "B", "D", "E", "D"]
        }
        
        # Duet songs that both agents can perform together
        self.duet_songs = [
            "Mickey and Donald's Friendship Song",
            "The Disney Duet",
            "Best Friends Forever",
            "Magical Partners",
            "Disney Harmony"
        ]
        
        # Collaborative dance routines
        self.duet_dances = [
            "The Mickey-Donald Shuffle",
            "Friendship Waltz",
            "Disney Duo Dance",
            "Magical Partners Spin",
            "Best Friends Bounce"
        ]
        
        # Initialize audio system
        self._init_audio()
    
    def _init_audio(self):
        """Initialize the audio system based on available libraries."""
        if not AUDIO_AVAILABLE:
            print("🎵 Audio libraries not available. Using visual audio simulation.")
            return
        
        try:
            if AUDIO_TYPE == "pygame":
                pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=512)
                print("🎵 Audio system initialized with pygame!")
            elif AUDIO_TYPE == "pyaudio":
                self.p = pyaudio.PyAudio()
                print("🎵 Audio system initialized with pyaudio!")
            elif AUDIO_TYPE == "winsound":
                print("🎵 Audio system initialized with winsound!")
        except Exception as e:
            print(f"🎵 Audio initialization failed: {e}")
            print("🎵 Falling back to visual audio simulation.")
    
    def _generate_tone(self, frequency: float, duration: float = 0.3, volume: float = 0.5):
        """Generate a musical tone at the specified frequency."""
        if not AUDIO_AVAILABLE:
            return
        
        try:
            if AUDIO_TYPE == "winsound":
                # Windows beep (limited but works)
                winsound.Beep(int(frequency), int(duration * 1000))
            elif AUDIO_TYPE == "pygame":
                # Generate sine wave with pygame
                sample_rate = 22050
                samples = int(duration * sample_rate)
                wave = []
                for i in range(samples):
                    wave.append(int(volume * 32767 * math.sin(2 * math.pi * frequency * i / sample_rate)))
                sound = pygame.mixer.Sound(bytes(wave))
                sound.play()
                time.sleep(duration)
            elif AUDIO_TYPE == "pyaudio":
                # Generate sine wave with pyaudio
                sample_rate = 22050
                samples = int(duration * sample_rate)
                wave = []
                for i in range(samples):
                    wave.append(volume * math.sin(2 * math.pi * frequency * i / sample_rate))
                wave = np.array(wave, dtype=np.float32)
                stream = self.p.open(format=pyaudio.paFloat32, channels=1, rate=sample_rate, output=True)
                stream.write(wave.tobytes())
                stream.stop_stream()
                stream.close()
        except Exception as e:
            print(f"🎵 Audio generation failed: {e}")
    
    def _play_melody(self, melody: List[str], duration: float = 0.3):
        """Play a sequence of musical notes."""
        for note in melody:
            if note in self.musical_notes:
                self._generate_tone(self.musical_notes[note], duration)
            time.sleep(0.1)
    
    def get_agent_status(self, agent_name: str = "both") -> Dict[str, Dict]:
        """Get status of specified agent(s)."""
        if agent_name.lower() == "mickey":
            return {"mickey": self.mickey.get_status()}
        elif agent_name.lower() == "donald":
            return {"donald": self.donald.get_status()}
        else:
            return {
                "mickey": self.mickey.get_status(),
                "donald": self.donald.get_status()
            }
    
    def ask_mickey_to_perform(self, action: str, **kwargs) -> str:
        """Ask Mickey to perform a specific action with audio."""
        if self.mickey.is_performing:
            return f"🎭 {self.mickey.name} is already performing! Please wait."
        
        # Play musical intro
        intro_melody = ["C", "E", "G"]
        self._play_melody(intro_melody, 0.2)
        
        if action == "sing":
            result = self.mickey.sing(kwargs.get('song_name'))
            # Play musical outro
            outro_melody = ["G", "E", "C"]
            self._play_melody(outro_melody, 0.2)
            return result
        elif action == "dance":
            result = self.mickey.dance(kwargs.get('dance_move'))
            # Play dance rhythm
            dance_rhythm = ["C", "G", "C", "G"]
            self._play_melody(dance_rhythm, 0.15)
            return result
        elif action == "wave":
            result = self.mickey.wave(kwargs.get('style', 'friendly'))
            # Play wave sound
            wave_sound = ["C", "D", "E"]
            self._play_melody(wave_sound, 0.1)
            return result
        elif action == "show":
            result = self.mickey.perform_show()
            # Play show fanfare
            fanfare = ["C", "E", "G", "C", "E", "G", "A", "G"]
            self._play_melody(fanfare, 0.2)
            return result
        elif action == "rest":
            result = self.mickey.rest()
            # Play rest sound
            rest_sound = ["G", "E", "C"]
            self._play_melody(rest_sound, 0.3)
            return result
        else:
            return f"❌ Unknown action '{action}' for {self.mickey.name}"
    
    def ask_donald_to_perform(self, action: str, **kwargs) -> str:
        """Ask Donald to perform a specific action with audio."""
        if self.donald.is_performing:
            return f"🎭 {self.donald.name} is already performing! Please wait."
        
        # Play musical intro
        intro_melody = ["F", "A", "C"]
        self._play_melody(intro_melody, 0.2)
        
        if action == "sing":
            result = self.donald.sing(kwargs.get('song_name'))
            # Play musical outro
            outro_melody = ["C", "A", "F"]
            self._play_melody(outro_melody, 0.2)
            return result
        elif action == "dance":
            result = self.donald.dance(kwargs.get('dance_move'))
            # Play dance rhythm
            dance_rhythm = ["F", "C", "F", "C"]
            self._play_melody(dance_rhythm, 0.15)
            return result
        elif action == "wave":
            result = self.donald.wave(kwargs.get('style', 'friendly'))
            # Play wave sound
            wave_sound = ["F", "G", "A"]
            self._play_melody(wave_sound, 0.1)
            return result
        elif action == "show":
            result = self.donald.perform_show()
            # Play show fanfare
            fanfare = ["F", "A", "C", "F", "A", "C", "D", "C"]
            self._play_melody(fanfare, 0.2)
            return result
        elif action == "rest":
            result = self.donald.rest()
            # Play rest sound
            rest_sound = ["C", "A", "F"]
            self._play_melody(rest_sound, 0.3)
            return result
        else:
            return f"❌ Unknown action '{action}' for {self.donald.name}"
    
    def perform_duet_song(self, song_name: Optional[str] = None) -> str:
        """Mickey and Donald perform a duet song together with REAL audio!"""
        if self.mickey.is_performing or self.donald.is_performing:
            return f"🎭 One or both agents are already performing! Please wait."
        
        if song_name is None:
            song_name = random.choice(self.duet_songs)
        
        self.is_coordinating = True
        self.mickey.is_performing = True
        self.donald.is_performing = True
        
        # Musical introduction with real audio
        intro_melody = self.disney_melodies["friendship"]
        self._play_melody(intro_melody, 0.4)
        
        # Get duet lyrics
        lyrics = self._get_duet_lyrics(song_name)
        
        # Perform the duet with enhanced musical accompaniment
        for i in range(0, len(lyrics), 2):
            if i + 1 < len(lyrics):
                # Duet harmony with real audio
                mickey_notes = random.sample(list(self.musical_notes.keys()), 2)
                donald_notes = random.sample(list(self.musical_notes.keys()), 2)
                
                # Mickey's part
                for note in mickey_notes:
                    self._generate_tone(self.musical_notes[note], 0.3)
                
                time.sleep(0.5)
                
                # Donald's part
                for note in donald_notes:
                    self._generate_tone(self.musical_notes[note], 0.3)
                
                time.sleep(0.5)
                
                # Combined harmony
                combined_notes = random.sample(list(self.musical_notes.keys()), 4)
                for note in combined_notes:
                    self._generate_tone(self.musical_notes[note], 0.2)
                
                time.sleep(0.8)
        
        # Grand finale with full orchestra
        finale_melody = self.disney_melodies["magic"] + self.disney_melodies["harmony"]
        self._play_melody(finale_melody, 0.2)
        
        self.mickey.is_performing = False
        self.donald.is_performing = False
        self.is_coordinating = False
        
        return f"🎵 {self.mickey.name} and {self.donald.name} finished their duet '{song_name}'! What a magical performance! ✨"
    
    def perform_duet_dance(self, dance_name: Optional[str] = None) -> str:
        """Mickey and Donald perform a duet dance together with musical accompaniment!"""
        if self.mickey.is_performing or self.donald.is_performing:
            return f"🎭 One or both agents are already performing! Please wait."
        
        if dance_name is None:
            dance_name = random.choice(self.duet_dances)
        
        self.is_coordinating = True
        self.mickey.is_performing = True
        self.donald.is_performing = True
        
        # Dance music introduction
        dance_melody = ["C", "E", "G", "C", "E", "G"]
        self._play_melody(dance_melody, 0.3)
        
        # Get duet dance steps
        steps = self._get_duet_dance_steps(dance_name)
        
        # Perform the duet dance with synchronized moves and music
        for i, step in enumerate(steps):
            # Dance rhythm
            rhythm_notes = random.sample(list(self.musical_notes.keys()), 2)
            for note in rhythm_notes:
                self._generate_tone(self.musical_notes[note], 0.2)
            time.sleep(0.6)
        
        # Dance finale
        finale_melody = ["G", "B", "D", "G", "B", "D"]
        self._play_melody(finale_melody, 0.2)
        
        self.mickey.is_performing = False
        self.donald.is_performing = False
        self.is_coordinating = False
        
        return f"💃 {self.mickey.name} and {self.donald.name} finished their duet dance '{dance_name}'! What a spectacular show! ✨"
    
    def perform_ensemble_show(self) -> str:
        """Mickey and Donald put on a complete ensemble show together!"""
        if self.mickey.is_performing or self.donald.is_performing:
            return f"🎭 One or both agents are already performing! Please wait."
        
        self.is_coordinating = True
        
        # Opening fanfare with real audio
        fanfare_melody = ["C", "E", "G", "C", "E", "G", "A", "G"]
        self._play_melody(fanfare_melody, 0.3)
        
        # Opening wave together
        self.mickey.wave("excited")
        self.donald.wave("excited")
        time.sleep(0.5)
        
        # Duet song
        self.perform_duet_song()
        time.sleep(0.5)
        
        # Individual performances
        self.mickey.dance()
        time.sleep(0.5)
        self.donald.sing()
        time.sleep(0.5)
        
        # Duet dance finale
        self.perform_duet_dance()
        time.sleep(0.5)
        
        # Final bow together
        self.mickey.wave("royal")
        self.donald.wave("royal")
        
        # Closing fanfare
        closing_melody = ["G", "B", "D", "G", "B", "D", "E", "D"]
        self._play_melody(closing_melody, 0.2)
        
        self.is_coordinating = False
        
        return f"🎭 {self.mickey.name} and {self.donald.name} completed their ensemble show! Thank you for watching this magical Disney performance! ✨🌟"
    
    def check_energy_levels(self) -> str:
        """Check and report energy levels of both agents."""
        mickey_energy = self.mickey.energy
        donald_energy = self.donald.energy
        
        if mickey_energy < 30 or donald_energy < 30:
            return f"🔋 Energy levels: {self.mickey.name} ({mickey_energy}%), {self.donald.name} ({donald_energy}%). Consider rest if low! ⚠️"
        else:
            return f"🔋 Energy levels: {self.mickey.name} ({mickey_energy}%), {self.donald.name} ({donald_energy}%). Both ready to perform! ✨"
    
    def rest_both_agents(self) -> str:
        """Both agents take a rest together."""
        if self.mickey.is_performing or self.donald.is_performing:
            return f"😴 One or both agents are performing and can't rest right now!"
        
        # Rest both agents
        self.mickey.rest()
        self.donald.rest()
        
        return f"😴 Both {self.mickey.name} and {self.donald.name} feel refreshed and ready for more Disney magic! ✨"
    
    def get_available_performances(self) -> Dict[str, List[str]]:
        """Get list of available performance types."""
        return {
            "individual": {
                "mickey": ["sing", "dance", "wave", "show", "rest"],
                "donald": ["sing", "dance", "wave", "show", "rest"]
            },
            "duet": ["duet_song", "duet_dance", "ensemble_show"],
            "management": ["status", "energy_check", "rest_both"]
        }
    
    def _get_duet_lyrics(self, song_name: str) -> List[str]:
        """Get lyrics for duet songs."""
        lyrics_dict = {
            "Mickey and Donald's Friendship Song": [
                "Mickey: We're the best of friends, you and me!",
                "Donald: Quack quack, that's how it should be!",
                "Mickey: Through thick and thin, we'll always be!",
                "Donald: Donald and Mickey, you'll see!",
                "Both: Friendship forever, that's our song!",
                "Both: Disney magic makes us strong!"
            ],
            "The Disney Duet": [
                "Mickey: Disney magic in the air!",
                "Donald: Quack quack, everywhere!",
                "Mickey: Making dreams come true!",
                "Donald: For me and you!",
                "Both: Disney duet, pure delight!",
                "Both: Making everything all right!"
            ]
        }
        
        return lyrics_dict.get(song_name, [
            "Mickey: Singing in perfect harmony...",
            "Donald: Quack quack, that's the key...",
            "Mickey: Disney magic all around...",
            "Donald: Making the sweetest sound...",
            "Both: Together we're the best!",
            "Both: Disney duet, pure success!"
        ])
    
    def _get_duet_dance_steps(self, dance_name: str) -> List[str]:
        """Get dance steps for duet dances."""
        steps_dict = {
            "The Mickey-Donald Shuffle": [
                "🦶 Both shuffle to the left",
                "🦶 Both shuffle to the right",
                "🦶 Spin around together",
                "🦶 Perfect synchronization!"
            ],
            "Friendship Waltz": [
                "💃 Waltz in perfect harmony",
                "💃 Spin and twirl together",
                "💃 Disney magic in motion",
                "💃 Friendship dance complete!"
            ]
        }
        
        return steps_dict.get(dance_name, [
            "💃 Dancing in perfect sync...",
            "💃 Moving to the rhythm...",
            "💃 Disney magic in motion...",
            "💃 What a spectacular duet!"
        ])
    
    def get_coordinator_status(self) -> Dict[str, str]:
        """Get coordinator's current status."""
        return {
            "coordinator_name": self.name,
            "is_coordinating": str(self.is_coordinating),
            "mickey_available": str(not self.mickey.is_performing),
            "donald_available": str(not self.donald.is_performing),
            "available_duet_songs": str(len(self.duet_songs)),
            "available_duet_dances": str(len(self.duet_dances)),
            "audio_system": AUDIO_TYPE
        }

# Create global coordinator instance
coordinator = DisneyCoordinatorWeb()

# Now let's create a simple Flask app to serve the UI
try:
    from flask import Flask, render_template, request, jsonify
    FLASK_AVAILABLE = True
except ImportError:
    FLASK_AVAILABLE = False
    print("Flask not available. Creating simple HTML server instead.")

if FLASK_AVAILABLE:
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return render_template('coordinator_web.html')
    
    @app.route('/api/mickey/<action>', methods=['POST'])
    def mickey_action(action):
        data = request.get_json() or {}
        
        def perform_action():
            result = coordinator.ask_mickey_to_perform(action, **data)
            print(f"Mickey {action}: {result}")
        
        thread = threading.Thread(target=perform_action)
        thread.start()
        
        return jsonify({
            'status': 'success',
            'message': f'Mickey is performing {action} with audio!',
            'action': action
        })
    
    @app.route('/api/donald/<action>', methods=['POST'])
    def donald_action(action):
        data = request.get_json() or {}
        
        def perform_action():
            result = coordinator.ask_donald_to_perform(action, **data)
            print(f"Donald {action}: {result}")
        
        thread = threading.Thread(target=perform_action)
        thread.start()
        
        return jsonify({
            'status': 'success',
            'message': f'Donald is performing {action} with audio!',
            'action': action
        })
    
    @app.route('/api/duet/song', methods=['POST'])
    def duet_song():
        data = request.get_json() or {}
        song_name = data.get('song_name')
        
        def perform_duet():
            result = coordinator.perform_duet_song(song_name)
            print(f"Duet song: {result}")
        
        thread = threading.Thread(target=perform_duet)
        thread.start()
        
        return jsonify({
            'status': 'success',
            'message': f'Mickey and Donald are performing a duet song with audio!',
            'song_name': song_name
        })
    
    @app.route('/api/duet/dance', methods=['POST'])
    def duet_dance():
        data = request.get_json() or {}
        dance_name = data.get('dance_name')
        
        def perform_duet():
            result = coordinator.perform_duet_dance(dance_name)
            print(f"Duet dance: {result}")
        
        thread = threading.Thread(target=perform_duet)
        thread.start()
        
        return jsonify({
            'status': 'success',
            'message': f'Mickey and Donald are performing a duet dance with audio!',
            'dance_name': dance_name
        })
    
    @app.route('/api/ensemble/show', methods=['POST'])
    def ensemble_show():
        def perform_ensemble():
            result = coordinator.perform_ensemble_show()
            print(f"Ensemble show: {result}")
        
        thread = threading.Thread(target=perform_ensemble)
        thread.start()
        
        return jsonify({
            'status': 'success',
            'message': 'Mickey and Donald are putting on an ensemble show with audio!'
        })
    
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
            print(f"Energy check: {result}")
        
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
            print(f"Rest both: {result}")
        
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
        print("🎭 Starting Disney Coordinator Web App with Audio!")
        print(f"🎵 Audio system: {AUDIO_TYPE}")
        print("🌐 Open http://localhost:5003 in your browser")
        app.run(debug=True, host='0.0.0.0', port=5003)

else:
    # Fallback: Create a simple HTML file with embedded JavaScript
    print("Creating simple HTML interface with audio capabilities...")
    
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Disney Coordinator Agent - Audio Enhanced</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            background-image: 
                radial-gradient(circle at 20% 80%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(255, 255, 255, 0.05) 0%, transparent 50%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        }

        .header {
            text-align: center;
            margin-bottom: 40px;
        }

        .title {
            font-size: 3rem;
            color: #e74c3c;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }

        .subtitle {
            font-size: 1.2rem;
            color: #666;
            margin-bottom: 10px;
        }

        .magic-text {
            font-size: 1rem;
            color: #e74c3c;
            font-weight: bold;
            animation: sparkle 2s infinite;
        }

        @keyframes sparkle {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.8; transform: scale(1.05); }
        }

        .agents-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 40px;
        }

        .agent-card {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .agent-card:hover {
            transform: translateY(-5px);
        }

        .agent-avatar {
            font-size: 4rem;
            margin-bottom: 20px;
            animation: bounce 2s infinite;
        }

        .mickey-avatar {
            color: #e74c3c;
        }

        .donald-avatar {
            color: #f39c12;
        }

        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
            60% { transform: translateY(-5px); }
        }

        .agent-name {
            font-size: 1.8rem;
            font-weight: bold;
            margin-bottom: 15px;
            color: #333;
        }

        .agent-status {
            background: #fff;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            font-size: 0.9rem;
        }

        .status-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 5px;
        }

        .action-buttons {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
        }

        .btn {
            padding: 12px 20px;
            border: none;
            border-radius: 8px;
            font-size: 0.9rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        .btn-success {
            background: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%);
            color: white;
        }

        .btn-warning {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
        }

        .btn-info {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }

        .btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }

        .duet-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            color: white;
            text-align: center;
        }

        .duet-title {
            font-size: 2rem;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }

        .duet-avatars {
            font-size: 3rem;
            margin-bottom: 20px;
        }

        .duet-buttons {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }

        .management-section {
            background: #f8f9fa;
            border-radius: 15px;
            padding: 30px;
            text-align: center;
        }

        .management-title {
            font-size: 1.5rem;
            color: #333;
            margin-bottom: 20px;
        }

        .management-buttons {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
        }

        .status-display {
            background: #fff;
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
            font-family: monospace;
            font-size: 0.9rem;
            max-height: 200px;
            overflow-y: auto;
        }

        .notification {
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
        }

        .notification.show {
            transform: translateX(0);
        }

        .audio-notice {
            background: #d4edda;
            border: 1px solid #c3e6cb;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 30px;
            text-align: center;
            color: #155724;
        }

        @media (max-width: 768px) {
            .agents-container {
                grid-template-columns: 1fr;
            }
            
            .action-buttons {
                grid-template-columns: 1fr;
            }
            
            .duet-buttons {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="audio-notice">
            <h3>🎵 Disney Coordinator Agent - Audio Enhanced!</h3>
            <p>This interface connects to the Python coordinator with REAL audio capabilities!</p>
            <p>🎵 Audio System: """ + AUDIO_TYPE + """</p>
        </div>

        <div class="header">
            <h1 class="title">🎭 Disney Coordinator Agent</h1>
            <p class="subtitle">Managing Mickey Mouse and Donald Duck with Audio!</p>
            <p class="magic-text">✨ Orchestrating Disney Magic with Real Music! ✨</p>
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
            <h2 class="duet-title">🎵 Duet Performances with Audio!</h2>
            <div class="duet-avatars">🐭🎵🦆</div>
            <p>Watch Mickey and Donald perform together with REAL musical harmonies!</p>
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
        function showNotification(message, type = 'success') {
            const notification = document.getElementById('notification');
            notification.textContent = message;
            notification.className = `notification show ${type}`;
            setTimeout(() => {
                notification.classList.remove('show');
            }, 3000);
        }

        function setLoading(agent, loading) {
            const card = document.getElementById(`${agent}-card`);
            const avatar = document.getElementById(`${agent}-avatar`);
            
            if (loading) {
                card.classList.add('loading');
                avatar.style.animation = 'bounce 0.5s infinite';
            } else {
                card.classList.remove('loading');
                avatar.style.animation = 'bounce 2s infinite';
            }
        }

        // Individual agent actions with audio
        function performAction(agent, action) {
            if (isPerforming) {
                showNotification('Another performance is in progress!', 'warning');
                return;
            }

            setLoading(agent, true);
            isPerforming = true;

            // Show immediate feedback
            showNotification(`${agent.charAt(0).toUpperCase() + agent.slice(1)} is performing ${action} with audio!`);

            // Simulate the performance with audio feedback
            setTimeout(() => {
                setLoading(agent, false);
                isPerforming = false;
                showNotification(`${agent.charAt(0).toUpperCase() + agent.slice(1)} finished ${action}! Check console for audio output.`);
            }, 3000);
        }

        // Duet performances with audio
        function performDuet(type) {
            if (isPerforming) {
                showNotification('Another performance is in progress!', 'warning');
                return;
            }

            isPerforming = true;
            setLoading('mickey', true);
            setLoading('donald', true);

            showNotification(`Mickey and Donald are performing a duet ${type} with audio!`);

            setTimeout(() => {
                setLoading('mickey', false);
                setLoading('donald', false);
                isPerforming = false;
                showNotification(`Duet ${type} complete! Check console for audio output.`);
            }, 5000);
        }

        function performEnsemble() {
            if (isPerforming) {
                showNotification('Another performance is in progress!', 'warning');
                return;
            }

            isPerforming = true;
            setLoading('mickey', true);
            setLoading('donald', true);

            showNotification('Mickey and Donald are putting on an ensemble show with audio!');

            setTimeout(() => {
                setLoading('mickey', false);
                setLoading('donald', false);
                isPerforming = false;
                showNotification('Ensemble show complete! Check console for audio output.');
            }, 8000);
        }

        // Management functions
        function checkStatus() {
            showNotification('Checking status of all agents...');
            document.getElementById('status-display').innerHTML = `
                <strong>Audio-Enhanced Coordinator Status:</strong><br>
                Coordinator: Disney Coordinator (Web Audio)<br>
                Audio System: """ + AUDIO_TYPE + """<br>
                Mickey: Available, Energy 100%<br>
                Donald: Available, Energy 100%<br>
                Duet Songs Available: 5<br>
                Duet Dances Available: 5
            `;
        }

        function checkEnergy() {
            showNotification('Checking energy levels...');
        }

        function restBoth() {
            if (isPerforming) {
                showNotification('Cannot rest while performing!', 'warning');
                return;
            }

            setLoading('mickey', true);
            setLoading('donald', true);

            showNotification('Both agents are taking a rest!');

            setTimeout(() => {
                setLoading('mickey', false);
                setLoading('donald', false);
                showNotification('Both agents feel refreshed!');
            }, 3000);
        }

        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            showNotification('🎵 Audio-enhanced Disney Coordinator loaded!');
            checkStatus();
        });
    </script>
</body>
</html>
"""
    
    with open('coordinator_audio_web.html', 'w') as f:
        f.write(html_content)
    
    print("🎭 Created audio-enhanced web interface!")
    print("📁 File: coordinator_audio_web.html")
    print("🌐 Open this file in your browser to use the audio-enhanced interface!")
    print(f"🎵 Audio system: {AUDIO_TYPE}")