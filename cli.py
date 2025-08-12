#!/usr/bin/env python3
"""
Disney Coordinator CLI - Consolidated Command Line Interface
Provides interactive access to Mickey and Donald with visual audio
"""

import sys
import os
from disney_coordinator import DisneyCoordinatorVisualAudio

def main():
    """Main CLI interface for Disney Coordinator."""
    coordinator = DisneyCoordinatorVisualAudio()
    
    print("🎭🎵🦆🐭")
    print("=" * 60)
    print("    DISNEY COORDINATOR CLI - VISUAL AUDIO")
    print("=" * 60)
    print("🎭🎵🦆🐭")
    print()
    print(f"🎉 Welcome! {coordinator.name} is ready!")
    print("✨ This version uses rich visual audio simulation!")
    print("🎵 Musical symbols and animations create the audio experience!")
    print()
    print("🎭 Quick Start:")
    print("   • Type 'duet' for Mickey and Donald to perform together")
    print("   • Type 'mickey sing' for Mickey to sing")
    print("   • Type 'donald dance' for Donald to dance")
    print("   • Type 'help' for all commands")
    print("   • Type 'quit' to exit")
    print()
    
    while True:
        try:
            command = input("🎭 Enter command: ").strip().lower()
            
            if command in ['quit', 'exit', 'q']:
                print("🎭 Thank you for using the Disney Coordinator!")
                print("🎵 Hope you enjoyed the musical performances!")
                break
            
            elif command == 'help':
                print("\n🎭 Available Commands:")
                print("Individual Actions:")
                print("  mickey sing     - Mickey sings with visual audio")
                print("  mickey dance    - Mickey dances with visual audio")
                print("  mickey wave     - Mickey waves with visual audio")
                print("  mickey show     - Mickey performs a show")
                print("  mickey rest     - Mickey takes a rest")
                print("  donald sing     - Donald sings with visual audio")
                print("  donald dance    - Donald dances with visual audio")
                print("  donald wave     - Donald waves with visual audio")
                print("  donald show     - Donald performs a show")
                print("  donald rest     - Donald takes a rest")
                print()
                print("Duet Performances:")
                print("  duet            - Mickey and Donald sing together")
                print("  duet song       - Mickey and Donald sing together")
                print("  duet dance      - Mickey and Donald dance together")
                print("  ensemble        - Complete ensemble show")
                print()
                print("Management:")
                print("  status          - Check agent status")
                print("  energy          - Check energy levels")
                print("  rest both       - Both agents rest")
                print("  help            - Show this help")
                print("  quit            - Exit the program")
                print()
            
            elif command == 'status':
                status = coordinator.get_coordinator_status()
                print("\n📊 Coordinator Status:")
                for key, value in status.items():
                    print(f"   {key}: {value}")
                
                agents = coordinator.get_agent_status()
                print("\n🐭 Mickey Status:")
                for key, value in agents['mickey'].items():
                    print(f"   {key}: {value}")
                print("\n🦆 Donald Status:")
                for key, value in agents['donald'].items():
                    print(f"   {key}: {value}")
                print()
            
            elif command == 'energy':
                result = coordinator.check_energy_levels()
                print(f"\n{result}\n")
            
            elif command == 'rest both':
                result = coordinator.rest_both_agents()
                print(f"\n{result}\n")
            
            elif command in ['duet', 'duet song']:
                print("\n🎵 Performing duet song with visual audio!")
                result = coordinator.perform_duet_song()
                print(f"\n{result}\n")
            
            elif command == 'duet dance':
                print("\n💃 Performing duet dance with visual audio!")
                result = coordinator.perform_duet_dance()
                print(f"\n{result}\n")
            
            elif command == 'ensemble':
                print("\n🎭 Performing ensemble show with visual audio!")
                result = coordinator.perform_ensemble_show()
                print(f"\n{result}\n")
            
            elif command.startswith('mickey '):
                action = command.split(' ', 1)[1]
                if action in ['sing', 'dance', 'wave', 'show', 'rest']:
                    print(f"\n🎵 Mickey is performing {action} with visual audio!")
                    if action == 'sing':
                        result = coordinator.ask_mickey_to_perform("sing", song_name="It's a Small World")
                    elif action == 'dance':
                        result = coordinator.ask_mickey_to_perform("dance", dance_move="The Mickey Shuffle")
                    elif action == 'wave':
                        result = coordinator.ask_mickey_to_perform("wave", style="friendly")
                    elif action == 'show':
                        result = coordinator.ask_mickey_to_perform("show")
                    elif action == 'rest':
                        result = coordinator.ask_mickey_to_perform("rest")
                    print(f"\n{result}\n")
                else:
                    print(f"❌ Unknown Mickey action: {action}")
                    print("Available actions: sing, dance, wave, show, rest\n")
            
            elif command.startswith('donald '):
                action = command.split(' ', 1)[1]
                if action in ['sing', 'dance', 'wave', 'show', 'rest']:
                    print(f"\n🎵 Donald is performing {action} with visual audio!")
                    if action == 'sing':
                        result = coordinator.ask_donald_to_perform("sing", song_name="Donald's Quack Song")
                    elif action == 'dance':
                        result = coordinator.ask_donald_to_perform("dance", dance_move="The Quack Attack")
                    elif action == 'wave':
                        result = coordinator.ask_donald_to_perform("wave", style="excited")
                    elif action == 'show':
                        result = coordinator.ask_donald_to_perform("show")
                    elif action == 'rest':
                        result = coordinator.ask_donald_to_perform("rest")
                    print(f"\n{result}\n")
                else:
                    print(f"❌ Unknown Donald action: {action}")
                    print("Available actions: sing, dance, wave, show, rest\n")
            
            else:
                print(f"❌ Unknown command: {command}")
                print("Type 'help' for available commands\n")
        
        except KeyboardInterrupt:
            print("\n🎭 Goodbye! Thanks for using the Disney Coordinator!")
            break
        except EOFError:
            print("\n🎭 Goodbye! Thanks for using the Disney Coordinator!")
            break

if __name__ == "__main__":
    main()