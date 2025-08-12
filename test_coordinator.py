#!/usr/bin/env python3
"""
Test script to verify the Disney Coordinator Agent functionality
"""

import requests
import time
import json

def test_coordinator_agent():
    """Test the Disney Coordinator Agent API endpoints"""
    base_url = "http://localhost:5002"
    
    print("🎭 Testing Disney Coordinator Agent - Orchestrating Disney Magic!")
    print("=" * 60)
    
    # Test 1: Get status
    print("\n1. 📊 Getting coordinator and agents status...")
    try:
        response = requests.get(f"{base_url}/api/status")
        status = response.json()
        print(f"   ✅ Status: {json.dumps(status, indent=2)}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 2: Individual Mickey performance
    print("\n2. 🐭 Testing Mickey's individual performance...")
    try:
        response = requests.post(
            f"{base_url}/api/mickey/sing",
            json={"song_name": "It's a Small World"}
        )
        result = response.json()
        print(f"   ✅ Mickey sing result: {result['message']}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: Individual Donald performance
    print("\n3. 🦆 Testing Donald's individual performance...")
    try:
        response = requests.post(
            f"{base_url}/api/donald/dance",
            json={"dance_move": "The Quack Attack"}
        )
        result = response.json()
        print(f"   ✅ Donald dance result: {result['message']}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 4: Duet song
    print("\n4. 🎵 Testing duet song performance...")
    try:
        response = requests.post(
            f"{base_url}/api/duet/song",
            json={"song_name": "Mickey and Donald's Friendship Song"}
        )
        result = response.json()
        print(f"   ✅ Duet song result: {result['message']}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 5: Duet dance
    print("\n5. 💃 Testing duet dance performance...")
    try:
        response = requests.post(
            f"{base_url}/api/duet/dance",
            json={"dance_name": "The Mickey-Donald Shuffle"}
        )
        result = response.json()
        print(f"   ✅ Duet dance result: {result['message']}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 6: Ensemble show
    print("\n6. 🎭 Testing ensemble show...")
    try:
        response = requests.post(f"{base_url}/api/ensemble/show")
        result = response.json()
        print(f"   ✅ Ensemble show result: {result['message']}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 7: Energy check
    print("\n7. 🔋 Testing energy check...")
    try:
        response = requests.get(f"{base_url}/api/energy")
        result = response.json()
        print(f"   ✅ Energy check result: {result['message']}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 8: Rest both agents
    print("\n8. 😴 Testing rest both agents...")
    try:
        response = requests.post(f"{base_url}/api/rest/both")
        result = response.json()
        print(f"   ✅ Rest both result: {result['message']}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 9: Get available performances
    print("\n9. 📋 Testing available performances...")
    try:
        response = requests.get(f"{base_url}/api/available")
        performances = response.json()
        print(f"   ✅ Available performances: {json.dumps(performances, indent=2)}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 Testing completed!")
    print("\n📝 Coordinator's unique features:")
    print("   • 🎭 Individual agent management (Mickey & Donald)")
    print("   • 🎵 Duet song performances")
    print("   • 💃 Duet dance routines")
    print("   • 🎭 Full ensemble shows")
    print("   • 🔋 Energy level monitoring")
    print("   • 😴 Coordinated rest periods")
    print("   • 📊 Real-time status tracking")
    print("   • ✨ Disney magic coordination")

    print("\n🌐 Open http://localhost:5002 in your browser to see the coordinator in action!")

if __name__ == "__main__":
    test_coordinator_agent()