#!/usr/bin/env python3
"""
Test script to demonstrate the improved Mickey Mouse Agent functionality
"""

import requests
import time
import json

def test_mickey_agent():
    """Test the Mickey Mouse Agent API endpoints"""
    base_url = "http://localhost:5000"
    
    print("🎭 Testing Mickey Mouse Agent - Enhanced Version!")
    print("=" * 50)
    
    # Test 1: Get status
    print("\n1. 📊 Getting Mickey's status...")
    try:
        response = requests.get(f"{base_url}/api/status")
        status = response.json()
        print(f"   ✅ Status: {status}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 2: Wave
    print("\n2. 👋 Testing wave functionality...")
    try:
        response = requests.post(
            f"{base_url}/api/wave",
            json={"style": "excited"}
        )
        result = response.json()
        print(f"   ✅ Wave result: {result['message']}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: Sing
    print("\n3. 🎤 Testing sing functionality...")
    try:
        response = requests.post(
            f"{base_url}/api/sing",
            json={"song_name": "It's a Small World"}
        )
        result = response.json()
        print(f"   ✅ Sing result: {result['message']}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 4: Dance
    print("\n4. 💃 Testing dance functionality...")
    try:
        response = requests.post(
            f"{base_url}/api/dance",
            json={"dance_move": "The Hot Dog Dance"}
        )
        result = response.json()
        print(f"   ✅ Dance result: {result['message']}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 5: Full show
    print("\n5. 🎭 Testing full show...")
    try:
        response = requests.post(f"{base_url}/api/show")
        result = response.json()
        print(f"   ✅ Show result: {result['message']}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 6: Rest
    print("\n6. 😴 Testing rest functionality...")
    try:
        response = requests.post(f"{base_url}/api/rest")
        result = response.json()
        print(f"   ✅ Rest result: {result['message']}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 Testing completed!")
    print("\n📝 What's been improved:")
    print("   • 🎵 Audio playback using Web Audio API in the browser")
    print("   • 🎭 Visual animations for Mickey's avatar")
    print("   • 👋 Enhanced wave sequences with multiple emojis")
    print("   • 💃 Better dance step visualization")
    print("   • 🎤 Improved singing with alternating emojis")
    print("   • 😴 Visual rest sequence")
    print("\n🌐 Open http://localhost:5000 in your browser to see the full experience!")

if __name__ == "__main__":
    test_mickey_agent()