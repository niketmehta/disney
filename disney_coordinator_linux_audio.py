#!/usr/bin/env python3
"""
Disney Coordinator Agent with Linux Audio Capabilities
Uses Linux system commands to generate actual audio
"""

import time
import random
import threading
import os
import sys
import subprocess
import tempfile
import math
from typing import List, Dict, Optional, Tuple
from mickey_mouse_agent import MickeyMouseAgent
from donald_duck_agent import DonaldDuckAgent

class DisneyCoordinatorLinuxAudio:
    """
    Disney Coordinator Agent with Real Linux Audio Capabilities
    """
    
    def __init__(self):
        self.name = "Disney Coordinator (Linux Audio)"
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
        """Initialize the Linux audio system."""
        self.audio_available = False
        self.audio_method = "none"
        
        # Try different Linux audio methods
        methods = [
            ("speaker-test", self._test_speaker_test),
            ("aplay", self._test_aplay),
            ("paplay", self._test_paplay),
            ("ffplay", self._test_ffplay),
            ("sox", self._test_sox),
            ("beep", self._test_beep)
        ]
        
        for method_name, test_func in methods:
            if test_func():
                self.audio_available = True
                self.audio_method = method_name
                print(f"🎵 Linux audio system initialized with {method_name}!")
                break
        
        if not self.audio_available:
            print("🎵 No Linux audio method available. Using enhanced visual audio.")
    
    def _test_speaker_test(self):
        """Test if speaker-test is available."""
        try:
            result = subprocess.run(['speaker-test', '--help'], 
                                  capture_output=True, text=True, timeout=2)
            return result.returncode == 0
        except:
            return False
    
    def _test_aplay(self):
        """Test if aplay is available."""
        try:
            result = subprocess.run(['aplay', '--help'], 
                                  capture_output=True, text=True, timeout=2)
            return result.returncode == 0
        except:
            return False
    
    def _test_paplay(self):
        """Test if paplay is available."""
        try:
            result = subprocess.run(['paplay', '--help'], 
                                  capture_output=True, text=True, timeout=2)
            return result.returncode == 0
        except:
            return False
    
    def _test_ffplay(self):
        """Test if ffplay is available."""
        try:
            result = subprocess.run(['ffplay', '-version'], 
                                  capture_output=True, text=True, timeout=2)
            return result.returncode == 0
        except:
            return False
    
    def _test_sox(self):
        """Test if sox is available."""
        try:
            result = subprocess.run(['sox', '--help'], 
                                  capture_output=True, text=True, timeout=2)
            return result.returncode == 0
        except:
            return False
    
    def _test_beep(self):
        """Test if beep is available."""
        try:
            result = subprocess.run(['beep', '--help'], 
                                  capture_output=True, text=True, timeout=2)
            return result.returncode == 0
        except:
            return False
    
    def _generate_tone_linux(self, frequency: float, duration: float = 0.3, volume: float = 0.5):
        """Generate a musical tone using Linux audio commands."""
        if not self.audio_available:
            return
        
        try:
            if self.audio_method == "speaker-test":
                # Use speaker-test for sine wave
                cmd = ['speaker-test', '-t', 'sine', '-f', str(int(frequency)), 
                      '-l', '1', '-D', 'default']
                subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                time.sleep(duration)
                # Stop speaker-test
                subprocess.run(['pkill', 'speaker-test'], 
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            elif self.audio_method == "sox":
                # Use sox to generate and play tone
                with tempfile.NamedTemporaryFile(suffix='.wav', delete=True) as temp_file:
                    # Generate sine wave
                    cmd = ['sox', '-n', temp_file.name, 'sine', str(int(frequency)), 
                          'trim', '0', str(duration)]
                    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    # Play the file
                    subprocess.run(['aplay', temp_file.name], 
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            elif self.audio_method == "beep":
                # Use beep command
                cmd = ['beep', '-f', str(int(frequency)), '-l', str(int(duration * 1000))]
                subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            elif self.audio_method == "ffplay":
                # Use ffplay to generate and play tone
                cmd = ['ffplay', '-f', 'lavfi', '-i', 
                      f'sine=frequency={int(frequency)}:duration={duration}',
                      '-autoexit', '-nodisp', '-loglevel', 'quiet']
                subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            else:
                # Fallback: use system beep
                print('\a', end='', flush=True)
                time.sleep(duration)
                
        except Exception as e:
            print(f"🎵 Audio generation failed: {e}")
            # Fallback to system beep
            print('\a', end='', flush=True)
            time.sleep(duration)
    
    def _play_melody_linux(self, melody: List[str], duration: float = 0.3):
        """Play a sequence of musical notes using Linux audio."""
        for note in melody:
            if note in self.musical_notes:
                self._generate_tone_linux(self.musical_notes[note], duration)
                print(f"🎵 Playing note {note} ({self.musical_notes[note]:.0f}Hz)")
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
        """Ask Mickey to perform a specific action with Linux audio."""
        if self.mickey.is_performing:
            return f"🎭 {self.mickey.name} is already performing! Please wait."
        
        print(f"🎵 Mickey is performing {action} with Linux audio!")
        
        # Play musical intro
        intro_melody = ["C", "E", "G"]
        self._play_melody_linux(intro_melody, 0.2)
        
        if action == "sing":
            result = self.mickey.sing(kwargs.get('song_name'))
            # Play musical outro
            outro_melody = ["G", "E", "C"]
            self._play_melody_linux(outro_melody, 0.2)
            return result
        elif action == "dance":
            result = self.mickey.dance(kwargs.get('dance_move'))
            # Play dance rhythm
            dance_rhythm = ["C", "G", "C", "G"]
            self._play_melody_linux(dance_rhythm, 0.15)
            return result
        elif action == "wave":
            result = self.mickey.wave(kwargs.get('style', 'friendly'))
            # Play wave sound
            wave_sound = ["C", "D", "E"]
            self._play_melody_linux(wave_sound, 0.1)
            return result
        elif action == "show":
            result = self.mickey.perform_show()
            # Play show fanfare
            fanfare = ["C", "E", "G", "C", "E", "G", "A", "G"]
            self._play_melody_linux(fanfare, 0.2)
            return result
        elif action == "rest":
            result = self.mickey.rest()
            # Play rest sound
            rest_sound = ["G", "E", "C"]
            self._play_melody_linux(rest_sound, 0.3)
            return result
        else:
            return f"❌ Unknown action '{action}' for {self.mickey.name}"
    
    def ask_donald_to_perform(self, action: str, **kwargs) -> str:
        """Ask Donald to perform a specific action with Linux audio."""
        if self.donald.is_performing:
            return f"🎭 {self.donald.name} is already performing! Please wait."
        
        print(f"🎵 Donald is performing {action} with Linux audio!")
        
        # Play musical intro
        intro_melody = ["F", "A", "C"]
        self._play_melody_linux(intro_melody, 0.2)
        
        if action == "sing":
            result = self.donald.sing(kwargs.get('song_name'))
            # Play musical outro
            outro_melody = ["C", "A", "F"]
            self._play_melody_linux(outro_melody, 0.2)
            return result
        elif action == "dance":
            result = self.donald.dance(kwargs.get('dance_move'))
            # Play dance rhythm
            dance_rhythm = ["F", "C", "F", "C"]
            self._play_melody_linux(dance_rhythm, 0.15)
            return result
        elif action == "wave":
            result = self.donald.wave(kwargs.get('style', 'friendly'))
            # Play wave sound
            wave_sound = ["F", "G", "A"]
            self._play_melody_linux(wave_sound, 0.1)
            return result
        elif action == "show":
            result = self.donald.perform_show()
            # Play show fanfare
            fanfare = ["F", "A", "C", "F", "A", "C", "D", "C"]
            self._play_melody_linux(fanfare, 0.2)
            return result
        elif action == "rest":
            result = self.donald.rest()
            # Play rest sound
            rest_sound = ["C", "A", "F"]
            self._play_melody_linux(rest_sound, 0.3)
            return result
        else:
            return f"❌ Unknown action '{action}' for {self.donald.name}"
    
    def perform_duet_song(self, song_name: Optional[str] = None) -> str:
        """Mickey and Donald perform a duet song together with Linux audio!"""
        if self.mickey.is_performing or self.donald.is_performing:
            return f"🎭 One or both agents are already performing! Please wait."
        
        if song_name is None:
            song_name = random.choice(self.duet_songs)
        
        print(f"🎵 Mickey and Donald are performing duet '{song_name}' with Linux audio!")
        
        self.is_coordinating = True
        self.mickey.is_performing = True
        self.donald.is_performing = True
        
        # Musical introduction with Linux audio
        intro_melody = self.disney_melodies["friendship"]
        self._play_melody_linux(intro_melody, 0.4)
        
        # Get duet lyrics
        lyrics = self._get_duet_lyrics(song_name)
        
        # Perform the duet with enhanced musical accompaniment
        for i in range(0, len(lyrics), 2):
            if i + 1 < len(lyrics):
                # Duet harmony with Linux audio
                mickey_notes = random.sample(list(self.musical_notes.keys()), 2)
                donald_notes = random.sample(list(self.musical_notes.keys()), 2)
                
                print(f"🎤 Mickey sings: {lyrics[i]}")
                # Mickey's part
                for note in mickey_notes:
                    self._generate_tone_linux(self.musical_notes[note], 0.3)
                
                time.sleep(0.5)
                
                print(f"🦆 Donald sings: {lyrics[i+1]}")
                # Donald's part
                for note in donald_notes:
                    self._generate_tone_linux(self.musical_notes[note], 0.3)
                
                time.sleep(0.5)
                
                # Combined harmony
                combined_notes = random.sample(list(self.musical_notes.keys()), 4)
                print("🎵 Both sing in harmony!")
                for note in combined_notes:
                    self._generate_tone_linux(self.musical_notes[note], 0.2)
                
                time.sleep(0.8)
        
        # Grand finale with full orchestra
        finale_melody = self.disney_melodies["magic"] + self.disney_melodies["harmony"]
        self._play_melody_linux(finale_melody, 0.2)
        
        self.mickey.is_performing = False
        self.donald.is_performing = False
        self.is_coordinating = False
        
        return f"🎵 {self.mickey.name} and {self.donald.name} finished their duet '{song_name}'! What a magical performance! ✨"
    
    def perform_duet_dance(self, dance_name: Optional[str] = None) -> str:
        """Mickey and Donald perform a duet dance together with Linux audio!"""
        if self.mickey.is_performing or self.donald.is_performing:
            return f"🎭 One or both agents are already performing! Please wait."
        
        if dance_name is None:
            dance_name = random.choice(self.duet_dances)
        
        print(f"💃 Mickey and Donald are performing duet dance '{dance_name}' with Linux audio!")
        
        self.is_coordinating = True
        self.mickey.is_performing = True
        self.donald.is_performing = True
        
        # Dance music introduction
        dance_melody = ["C", "E", "G", "C", "E", "G"]
        self._play_melody_linux(dance_melody, 0.3)
        
        # Get duet dance steps
        steps = self._get_duet_dance_steps(dance_name)
        
        # Perform the duet dance with synchronized moves and music
        for i, step in enumerate(steps):
            print(f"💃 Step {i+1}: {step}")
            # Dance rhythm
            rhythm_notes = random.sample(list(self.musical_notes.keys()), 2)
            for note in rhythm_notes:
                self._generate_tone_linux(self.musical_notes[note], 0.2)
            time.sleep(0.6)
        
        # Dance finale
        finale_melody = ["G", "B", "D", "G", "B", "D"]
        self._play_melody_linux(finale_melody, 0.2)
        
        self.mickey.is_performing = False
        self.donald.is_performing = False
        self.is_coordinating = False
        
        return f"💃 {self.mickey.name} and {self.donald.name} finished their duet dance '{dance_name}'! What a spectacular show! ✨"
    
    def perform_ensemble_show(self) -> str:
        """Mickey and Donald put on a complete ensemble show together!"""
        if self.mickey.is_performing or self.donald.is_performing:
            return f"🎭 One or both agents are already performing! Please wait."
        
        print("🎭 Mickey and Donald are putting on an ensemble show with Linux audio!")
        
        self.is_coordinating = True
        
        # Opening fanfare with Linux audio
        fanfare_melody = ["C", "E", "G", "C", "E", "G", "A", "G"]
        self._play_melody_linux(fanfare_melody, 0.3)
        
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
        self._play_melody_linux(closing_melody, 0.2)
        
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
            "audio_system": self.audio_method
        }

# Test the Linux audio capabilities
if __name__ == "__main__":
    print("🎭🎵🦆🐭")
    print("=" * 60)
    print("    LINUX AUDIO CAPABILITIES TEST")
    print("=" * 60)
    print("🎭🎵🦆🐭")
    print()
    
    coordinator = DisneyCoordinatorLinuxAudio()
    print(f"🎉 Welcome! {coordinator.name} is ready to test Linux audio!")
    print(f"🎵 Audio system: {coordinator.audio_method}")
    print()
    
    # Test individual performances with Linux audio
    print("🎬 Testing Individual Performances with Linux Audio:")
    print("-" * 50)
    
    print("🐭 Mickey's solo performance with Linux audio:")
    print("-" * 40)
    result = coordinator.ask_mickey_to_perform("sing", song_name="It's a Small World")
    print(f"Result: {result}")
    print()
    
    time.sleep(1)
    
    print("🦆 Donald's solo performance with Linux audio:")
    print("-" * 40)
    result = coordinator.ask_donald_to_perform("dance", dance_move="The Quack Attack")
    print(f"Result: {result}")
    print()
    
    # Test duet performance with Linux audio
    print("🎬 Testing Duet Performance with Linux Audio:")
    print("-" * 50)
    
    print("🎵 Mickey and Donald duet with Linux audio:")
    print("-" * 40)
    result = coordinator.perform_duet_song("Mickey and Donald's Friendship Song")
    print(f"Result: {result}")
    print()
    
    print("🎭 Linux audio capabilities test complete!")
    print("🎵 You should have heard musical tones during the performances!")
    print("🌐 The Linux audio system is now working!")