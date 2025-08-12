#!/usr/bin/env python3
"""
Disney Coordinator Agent - Command Line Interface
Interactive CLI for managing Mickey and Donald agents
"""

import time
import sys
from disney_coordinator_agent import DisneyCoordinatorAgent

class CoordinatorCLI:
    def __init__(self):
        self.coordinator = DisneyCoordinatorAgent()
        self.running = True
    
    def print_header(self):
        print("\n🎭🎵🦆🐭")
        print("=" * 60)
        print("    DISNEY COORDINATOR AGENT - CLI")
        print("=" * 60)
        print("🎭🎵🦆🐭")
        print()
    
    def print_menu(self):
        print("🎪 Available Actions:")
        print("-" * 30)
        print("1. 🐭 Mickey Mouse Actions")
        print("2. 🦆 Donald Duck Actions")
        print("3. 🎵 Duet Performances")
        print("4. 🎭 Ensemble Shows")
        print("5. ⚙️ Management")
        print("6. 📊 Status Report")
        print("0. 🚪 Exit")
        print()
    
    def mickey_menu(self):
        print("\n🐭 Mickey Mouse Actions:")
        print("-" * 25)
        print("1. 🎤 Sing")
        print("2. 💃 Dance")
        print("3. 👋 Wave")
        print("4. 🎭 Full Show")
        print("5. 😴 Rest")
        print("0. 🔙 Back")
        
        choice = input("\nChoose action (0-5): ").strip()
        
        if choice == "1":
            song = input("Song name (or press Enter for random): ").strip()
            song = song if song else None
            print(f"\n🎤 Asking Mickey to sing...")
            result = self.coordinator.ask_mickey_to_perform("sing", song_name=song)
            print(f"Result: {result}")
            
        elif choice == "2":
            dance = input("Dance move (or press Enter for random): ").strip()
            dance = dance if dance else None
            print(f"\n💃 Asking Mickey to dance...")
            result = self.coordinator.ask_mickey_to_perform("dance", dance_move=dance)
            print(f"Result: {result}")
            
        elif choice == "3":
            styles = ["friendly", "excited", "royal", "magical", "goofy"]
            print("Wave styles:", ", ".join(styles))
            style = input("Style (or press Enter for friendly): ").strip()
            style = style if style else "friendly"
            print(f"\n👋 Asking Mickey to wave...")
            result = self.coordinator.ask_mickey_to_perform("wave", style=style)
            print(f"Result: {result}")
            
        elif choice == "4":
            print(f"\n🎭 Asking Mickey to perform a full show...")
            result = self.coordinator.ask_mickey_to_perform("show")
            print(f"Result: {result}")
            
        elif choice == "5":
            print(f"\n😴 Asking Mickey to rest...")
            result = self.coordinator.ask_mickey_to_perform("rest")
            print(f"Result: {result}")
            
        elif choice == "0":
            return
        
        input("\nPress Enter to continue...")
    
    def donald_menu(self):
        print("\n🦆 Donald Duck Actions:")
        print("-" * 25)
        print("1. 🎤 Sing")
        print("2. 💃 Dance")
        print("3. 👋 Wave")
        print("4. 🎭 Full Show")
        print("5. 😴 Rest")
        print("0. 🔙 Back")
        
        choice = input("\nChoose action (0-5): ").strip()
        
        if choice == "1":
            song = input("Song name (or press Enter for random): ").strip()
            song = song if song else None
            print(f"\n🎤 Asking Donald to sing...")
            result = self.coordinator.ask_donald_to_perform("sing", song_name=song)
            print(f"Result: {result}")
            
        elif choice == "2":
            dance = input("Dance move (or press Enter for random): ").strip()
            dance = dance if dance else None
            print(f"\n💃 Asking Donald to dance...")
            result = self.coordinator.ask_donald_to_perform("dance", dance_move=dance)
            print(f"Result: {result}")
            
        elif choice == "3":
            styles = ["friendly", "excited", "royal", "magical", "goofy"]
            print("Wave styles:", ", ".join(styles))
            style = input("Style (or press Enter for friendly): ").strip()
            style = style if style else "friendly"
            print(f"\n👋 Asking Donald to wave...")
            result = self.coordinator.ask_donald_to_perform("wave", style=style)
            print(f"Result: {result}")
            
        elif choice == "4":
            print(f"\n🎭 Asking Donald to perform a full show...")
            result = self.coordinator.ask_donald_to_perform("show")
            print(f"Result: {result}")
            
        elif choice == "5":
            print(f"\n😴 Asking Donald to rest...")
            result = self.coordinator.ask_donald_to_perform("rest")
            print(f"Result: {result}")
            
        elif choice == "0":
            return
        
        input("\nPress Enter to continue...")
    
    def duet_menu(self):
        print("\n🎵 Duet Performances:")
        print("-" * 25)
        print("1. 🎵 Duet Song")
        print("2. 💃 Duet Dance")
        print("0. 🔙 Back")
        
        choice = input("\nChoose action (0-2): ").strip()
        
        if choice == "1":
            songs = self.coordinator.duet_songs
            print("Available duet songs:")
            for i, song in enumerate(songs, 1):
                print(f"   {i}. {song}")
            song_choice = input("Choose song number (or press Enter for random): ").strip()
            
            if song_choice.isdigit() and 1 <= int(song_choice) <= len(songs):
                song_name = songs[int(song_choice) - 1]
            else:
                song_name = None
            
            print(f"\n🎵 Performing duet song...")
            result = self.coordinator.perform_duet_song(song_name)
            print(f"Result: {result}")
            
        elif choice == "2":
            dances = self.coordinator.duet_dances
            print("Available duet dances:")
            for i, dance in enumerate(dances, 1):
                print(f"   {i}. {dance}")
            dance_choice = input("Choose dance number (or press Enter for random): ").strip()
            
            if dance_choice.isdigit() and 1 <= int(dance_choice) <= len(dances):
                dance_name = dances[int(dance_choice) - 1]
            else:
                dance_name = None
            
            print(f"\n💃 Performing duet dance...")
            result = self.coordinator.perform_duet_dance(dance_name)
            print(f"Result: {result}")
            
        elif choice == "0":
            return
        
        input("\nPress Enter to continue...")
    
    def ensemble_menu(self):
        print("\n🎭 Ensemble Shows:")
        print("-" * 20)
        print("1. 🎭 Full Ensemble Show")
        print("0. 🔙 Back")
        
        choice = input("\nChoose action (0-1): ").strip()
        
        if choice == "1":
            print(f"\n🎭 Performing full ensemble show...")
            print("This will be a spectacular performance with both agents!")
            confirm = input("Continue? (y/n): ").strip().lower()
            
            if confirm in ['y', 'yes']:
                result = self.coordinator.perform_ensemble_show()
                print(f"Result: {result}")
            else:
                print("Ensemble show cancelled.")
                
        elif choice == "0":
            return
        
        input("\nPress Enter to continue...")
    
    def management_menu(self):
        print("\n⚙️ Management:")
        print("-" * 15)
        print("1. 🔋 Check Energy Levels")
        print("2. 😴 Rest Both Agents")
        print("3. 📋 Available Performances")
        print("0. 🔙 Back")
        
        choice = input("\nChoose action (0-3): ").strip()
        
        if choice == "1":
            print(f"\n🔋 Checking energy levels...")
            result = self.coordinator.check_energy_levels()
            print(f"Result: {result}")
            
        elif choice == "2":
            print(f"\n😴 Resting both agents...")
            result = self.coordinator.rest_both_agents()
            print(f"Result: {result}")
            
        elif choice == "3":
            print(f"\n📋 Available performances:")
            performances = self.coordinator.get_available_performances()
            for category, items in performances.items():
                print(f"   {category.title()}:")
                if isinstance(items, dict):
                    for agent, actions in items.items():
                        print(f"     {agent.title()}: {', '.join(actions)}")
                else:
                    print(f"     {', '.join(items)}")
                    
        elif choice == "0":
            return
        
        input("\nPress Enter to continue...")
    
    def status_report(self):
        print("\n📊 Status Report:")
        print("-" * 20)
        
        # Coordinator status
        coord_status = self.coordinator.get_coordinator_status()
        print(f"🎭 Coordinator: {coord_status['coordinator_name']}")
        print(f"   Coordinating: {coord_status['is_coordinating']}")
        print(f"   Mickey Available: {coord_status['mickey_available']}")
        print(f"   Donald Available: {coord_status['donald_available']}")
        print(f"   Duet Songs: {coord_status['available_duet_songs']}")
        print(f"   Duet Dances: {coord_status['available_duet_dances']}")
        
        print()
        
        # Agent status
        agent_status = self.coordinator.get_agent_status()
        for agent, info in agent_status.items():
            print(f"🐭🦆 {agent.title()}:")
            for key, value in info.items():
                print(f"   {key.replace('_', ' ').title()}: {value}")
            print()
        
        input("Press Enter to continue...")
    
    def run(self):
        self.print_header()
        
        while self.running:
            self.print_menu()
            
            choice = input("Choose action (0-6): ").strip()
            
            if choice == "1":
                self.mickey_menu()
            elif choice == "2":
                self.donald_menu()
            elif choice == "3":
                self.duet_menu()
            elif choice == "4":
                self.ensemble_menu()
            elif choice == "5":
                self.management_menu()
            elif choice == "6":
                self.status_report()
            elif choice == "0":
                print("\n🎭 Thank you for using the Disney Coordinator Agent!")
                print("🐭🦆 See you next time for more Disney magic! ✨")
                self.running = False
            else:
                print("❌ Invalid choice. Please try again.")

def main():
    cli = CoordinatorCLI()
    try:
        cli.run()
    except KeyboardInterrupt:
        print("\n\n🎭 Coordinator interrupted. Goodbye! ✨")
        sys.exit(0)

if __name__ == "__main__":
    main()