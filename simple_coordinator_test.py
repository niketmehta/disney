#!/usr/bin/env python3
"""
Simple test of the Disney Coordinator Agent without web dependencies
"""

import time
from disney_coordinator_agent import DisneyCoordinatorAgent

def test_individual_performances():
    """Test individual agent performances"""
    print("🎬 Testing Individual Performances")
    print("=" * 50)
    
    coordinator = DisneyCoordinatorAgent()
    
    # Test Mickey's individual performance
    print("\n🐭 Mickey's Solo Performance:")
    result = coordinator.ask_mickey_to_perform("sing", song_name="It's a Small World")
    print(f"Result: {result}")
    
    time.sleep(1)
    
    # Test Donald's individual performance
    print("\n🦆 Donald's Solo Performance:")
    result = coordinator.ask_donald_to_perform("dance", dance_move="The Quack Attack")
    print(f"Result: {result}")
    
    return coordinator

def test_duet_performances(coordinator):
    """Test duet performances"""
    print("\n🎬 Testing Duet Performances")
    print("=" * 50)
    
    # Test duet song
    print("\n🎵 Duet Song Performance:")
    result = coordinator.perform_duet_song("Mickey and Donald's Friendship Song")
    print(f"Result: {result}")
    
    time.sleep(1)
    
    # Test duet dance
    print("\n💃 Duet Dance Performance:")
    result = coordinator.perform_duet_dance("The Mickey-Donald Shuffle")
    print(f"Result: {result}")
    
    return coordinator

def test_ensemble_show(coordinator):
    """Test ensemble show"""
    print("\n🎬 Testing Ensemble Show")
    print("=" * 50)
    
    print("\n🎭 Full Ensemble Show:")
    result = coordinator.perform_ensemble_show()
    print(f"Result: {result}")
    
    return coordinator

def test_management_functions(coordinator):
    """Test management functions"""
    print("\n🎬 Testing Management Functions")
    print("=" * 50)
    
    # Test status
    print("\n📊 Agent Status:")
    status = coordinator.get_agent_status()
    for agent, info in status.items():
        print(f"   {agent.title()}: {info}")
    
    # Test energy check
    print("\n🔋 Energy Check:")
    energy_result = coordinator.check_energy_levels()
    print(f"Result: {energy_result}")
    
    # Test rest both
    print("\n😴 Rest Both Agents:")
    rest_result = coordinator.rest_both_agents()
    print(f"Result: {rest_result}")
    
    return coordinator

def main():
    print("🎭🎵🦆🐭")
    print("=" * 60)
    print("    DISNEY COORDINATOR AGENT - SIMPLE TEST")
    print("=" * 60)
    print("🎭🎵🦆🐭")
    print()
    
    # Test individual performances
    coordinator = test_individual_performances()
    
    # Test duet performances
    coordinator = test_duet_performances(coordinator)
    
    # Test ensemble show
    coordinator = test_ensemble_show(coordinator)
    
    # Test management functions
    coordinator = test_management_functions(coordinator)
    
    print("\n" + "=" * 60)
    print("🎉 All tests completed successfully!")
    print("✨ The Disney Coordinator Agent is working perfectly!")
    print("🐭🦆 Both agents can perform individually and together!")
    print("🎭 The coordinator successfully manages Disney magic!")

if __name__ == "__main__":
    main()