import time
import random
from typing import List, Dict, Optional
import threading
import os

class MickeyMouseAgent:
    """
    Mickey Mouse Agent - A delightful character that can sing, wave, and dance!
    """
    
    def __init__(self):
        self.name = "Mickey Mouse"
        self.mood = "happy"
        self.energy = 100
        self.is_performing = False
        
        self.songs = [
            "It's a Small World",
            "When You Wish Upon a Star", 
            "Mickey Mouse Club March",
            "Zip-a-Dee-Doo-Dah",
            "Heigh-Ho",
            "Whistle While You Work"
        ]
        
        self.dance_moves = [
            "The Mickey Shuffle",
            "The Hot Dog Dance", 
            "The Sorcerer's Apprentice Spin",
            "The Steamboat Willie Jig",
            "The Fantasia Waltz",
            "The Clubhouse Bounce"
        ]
        
    def sing(self, song_name: Optional[str] = None) -> str:
        """Mickey sings a song!"""
        if self.is_performing:
            return f"🎵 {self.name} is already performing! Please wait."
        
        if song_name is None:
            song_name = random.choice(self.songs)
        
        self.is_performing = True
        self.energy -= 10
        
        lyrics = self._get_song_lyrics(song_name)
        
        # Simulate singing performance with visual feedback
        print(f"🎤 {self.name} starts singing '{song_name}'...")
        print(f"   🎭 Disney magic in the air! ✨")
        for i, line in enumerate(lyrics):
            # Add visual feedback with emojis
            visual_feedback = "🎵" if i % 2 == 0 else "🎤"
            print(f"   {visual_feedback} {line}")
            time.sleep(0.8)  # Slower for better visual effect
        
        print(f"   🌟 Encore! Encore! 👏")
        self.is_performing = False
        return f"🎵 {self.name} finished singing '{song_name}'! What a magical Disney performance! ✨"
    
    def wave(self, style: str = "friendly") -> str:
        """Mickey waves hello!"""
        if self.is_performing:
            return f"👋 {self.name} is busy performing! Please wait."
        
        wave_styles = {
            "friendly": ["👋", "👋", "👋", "👋", "👋"],
            "excited": ["👋✨", "👋✨", "👋✨", "👋✨", "👋✨"],
            "royal": ["👋👑", "👋👑", "👋👑", "👋👑", "👋👑"],
            "magical": ["👋✨🌟", "👋✨🌟", "👋✨🌟", "👋✨🌟", "👋✨🌟"],
            "goofy": ["👋🤪", "👋🤪", "👋🤪", "👋🤪", "👋🤪"]
        }
        
        wave_sequence = wave_styles.get(style, wave_styles["friendly"])
        
        print(f"👋 {self.name} waves {style}ly!")
        print(f"   🎭 Disney charm at its finest! ✨")
        
        # Animated wave sequence
        for wave_emoji in wave_sequence:
            print(f"   {wave_emoji}")
            time.sleep(0.3)
        
        return f"👋 Hi there! {self.name} says hello with a {style} wave! 🌟"
    
    def dance(self, dance_move: Optional[str] = None) -> str:
        """Mickey dances with style!"""
        if self.is_performing:
            return f"💃 {self.name} is already performing! Please wait."
        
        if dance_move is None:
            dance_move = random.choice(self.dance_moves)
        
        self.is_performing = True
        self.energy -= 15
        
        print(f"💃 {self.name} starts dancing the '{dance_move}'...")
        print(f"   🎭 Disney rhythm in the air! ✨")
        
        # Simulate dance performance with visual feedback
        dance_steps = self._get_dance_steps(dance_move)
        for i, step in enumerate(dance_steps):
            # Add visual feedback with emojis
            visual_feedback = "💃" if i % 2 == 0 else "🕺"
            print(f"   {visual_feedback} {step}")
            time.sleep(0.6)  # Slower for better visual effect
        
        print(f"   🌟 Bravo! What a performance! 👏")
        self.is_performing = False
        return f"💃 {self.name} finished the '{dance_move}'! What a magical Disney show! ✨"
    
    def perform_show(self) -> str:
        """Mickey puts on a complete show with singing, waving, and dancing!"""
        if self.is_performing:
            return f"🎭 {self.name} is already performing! Please wait."
        
        self.is_performing = True
        print(f"🎭 {self.name} is putting on a spectacular Disney show!")
        print(f"   ✨ The magic begins... 🌟")
        
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
        
        print(f"   🌟 Standing ovation! 👏✨")
        self.is_performing = False
        return f"🎭 {self.name} completed the show! Thank you for watching this magical Disney performance! ✨🌟"
    
    def _get_song_lyrics(self, song_name: str) -> List[str]:
        """Get lyrics for a specific song."""
        lyrics_dict = {
            "It's a Small World": [
                "It's a world of laughter, a world of tears",
                "It's a world of hopes and a world of fears",
                "There's so much that we share",
                "That it's time we're aware",
                "It's a small world after all!"
            ],
            "When You Wish Upon a Star": [
                "When you wish upon a star",
                "Makes no difference who you are",
                "Anything your heart desires",
                "Will come to you!"
            ],
            "Mickey Mouse Club March": [
                "M-I-C-K-E-Y M-O-U-S-E",
                "Mickey Mouse! Mickey Mouse!",
                "Forever let us hold our banner high!",
                "High! High! High!"
            ]
        }
        
        return lyrics_dict.get(song_name, [
            "🎵 La la la...",
            "🎵 Singing a beautiful melody...",
            "🎵 Making everyone smile...",
            "🎵 That's the magic of music!"
        ])
    
    def _get_dance_steps(self, dance_move: str) -> List[str]:
        """Get dance steps for a specific move."""
        steps_dict = {
            "The Mickey Shuffle": [
                "🦶 Step to the left",
                "🦶 Step to the right",
                "🦶 Shuffle your feet",
                "🦶 Spin around twice!"
            ],
            "The Hot Dog Dance": [
                "🌭 Arms up high",
                "🌭 Wiggle those hips",
                "🌭 Jump and spin",
                "🌭 Hot dog dance complete!"
            ],
            "The Sorcerer's Apprentice Spin": [
                "🧙‍♂️ Raise the magic wand",
                "🧙‍♂️ Start the slow spin",
                "🧙‍♂️ Faster and faster",
                "🧙‍♂️ Magical dance complete!"
            ]
        }
        
        return steps_dict.get(dance_move, [
            "💃 Dancing with style...",
            "💃 Moving to the rhythm...",
            "💃 Spinning and twirling...",
            "💃 What a fantastic dance!"
        ])
    
    def get_status(self) -> Dict[str, str]:
        """Get Mickey's current status."""
        return {
            "name": self.name,
            "mood": self.mood,
            "energy": f"{self.energy}%",
            "is_performing": str(self.is_performing),
            "available_songs": str(len(self.songs)),
            "available_dances": str(len(self.dance_moves))
        }
    
    def rest(self) -> str:
        """Mickey takes a rest to regain energy."""
        if self.is_performing:
            return f"😴 {self.name} is performing and can't rest right now!"
        
        old_energy = self.energy
        self.energy = min(100, self.energy + 30)
        
        print(f"😴 {self.name} takes a nice Disney rest...")
        print(f"   ✨ Sweet dreams and magic... 🌟")
        
        # Visual rest sequence
        rest_emojis = ["😴", "😴", "😴", "😴", "😴"]
        for emoji in rest_emojis:
            print(f"   {emoji}")
            time.sleep(0.5)
        
        return f"😴 {self.name} feels refreshed and ready for more Disney magic! Energy: {old_energy}% → {self.energy}% ✨"