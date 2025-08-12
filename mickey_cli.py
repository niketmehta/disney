#!/usr/bin/env python3
"""
Mickey Mouse Agent - Command Line Interface
A simple CLI to interact with Mickey Mouse directly!
"""

from mickey_mouse_agent import MickeyMouseAgent
import time

def print_banner():
    """Print a cute Mickey Mouse banner."""
    print("""
    🐭🎭🎤💃👋
    ========================================
        MICKEY MOUSE AGENT
    ========================================
    🎭🎤💃👋🐭
    """)

def print_menu():
    """Print the main menu options."""
    print("\n🎭 What would you like Mickey to do?")
    print("1. 🎤 Sing a song")
    print("2. 👋 Wave hello")
    print("3. 💃 Dance")
    print("4. 🎭 Put on a full show")
    print("5. 😴 Take a rest")
    print("6. 📊 Check Mickey's status")
    print("7. 🎵 List available songs")
    print("8. 💃 List available dances")
    print("9. 🚪 Exit")
    print("-" * 40)

def main():
    """Main CLI loop."""
    mickey = MickeyMouseAgent()
    
    print_banner()
    print(f"🎉 Welcome! {mickey.name} is ready to entertain you!")
    
    while True:
        print_menu()
        
        try:
            choice = input("🎯 Enter your choice (1-9): ").strip()
            
            if choice == "1":
                print("\n🎵 Available songs:")
                for i, song in enumerate(mickey.songs, 1):
                    print(f"   {i}. {song}")
                print("   0. Random song")
                
                song_choice = input("\n🎤 Choose a song (0-6): ").strip()
                if song_choice == "0":
                    result = mickey.sing()
                elif song_choice.isdigit() and 1 <= int(song_choice) <= len(mickey.songs):
                    song_name = mickey.songs[int(song_choice) - 1]
                    result = mickey.sing(song_name)
                else:
                    print("❌ Invalid choice! Mickey will sing a random song.")
                    result = mickey.sing()
                
                print(f"\n{result}")
                
            elif choice == "2":
                print("\n👋 Wave styles:")
                styles = ["friendly", "excited", "royal", "magical", "goofy"]
                for i, style in enumerate(styles, 1):
                    print(f"   {i}. {style.title()}")
                print("   0. Default (friendly)")
                
                style_choice = input("\n👋 Choose a wave style (0-5): ").strip()
                if style_choice == "0":
                    result = mickey.wave()
                elif style_choice.isdigit() and 1 <= int(style_choice) <= len(styles):
                    style = styles[int(style_choice) - 1]
                    result = mickey.wave(style)
                else:
                    print("❌ Invalid choice! Mickey will wave friendly.")
                    result = mickey.wave()
                
                print(f"\n{result}")
                
            elif choice == "3":
                print("\n💃 Available dances:")
                for i, dance in enumerate(mickey.dance_moves, 1):
                    print(f"   {i}. {dance}")
                print("   0. Random dance")
                
                dance_choice = input("\n💃 Choose a dance (0-6): ").strip()
                if dance_choice == "0":
                    result = mickey.dance()
                elif dance_choice.isdigit() and 1 <= int(dance_choice) <= len(mickey.dance_moves):
                    dance_name = mickey.dance_moves[int(dance_choice) - 1]
                    result = mickey.dance(dance_name)
                else:
                    print("❌ Invalid choice! Mickey will dance randomly.")
                    result = mickey.dance()
                
                print(f"\n{result}")
                
            elif choice == "4":
                print("\n🎭 Mickey is putting on a spectacular show!")
                result = mickey.perform_show()
                print(f"\n{result}")
                
            elif choice == "5":
                result = mickey.rest()
                print(f"\n{result}")
                
            elif choice == "6":
                status = mickey.get_status()
                print("\n📊 Mickey's Current Status:")
                print("-" * 30)
                for key, value in status.items():
                    print(f"   {key.replace('_', ' ').title()}: {value}")
                
            elif choice == "7":
                print("\n🎵 Available Songs:")
                print("-" * 20)
                for i, song in enumerate(mickey.songs, 1):
                    print(f"   {i}. {song}")
                
            elif choice == "8":
                print("\n💃 Available Dances:")
                print("-" * 20)
                for i, dance in enumerate(mickey.dance_moves, 1):
                    print(f"   {i}. {dance}")
                
            elif choice == "9":
                print("\n👋 Thanks for visiting Mickey Mouse!")
                print("🎭 Have a magical day!")
                break
                
            else:
                print("❌ Invalid choice! Please enter a number between 1-9.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Thanks for visiting Mickey Mouse!")
            print("🎭 Have a magical day!")
            break
        except Exception as e:
            print(f"❌ Oops! Something went wrong: {e}")
        
        input("\n⏸️  Press Enter to continue...")

if __name__ == "__main__":
    main()