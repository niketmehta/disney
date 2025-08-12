#!/usr/bin/env python3
"""
Disney Coordinator Agent with Working Audio
Uses system beep and provides a proper CLI interface
"""

import time
import random
import os
import sys
import math
from typing import List, Dict, Optional, Tuple
from mickey_mouse_agent import MickeyMouseAgent
from donald_duck_agent import DonaldDuckAgent

class DisneyCoordinatorWorkingAudio:
    """
    Disney Coordinator Agent with Working Audio Capabilities
    """
    
    def __init__(self):
        self.name = "Disney Coordinator (Working Audio)"
        self.mickey = MickeyMouseAgent()
        self.donald = DonaldDuckAgent()
        self.is_coordinating = False
        
        # Musical notes and frequencies (in Hz) - mapped to beep durations
        self.musical_notes = {
            "C": 0.2, "C#": 0.2, "D": 0.2, "D#": 0.2,
            "E": 0.2, "F": 0.2, "F#": 0.2, "G": 0.2,
            "G#": 0.2, "A": 0.2, "A#": 0.2, "B": 0.2
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
        
        print("🎵 Working audio system initialized!")
        print("🔊 Using system beep for musical tones!")
    
    def _generate_beep(self, duration: float = 0.2):
        """Generate a system beep."""
        try:
            # Use system beep
            print('\a', end='', flush=True)
            time.sleep(duration)
        except Exception as e:
            print(f"🎵 Beep failed: {e}")
            time.sleep(duration)
    
    def _play_melody(self, melody: List[str], duration: float = 0.2):
        """Play a sequence of musical notes using beeps."""
        for note in melody:
            if note in self.musical_notes:
                self._generate_beep(self.musical_notes[note])
                print(f"🎵 Playing note {note}")
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
        """Ask Mickey to perform a specific action with working audio."""
        if self.mickey.is_performing:
            return f"🎭 {self.mickey.name} is already performing! Please wait."
        
        print(f"🎵 Mickey is performing {action} with working audio!")
        
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
        """Ask Donald to perform a specific action with working audio."""
        if self.donald.is_performing:
            return f"🎭 {self.donald.name} is already performing! Please wait."
        
        print(f"🎵 Donald is performing {action} with working audio!")
        
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
        """Mickey and Donald perform a duet song together with working audio!"""
        if self.mickey.is_performing or self.donald.is_performing:
            return f"🎭 One or both agents are already performing! Please wait."
        
        if song_name is None:
            song_name = random.choice(self.duet_songs)
        
        print(f"🎵 Mickey and Donald are performing duet '{song_name}' with working audio!")
        
        self.is_coordinating = True
        self.mickey.is_performing = True
        self.donald.is_performing = True
        
        # Musical introduction with working audio
        intro_melody = self.disney_melodies["friendship"]
        self._play_melody(intro_melody, 0.4)
        
        # Get duet lyrics
        lyrics = self._get_duet_lyrics(song_name)
        
        # Perform the duet with enhanced musical accompaniment
        for i in range(0, len(lyrics), 2):
            if i + 1 < len(lyrics):
                # Duet harmony with working audio
                mickey_notes = random.sample(list(self.musical_notes.keys()), 2)
                donald_notes = random.sample(list(self.musical_notes.keys()), 2)
                
                print(f"🎤 Mickey sings: {lyrics[i]}")
                # Mickey's part
                for note in mickey_notes:
                    self._generate_beep(self.musical_notes[note])
                
                time.sleep(0.5)
                
                print(f"🦆 Donald sings: {lyrics[i+1]}")
                # Donald's part
                for note in donald_notes:
                    self._generate_beep(self.musical_notes[note])
                
                time.sleep(0.5)
                
                # Combined harmony
                combined_notes = random.sample(list(self.musical_notes.keys()), 4)
                print("🎵 Both sing in harmony!")
                for note in combined_notes:
                    self._generate_beep(self.musical_notes[note])
                
                time.sleep(0.8)
        
        # Grand finale with full orchestra
        finale_melody = self.disney_melodies["magic"] + self.disney_melodies["harmony"]
        self._play_melody(finale_melody, 0.2)
        
        self.mickey.is_performing = False
        self.donald.is_performing = False
        self.is_coordinating = False
        
        return f"🎵 {self.mickey.name} and {self.donald.name} finished their duet '{song_name}'! What a magical performance! ✨"
    
    def perform_duet_dance(self, dance_name: Optional[str] = None) -> str:
        """Mickey and Donald perform a duet dance together with working audio!"""
        if self.mickey.is_performing or self.donald.is_performing:
            return f"🎭 One or both agents are already performing! Please wait."
        
        if dance_name is None:
            dance_name = random.choice(self.duet_dances)
        
        print(f"💃 Mickey and Donald are performing duet dance '{dance_name}' with working audio!")
        
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
            print(f"💃 Step {i+1}: {step}")
            # Dance rhythm
            rhythm_notes = random.sample(list(self.musical_notes.keys()), 2)
            for note in rhythm_notes:
                self._generate_beep(self.musical_notes[note])
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
        
        print("🎭 Mickey and Donald are putting on an ensemble show with working audio!")
        
        self.is_coordinating = True
        
        # Opening fanfare with working audio
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
            "audio_system": "system_beep"
        }

def main():
    """Main interactive CLI for the Disney Coordinator with Working Audio."""
    coordinator = DisneyCoordinatorWorkingAudio()
    
    print("🎭🎵🦆🐭")
    print("=" * 60)
    print("    DISNEY COORDINATOR - WORKING AUDIO CLI")
    print("=" * 60)
    print("🎭🎵🦆🐭")
    print()
    print(f"🎉 Welcome! {coordinator.name} is ready!")
    print("🔊 This version uses system beep for actual audio!")
    print()
    
    while True:
        print("\n🎭 Available Actions:")
        print("1.  Mickey - Sing")
        print("2.  Mickey - Dance")
        print("3.  Mickey - Wave")
        print("4.  Mickey - Show")
        print("5.  Mickey - Rest")
        print("6.  Donald - Sing")
        print("7.  Donald - Dance")
        print("8.  Donald - Wave")
        print("9.  Donald - Show")
        print("10. Donald - Rest")
        print("11. Duet Song (with audio!)")
        print("12. Duet Dance (with audio!)")
        print("13. Ensemble Show (with audio!)")
        print("14. Check Energy Levels")
        print("15. Rest Both Agents")
        print("16. Show Status")
        print("17. Exit")
        print()
        
        try:
            choice = input("🎭 Enter your choice (1-17): ").strip()
            
            if choice == "1":
                result = coordinator.ask_mickey_to_perform("sing", song_name="It's a Small World")
                print(f"Result: {result}")
            
            elif choice == "2":
                result = coordinator.ask_mickey_to_perform("dance", dance_move="The Mickey Shuffle")
                print(f"Result: {result}")
            
            elif choice == "3":
                result = coordinator.ask_mickey_to_perform("wave", style="friendly")
                print(f"Result: {result}")
            
            elif choice == "4":
                result = coordinator.ask_mickey_to_perform("show")
                print(f"Result: {result}")
            
            elif choice == "5":
                result = coordinator.ask_mickey_to_perform("rest")
                print(f"Result: {result}")
            
            elif choice == "6":
                result = coordinator.ask_donald_to_perform("sing", song_name="Donald's Quack Song")
                print(f"Result: {result}")
            
            elif choice == "7":
                result = coordinator.ask_donald_to_perform("dance", dance_move="The Quack Attack")
                print(f"Result: {result}")
            
            elif choice == "8":
                result = coordinator.ask_donald_to_perform("wave", style="excited")
                print(f"Result: {result}")
            
            elif choice == "9":
                result = coordinator.ask_donald_to_perform("show")
                print(f"Result: {result}")
            
            elif choice == "10":
                result = coordinator.ask_donald_to_perform("rest")
                print(f"Result: {result}")
            
            elif choice == "11":
                print("🎵 Performing duet song with working audio!")
                result = coordinator.perform_duet_song()
                print(f"Result: {result}")
            
            elif choice == "12":
                print("💃 Performing duet dance with working audio!")
                result = coordinator.perform_duet_dance()
                print(f"Result: {result}")
            
            elif choice == "13":
                print("🎭 Performing ensemble show with working audio!")
                result = coordinator.perform_ensemble_show()
                print(f"Result: {result}")
            
            elif choice == "14":
                result = coordinator.check_energy_levels()
                print(f"Result: {result}")
            
            elif choice == "15":
                result = coordinator.rest_both_agents()
                print(f"Result: {result}")
            
            elif choice == "16":
                status = coordinator.get_coordinator_status()
                print("📊 Coordinator Status:")
                for key, value in status.items():
                    print(f"   {key}: {value}")
            
            elif choice == "17":
                print("🎭 Thank you for using the Disney Coordinator with Working Audio!")
                print("🎵 Hope you enjoyed the musical performances!")
                break
            
            else:
                print("❌ Invalid choice. Please enter a number between 1-17.")
        
        except KeyboardInterrupt:
            print("\n🎭 Goodbye! Thanks for using the Disney Coordinator!")
            break
        except EOFError:
            print("\n🎭 Goodbye! Thanks for using the Disney Coordinator!")
            break

if __name__ == "__main__":
    main()