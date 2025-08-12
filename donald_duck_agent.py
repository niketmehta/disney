import time
import random
from typing import List, Dict, Optional
import threading
import os

class DonaldDuckAgent:
    """
    Donald Duck Agent - A feisty and energetic character that can sing, wave, and dance!
    """
    
    def __init__(self):
        self.name = "Donald Duck"
        self.mood = "energetic"
        self.energy = 100
        self.is_performing = False
        
        self.songs = [
            "Quack Quack Quack",
            "Donald's Theme Song",
            "The Duck March",
            "Quack Attack",
            "Duck Tales Theme",
            "Donald's Lullaby"
        ]
        
        self.dance_moves = [
            "The Donald Shuffle",
            "The Quack Attack",
            "The Duck Waddle",
            "The Feisty Fling",
            "The Donald Spin",
            "The Duck Bounce"
        ]
        
    def sing(self, song_name: Optional[str] = None) -> str:
        """Donald sings a song with his unique style!"""
        if self.is_performing:
            return f"🎵 {self.name} is already performing! Please wait."
        
        if song_name is None:
            song_name = random.choice(self.songs)
        
        self.is_performing = True
        self.energy -= 10
        
        lyrics = self._get_song_lyrics(song_name)
        
        # Simulate singing performance with visual feedback
        print(f"🎤 {self.name} starts singing '{song_name}'...")
        print(f"   🦆 Donald's unique quacking style! ✨")
        for i, line in enumerate(lyrics):
            # Add visual feedback with emojis
            visual_feedback = "🦆" if i % 2 == 0 else "🎤"
            print(f"   {visual_feedback} {line}")
            time.sleep(0.8)  # Slower for better visual effect
        
        print(f"   🌟 Quack-tastic performance! 👏")
        self.is_performing = False
        return f"🎵 {self.name} finished singing '{song_name}'! What a quack-tastic performance! ✨"
    
    def wave(self, style: str = "friendly") -> str:
        """Donald waves hello with his energetic style!"""
        if self.is_performing:
            return f"👋 {self.name} is busy performing! Please wait."
        
        wave_styles = {
            "friendly": ["🦆", "🦆", "🦆", "🦆", "🦆"],
            "excited": ["🦆✨", "🦆✨", "🦆✨", "🦆✨", "🦆✨"],
            "royal": ["🦆👑", "🦆👑", "🦆👑", "🦆👑", "🦆👑"],
            "magical": ["🦆✨🌟", "🦆✨🌟", "🦆✨🌟", "🦆✨🌟", "🦆✨🌟"],
            "goofy": ["🦆🤪", "🦆🤪", "🦆🤪", "🦆🤪", "🦆🤪"]
        }
        
        wave_sequence = wave_styles.get(style, wave_styles["friendly"])
        
        print(f"👋 {self.name} waves {style}ly!")
        print(f"   🦆 Donald's energetic charm! ✨")
        
        # Animated wave sequence
        for wave_emoji in wave_sequence:
            print(f"   {wave_emoji}")
            time.sleep(0.3)
        
        return f"👋 Hi there! {self.name} says hello with a {style} wave! 🌟"
    
    def dance(self, dance_move: Optional[str] = None) -> str:
        """Donald dances with his energetic style!"""
        if self.is_performing:
            return f"💃 {self.name} is already performing! Please wait."
        
        if dance_move is None:
            dance_move = random.choice(self.dance_moves)
        
        self.is_performing = True
        self.energy -= 15
        
        print(f"💃 {self.name} starts dancing the '{dance_move}'...")
        print(f"   🦆 Donald's energetic rhythm! ✨")
        
        # Simulate dance performance with visual feedback
        dance_steps = self._get_dance_steps(dance_move)
        for i, step in enumerate(dance_steps):
            # Add visual feedback with emojis
            visual_feedback = "🦆" if i % 2 == 0 else "💃"
            print(f"   {visual_feedback} {step}")
            time.sleep(0.6)  # Slower for better visual effect
        
        print(f"   🌟 Quack-tastic dance moves! 👏")
        self.is_performing = False
        return f"💃 {self.name} finished the '{dance_move}'! What a quack-tastic show! ✨"
    
    def perform_show(self) -> str:
        """Donald puts on a complete show with singing, waving, and dancing!"""
        if self.is_performing:
            return f"🎭 {self.name} is already performing! Please wait."
        
        self.is_performing = True
        print(f"🎭 {self.name} is putting on a spectacular Donald show!")
        print(f"   ✨ The quack-tastic magic begins... 🌟")
        
        # Wave to the audience
        print("🎭 Opening with a wave to the audience...")
        self.wave("excited")
        time.sleep(0.5)
        
        # Sing a song
        print("🎭 Now for the musical performance...")
        self.sing()
        time.sleep(0.5)
        
        # Dance
        print("🎭 And now for the dance finale...")
        self.dance()
        time.sleep(0.5)
        
        # Final wave
        print("🎭 Final bow and wave...")
        self.wave("royal")
        
        print(f"   🌟 Standing ovation for Donald! 👏✨")
        self.is_performing = False
        return f"🎭 {self.name} completed the show! Thank you for watching this quack-tastic performance! ✨🌟"
    
    def _get_song_lyrics(self, song_name: str) -> List[str]:
        """Get lyrics for a specific song."""
        lyrics_dict = {
            "Quack Quack Quack": [
                "Quack quack quack, here comes Donald!",
                "Quack quack quack, he's the best!",
                "Quack quack quack, full of energy!",
                "Quack quack quack, never at rest!"
            ],
            "Donald's Theme Song": [
                "I'm Donald Duck, that's who I am!",
                "Energetic, feisty, that's my plan!",
                "I may get mad, but I'm still your friend!",
                "Donald Duck until the very end!"
            ],
            "The Duck March": [
                "Marching ducks, one by one!",
                "Donald leads the way with fun!",
                "Quack quack quack, we're on our way!",
                "Donald Duck saves the day!"
            ]
        }
        
        return lyrics_dict.get(song_name, [
            "🦆 Quack quack quack...",
            "🦆 Singing with Donald's style...",
            "🦆 Making everyone smile...",
            "🦆 That's the magic of Donald!"
        ])
    
    def _get_dance_steps(self, dance_move: str) -> List[str]:
        """Get dance steps for a specific move."""
        steps_dict = {
            "The Donald Shuffle": [
                "🦶 Waddle to the left",
                "🦶 Waddle to the right",
                "🦶 Shuffle those webbed feet",
                "🦶 Spin around with might!"
            ],
            "The Quack Attack": [
                "🦆 Arms up high",
                "🦆 Wiggle that tail",
                "🦆 Jump and quack",
                "🦆 Quack attack complete!"
            ],
            "The Duck Waddle": [
                "🦆 Start the waddle",
                "🦆 Side to side",
                "🦆 Faster and faster",
                "🦆 Donald's waddle complete!"
            ]
        }
        
        return steps_dict.get(dance_move, [
            "🦆 Dancing with Donald's style...",
            "🦆 Moving to the rhythm...",
            "🦆 Spinning and waddling...",
            "🦆 What a quack-tastic dance!"
        ])
    
    def get_status(self) -> Dict[str, str]:
        """Get Donald's current status."""
        return {
            "name": self.name,
            "mood": self.mood,
            "energy": f"{self.energy}%",
            "is_performing": str(self.is_performing),
            "available_songs": str(len(self.songs)),
            "available_dances": str(len(self.dance_moves))
        }
    
    def rest(self) -> str:
        """Donald takes a rest to regain energy."""
        if self.is_performing:
            return f"😴 {self.name} is performing and can't rest right now!"
        
        old_energy = self.energy
        self.energy = min(100, self.energy + 30)
        
        print(f"😴 {self.name} takes a nice Donald rest...")
        print(f"   ✨ Sweet dreams and quacks... 🌟")
        
        # Visual rest sequence
        rest_emojis = ["😴", "😴", "😴", "😴", "😴"]
        for emoji in rest_emojis:
            print(f"   {emoji}")
            time.sleep(0.5)
        
        return f"😴 {self.name} feels refreshed and ready for more quack-tastic adventures! Energy: {old_energy}% → {self.energy}% ✨"