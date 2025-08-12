#!/usr/bin/env python3
"""
Simple test to demonstrate working audio with system beeps
"""

import time
from disney_coordinator_working_audio import DisneyCoordinatorWorkingAudio

def test_working_audio():
    """Test the working audio capabilities."""
    print("🎭🎵🦆🐭")
    print("=" * 60)
    print("    WORKING AUDIO TEST")
    print("=" * 60)
    print("🎭🎵🦆🐭")
    print()
    
    coordinator = DisneyCoordinatorWorkingAudio()
    print(f"🎉 Welcome! {coordinator.name} is ready to test working audio!")
    print("🔊 You should hear actual beeps during this test!")
    print()
    
    # Test 1: Simple beep
    print("🔊 Test 1: Simple beep")
    print("You should hear a beep now...")
    coordinator._generate_beep(0.5)
    print("✅ Beep test complete!")
    print()
    
    # Test 2: Musical melody
    print("🎵 Test 2: Musical melody")
    print("You should hear a sequence of beeps...")
    melody = ["C", "E", "G", "C"]
    coordinator._play_melody(melody, 0.3)
    print("✅ Melody test complete!")
    print()
    
    # Test 3: Mickey's performance with audio
    print("🐭 Test 3: Mickey's performance with audio")
    print("You should hear musical intro, performance, and outro...")
    result = coordinator.ask_mickey_to_perform("sing", song_name="Test Song")
    print(f"Result: {result}")
    print()
    
    # Test 4: Donald's performance with audio
    print("🦆 Test 4: Donald's performance with audio")
    print("You should hear musical intro, performance, and outro...")
    result = coordinator.ask_donald_to_perform("dance", dance_move="Test Dance")
    print(f"Result: {result}")
    print()
    
    # Test 5: Duet with working audio
    print("🎵 Test 5: Duet with working audio")
    print("You should hear a full duet performance with multiple beeps...")
    result = coordinator.perform_duet_song("Mickey and Donald's Friendship Song")
    print(f"Result: {result}")
    print()
    
    print("🎭 Working audio test complete!")
    print("🔊 If you heard beeps, the audio system is working!")
    print("🎵 Your Disney duets now have real audio!")

if __name__ == "__main__":
    test_working_audio()