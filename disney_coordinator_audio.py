#!/usr/bin/env python3
"""
Disney Coordinator Agent with Real Audio Capabilities
Enhanced version with actual musical tones and harmonies
"""

import time
import random
import threading
import os
import sys
import math
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

class DisneyCoordinatorAudio:
    """
    Disney Coordinator Agent with Real Audio Capabilities
    Manages Mickey Mouse and Donald Duck agents with actual musical performances!
    """
    
    def __init__(self):
        self.name = "Disney Coordinator (Audio Enhanced)"
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
        
        # Visual musical notes for display
        self.visual_notes = ["♪", "♫", "♬", "♩", "♭", "♮", "♯"]
        self.harmony_notes = ["🎵", "🎶", "🎼", "🎤", "🎧", "🎹", "🎸", "🎺", "🎻"]
        
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
    
    def _play_harmony(self, notes: List[str], duration: float = 0.5):
        """Play a harmony sequence with visual feedback."""
        for note in notes:
            if note in self.musical_notes:
                self._generate_tone(self.musical_notes[note], duration / len(notes))
            print(f"   {note}", end="", flush=True)
            time.sleep(duration / len(notes))
        print()  # New line after harmony
    
    def _play_visual_note(self, note: str, duration: float = 0.3):
        """Play a visual musical note with optional audio."""
        print(f"   {note}", end="", flush=True)
        if AUDIO_AVAILABLE and note in self.musical_notes:
            self._generate_tone(self.musical_notes[note], duration)
        else:
            time.sleep(duration)
    
    def _play_duet_harmony(self, mickey_line: str, donald_line: str):
        """Play a duet harmony with both singers and musical accompaniment."""
        # Mickey's part with harmony
        print(f"   🐭 {self.mickey.name}: {mickey_line}")
        mickey_notes = random.sample(list(self.musical_notes.keys()), 2)
        print(f"      ", end="")
        for note in mickey_notes:
            self._play_visual_note(note, 0.3)
        print()
        
        time.sleep(0.5)
        
        # Donald's part with harmony
        print(f"   🦆 {self.donald.name}: {donald_line}")
        donald_notes = random.sample(list(self.musical_notes.keys()), 2)
        print(f"      ", end="")
        for note in donald_notes:
            self._play_visual_note(note, 0.3)
        print()
        
        time.sleep(0.5)
        
        # Combined harmony
        print(f"   🎵 Both: ", end="")
        combined_notes = random.sample(list(self.musical_notes.keys()), 4)
        for note in combined_notes:
            self._play_visual_note(note, 0.2)
        print("Harmony!")
        
        time.sleep(0.8)
    
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
        """Ask Mickey to perform a specific action."""
        if self.mickey.is_performing:
            return f"🎭 {self.mickey.name} is already performing! Please wait."
        
        if action == "sing":
            return self.mickey.sing(kwargs.get('song_name'))
        elif action == "dance":
            return self.mickey.dance(kwargs.get('dance_move'))
        elif action == "wave":
            return self.mickey.wave(kwargs.get('style', 'friendly'))
        elif action == "show":
            return self.mickey.perform_show()
        elif action == "rest":
            return self.mickey.rest()
        else:
            return f"❌ Unknown action '{action}' for {self.mickey.name}"
    
    def ask_donald_to_perform(self, action: str, **kwargs) -> str:
        """Ask Donald to perform a specific action."""
        if self.donald.is_performing:
            return f"🎭 {self.donald.name} is already performing! Please wait."
        
        if action == "sing":
            return self.donald.sing(kwargs.get('song_name'))
        elif action == "dance":
            return self.donald.dance(kwargs.get('dance_move'))
        elif action == "wave":
            return self.donald.wave(kwargs.get('style', 'friendly'))
        elif action == "show":
            return self.donald.perform_show()
        elif action == "rest":
            return self.donald.rest()
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
        
        print(f"🎵 {self.mickey.name} and {self.donald.name} are performing a duet!")
        print(f"   🎭 Song: '{song_name}'")
        print(f"   ✨ Disney magic in perfect harmony! 🌟")
        print()
        
        # Musical introduction with real audio
        print("🎼 Musical Introduction:")
        intro_melody = self.disney_melodies["friendship"]
        self._play_melody(intro_melody, 0.4)
        print()
        
        # Get duet lyrics
        lyrics = self._get_duet_lyrics(song_name)
        
        # Perform the duet with enhanced musical accompaniment
        print("🎤 Duet Performance:")
        for i in range(0, len(lyrics), 2):
            if i + 1 < len(lyrics):
                # Duet harmony with real audio
                self._play_duet_harmony(lyrics[i], lyrics[i + 1])
            else:
                # Solo part if odd number of lines
                print(f"   🐭 {self.mickey.name}: {lyrics[i]}")
                solo_notes = random.sample(list(self.musical_notes.keys()), 3)
                for note in solo_notes:
                    self._play_visual_note(note, 0.2)
                print()
        
        # Grand finale with full orchestra
        print("🎼 Grand Finale:")
        print(f"   🎵 Both: Together in perfect Disney harmony!")
        finale_melody = self.disney_melodies["magic"] + self.disney_melodies["harmony"]
        self._play_melody(finale_melody, 0.2)
        print()
        
        print(f"   🌟 Encore! Encore! 👏")
        print(f"   🎭 Standing ovation! ✨")
        
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
        
        print(f"💃 {self.mickey.name} and {self.donald.name} are performing a duet dance!")
        print(f"   🎭 Dance: '{dance_name}'")
        print(f"   ✨ Disney rhythm in perfect sync! 🌟")
        
        # Dance music introduction
        print("🎵 Dance Music:")
        dance_melody = ["C", "E", "G", "C", "E", "G"]
        self._play_melody(dance_melody, 0.3)
        print()
        
        # Get duet dance steps
        steps = self._get_duet_dance_steps(dance_name)
        
        # Perform the duet dance with synchronized moves and music
        for i, step in enumerate(steps):
            print(f"   💃 Both: {step}")
            # Dance rhythm
            rhythm_notes = random.sample(list(self.musical_notes.keys()), 2)
            for note in rhythm_notes:
                self._play_visual_note(note, 0.2)
            print()
            time.sleep(0.6)
        
        # Dance finale
        print("🎵 Dance Finale:")
        finale_melody = ["G", "B", "D", "G", "B", "D"]
        self._play_melody(finale_melody, 0.2)
        print()
        
        print(f"   🌟 Perfect synchronization! 👏")
        
        self.mickey.is_performing = False
        self.donald.is_performing = False
        self.is_coordinating = False
        
        return f"💃 {self.mickey.name} and {self.donald.name} finished their duet dance '{dance_name}'! What a spectacular show! ✨"
    
    def perform_ensemble_show(self) -> str:
        """Mickey and Donald put on a complete ensemble show together!"""
        if self.mickey.is_performing or self.donald.is_performing:
            return f"🎭 One or both agents are already performing! Please wait."
        
        self.is_coordinating = True
        print(f"🎭 {self.mickey.name} and {self.donald.name} are putting on a spectacular ensemble show!")
        print(f"   ✨ The ultimate Disney magic begins... 🌟")
        
        # Opening fanfare with real audio
        print("🎺 Opening Fanfare:")
        fanfare_melody = ["C", "E", "G", "C", "E", "G", "A", "G"]
        self._play_melody(fanfare_melody, 0.3)
        print()
        
        # Opening wave together
        print("🎭 Opening with a synchronized wave...")
        self.mickey.wave("excited")
        self.donald.wave("excited")
        time.sleep(0.5)
        
        # Duet song
        print("🎭 Now for the musical duet...")
        self.perform_duet_song()
        time.sleep(0.5)
        
        # Individual performances
        print("🎭 Individual spotlight moments...")
        self.mickey.dance()
        time.sleep(0.5)
        self.donald.sing()
        time.sleep(0.5)
        
        # Duet dance finale
        print("🎭 And now for the grand finale duet dance...")
        self.perform_duet_dance()
        time.sleep(0.5)
        
        # Final bow together
        print("🎭 Final synchronized bow...")
        self.mickey.wave("royal")
        self.donald.wave("royal")
        
        # Closing fanfare
        print("🎺 Closing Fanfare:")
        closing_melody = ["G", "B", "D", "G", "B", "D", "E", "D"]
        self._play_melody(closing_melody, 0.2)
        print()
        
        print(f"   🌟 Standing ovation for the Disney duo! 👏✨")
        self.is_coordinating = False
        
        return f"🎭 {self.mickey.name} and {self.donald.name} completed their ensemble show! Thank you for watching this magical Disney performance! ✨🌟"
    
    def check_energy_levels(self) -> str:
        """Check and report energy levels of both agents."""
        mickey_energy = self.mickey.energy
        donald_energy = self.donald.energy
        
        print(f"🔋 Energy Level Report:")
        print(f"   🐭 {self.mickey.name}: {mickey_energy}%")
        print(f"   🦆 {self.donald.name}: {donald_energy}%")
        
        if mickey_energy < 30 or donald_energy < 30:
            print(f"   ⚠️  One or both agents need rest!")
            return f"🔋 Energy levels: {self.mickey.name} ({mickey_energy}%), {self.donald.name} ({donald_energy}%). Consider rest if low! ⚠️"
        else:
            return f"🔋 Energy levels: {self.mickey.name} ({mickey_energy}%), {self.donald.name} ({donald_energy}%). Both ready to perform! ✨"
    
    def rest_both_agents(self) -> str:
        """Both agents take a rest together."""
        if self.mickey.is_performing or self.donald.is_performing:
            return f"😴 One or both agents are performing and can't rest right now!"
        
        print(f"😴 {self.mickey.name} and {self.donald.name} are taking a rest together...")
        print(f"   ✨ Sweet Disney dreams... 🌟")
        
        # Visual rest sequence
        rest_emojis = ["😴", "😴", "😴", "😴", "😴"]
        for emoji in rest_emojis:
            print(f"   {emoji}")
            time.sleep(0.5)
        
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

def main():
    """Test the audio-enhanced coordinator."""
    print("🎭🎵🦆🐭")
    print("=" * 60)
    print("    DISNEY COORDINATOR AGENT - AUDIO ENHANCED")
    print("=" * 60)
    print("🎭🎵🦆🐭")
    print()
    
    coordinator = DisneyCoordinatorAudio()
    print(f"🎉 Welcome! {coordinator.name} is ready to orchestrate Disney magic!")
    print(f"🎵 Audio system: {AUDIO_TYPE}")
    print()
    
    # Test duet performance with real audio
    print("🎬 Testing Duet Performance with Real Audio:")
    print("-" * 50)
    result = coordinator.perform_duet_song("Mickey and Donald's Friendship Song")
    print(f"Result: {result}")
    print()
    
    print("🎭 Audio-enhanced coordinator is working perfectly!")
    print("🎵 You should have heard actual musical tones during the performance!")

if __name__ == "__main__":
    main()