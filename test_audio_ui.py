#!/usr/bin/env python3
"""
Test script to demonstrate audio capabilities and UI connection
"""

import time
import sys
import os

# Add the current directory to the path so we can import the coordinator
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the coordinator class directly from the web app file
from coordinator_web_app import DisneyCoordinatorWeb

def test_audio_capabilities():
    """Test the audio capabilities of the coordinator."""
    print("🎭🎵🦆🐭")
    print("=" * 60)
    print("    AUDIO CAPABILITIES TEST")
    print("=" * 60)
    print("🎭🎵🦆🐭")
    print()
    
    coordinator = DisneyCoordinatorWeb()
    print(f"🎉 Welcome! {coordinator.name} is ready to test audio!")
    print(f"🎵 Audio system: {coordinator.get_coordinator_status()['audio_system']}")
    print()
    
    # Test individual performances with audio
    print("🎬 Testing Individual Performances with Audio:")
    print("-" * 50)
    
    print("🐭 Mickey's solo performance with audio:")
    print("-" * 40)
    result = coordinator.ask_mickey_to_perform("sing", song_name="It's a Small World")
    print(f"Result: {result}")
    print()
    
    time.sleep(1)
    
    print("🦆 Donald's solo performance with audio:")
    print("-" * 40)
    result = coordinator.ask_donald_to_perform("dance", dance_move="The Quack Attack")
    print(f"Result: {result}")
    print()
    
    # Test duet performance with audio
    print("🎬 Testing Duet Performance with Audio:")
    print("-" * 50)
    
    print("🎵 Mickey and Donald duet with real audio:")
    print("-" * 40)
    result = coordinator.perform_duet_song("Mickey and Donald's Friendship Song")
    print(f"Result: {result}")
    print()
    
    print("🎭 Audio capabilities test complete!")
    print("🎵 You should have heard musical tones during the performances!")
    print("🌐 Open coordinator_audio_web.html in your browser for the full UI experience!")

if __name__ == "__main__":
    test_audio_capabilities()