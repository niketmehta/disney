#!/usr/bin/env python3
"""
Quick Demo of Mickey Mouse Agent
"""

import time

# Simple demo without external dependencies
class MickeyDemo:
    def __init__(self):
        self.name = "Mickey Mouse"
        self.energy = 100
        
    def sing(self, song_name="It's a Small World"):
        print(f"🎤 {self.name} starts singing '{song_name}'...")
        time.sleep(0.5)
        print("   It's a world of laughter, a world of tears")
        time.sleep(0.5)
        print("   It's a world of hopes and a world of fears")
        time.sleep(0.5)
        print("   There's so much that we share")
        time.sleep(0.5)
        print("   That it's time we're aware")
        time.sleep(0.5)
        print("   It's a small world after all!")
        time.sleep(0.5)
        print(f"🎵 {self.name} finished singing! What a performance!")
        self.energy -= 10
        
    def wave(self, style="friendly"):
        wave_style = {
            "friendly": "👋",
            "excited": "👋✨",
            "royal": "👋👑",
            "magical": "👋✨🌟",
            "goofy": "👋🤪"
        }
        emoji = wave_style.get(style, "👋")
        print(f"{emoji} {self.name} waves {style}ly!")
        time.sleep(0.3)
        print(f"{emoji} Hi there! {self.name} says hello with a {style} wave!")
        
    def dance(self, dance_name="The Mickey Shuffle"):
        print(f"💃 {self.name} starts dancing the '{dance_name}'...")
        time.sleep(0.4)
        print("   🦶 Step to the left")
        time.sleep(0.4)
        print("   🦶 Step to the right")
        time.sleep(0.4)
        print("   🦶 Shuffle your feet")
        time.sleep(0.4)
        print("   🦶 Spin around twice!")
        time.sleep(0.4)
        print(f"💃 {self.name} finished the '{dance_name}'! What a show!")
        self.energy -= 15
        
    def perform_show(self):
        print(f"🎭 {self.name} is putting on a spectacular show!")
        time.sleep(0.5)
        
        # Wave to audience
        self.wave("excited")
        time.sleep(0.5)
        
        # Sing a song
        self.sing()
        time.sleep(0.5)
        
        # Dance
        self.dance()
        time.sleep(0.5)
        
        # Final wave
        self.wave("royal")
        print(f"🎭 {self.name} completed the show! Thank you for watching!")
        
    def get_status(self):
        return {
            "name": self.name,
            "energy": f"{self.energy}%",
            "mood": "happy"
        }

def main():
    print("🐭🎭🎤💃👋")
    print("=" * 50)
    print("    MICKEY MOUSE AGENT DEMO")
    print("=" * 50)
    print("🎭🎤💃👋🐭")
    print()
    
    mickey = MickeyDemo()
    print(f"🎉 Welcome! {mickey.name} is ready to entertain you!")
    print()
    
    # Demo 1: Wave
    print("🎬 DEMO 1: Mickey waves hello!")
    print("-" * 40)
    mickey.wave("friendly")
    print()
    
    # Demo 2: Sing
    print("🎬 DEMO 2: Mickey sings a song!")
    print("-" * 40)
    mickey.sing()
    print()
    
    # Demo 3: Dance
    print("🎬 DEMO 3: Mickey dances!")
    print("-" * 40)
    mickey.dance()
    print()
    
    # Demo 4: Full Show
    print("🎬 DEMO 4: Mickey puts on a full show!")
    print("-" * 40)
    mickey.perform_show()
    print()
    
    # Status
    status = mickey.get_status()
    print("📊 Mickey's Final Status:")
    print("-" * 30)
    for key, value in status.items():
        print(f"   {key.title()}: {value}")
    
    print()
    print("🎭 Demo complete! Mickey Mouse Agent is working perfectly!")
    print("🐭 Thanks for watching the show!")

if __name__ == "__main__":
    main()