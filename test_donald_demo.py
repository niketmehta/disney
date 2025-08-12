#!/usr/bin/env python3
"""
Test script to demonstrate the Donald Duck Agent functionality
"""

import requests
import time
import json

def test_donald_agent():
    """Test the Donald Duck Agent API endpoints"""
    base_url = "http://localhost:5001"
    
    print("🦆 Testing Donald Duck Agent - Quack-tastic Version!")
    print("=" * 50)
    
    # Test 1: Get status
    print("\n1. 📊 Getting Donald's status...")
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
            json={"song_name": "Quack Quack Quack"}
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
            json={"dance_move": "The Quack Attack"}
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
    print("\n📝 Donald's unique features:")
    print("   • 🦆 Quack-tastic personality and energy")
    print("   • 🎵 Donald-themed songs and lyrics")
    print("   • 💃 Duck-specific dance moves")
    print("   • 🎭 Energetic performance style")
    print("   • ✨ Orange-themed Disney styling")
    print("   • 🌟 Quack-tastic magic elements")

    print("\n🌐 Open http://localhost:5001 in your browser to see Donald in action!")

if __name__ == "__main__":
    test_donald_agent()