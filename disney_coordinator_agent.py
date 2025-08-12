import time
import random
import threading
from typing import List, Dict, Optional, Tuple
from mickey_mouse_agent import MickeyMouseAgent
from donald_duck_agent import DonaldDuckAgent

class DisneyCoordinatorAgent:
    """
    Disney Coordinator Agent - Manages Mickey Mouse and Donald Duck agents
    for individual and collaborative performances!
    """
    
    def __init__(self):
        self.name = "Disney Coordinator"
        self.mickey = MickeyMouseAgent()
        self.donald = DonaldDuckAgent()
        self.is_coordinating = False
        
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
        
        # Performance types
        self.performance_types = {
            "individual": ["solo_sing", "solo_dance", "solo_wave", "solo_show"],
            "duet": ["duet_sing", "duet_dance", "duet_show"],
            "ensemble": ["ensemble_show", "energy_check", "status_report"]
        }
    
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
        """Mickey and Donald perform a duet song together!"""
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
        
        # Get duet lyrics
        lyrics = self._get_duet_lyrics(song_name)
        
        # Perform the duet with alternating parts
        for i, line in enumerate(lyrics):
            if i % 2 == 0:
                # Mickey's part
                print(f"   🐭 {self.mickey.name}: {line}")
            else:
                # Donald's part
                print(f"   🦆 {self.donald.name}: {line}")
            time.sleep(1.0)
        
        # Final chorus together
        print(f"   🎵 Both: Together in perfect Disney harmony!")
        print(f"   🌟 Encore! Encore! 👏")
        
        self.mickey.is_performing = False
        self.donald.is_performing = False
        self.is_coordinating = False
        
        return f"🎵 {self.mickey.name} and {self.donald.name} finished their duet '{song_name}'! What a magical performance! ✨"
    
    def perform_duet_dance(self, dance_name: Optional[str] = None) -> str:
        """Mickey and Donald perform a duet dance together!"""
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
        
        # Get duet dance steps
        steps = self._get_duet_dance_steps(dance_name)
        
        # Perform the duet dance with synchronized moves
        for i, step in enumerate(steps):
            print(f"   💃 Both: {step}")
            time.sleep(0.8)
        
        # Final pose together
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
            "available_duet_dances": str(len(self.duet_dances))
        }