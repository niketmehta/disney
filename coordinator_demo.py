#!/usr/bin/env python3
"""
Disney Coordinator Agent Demo
Showcasing individual and collaborative performances with Mickey and Donald
"""

import time
from disney_coordinator_agent import DisneyCoordinatorAgent

def main():
    print("🎭🎵🦆🐭")
    print("=" * 60)
    print("    DISNEY COORDINATOR AGENT DEMO")
    print("=" * 60)
    print("🎭🎵🦆🐭")
    print()
    
    coordinator = DisneyCoordinatorAgent()
    print(f"🎉 Welcome! {coordinator.name} is ready to orchestrate Disney magic!")
    print()
    
    # Demo 1: Individual Performances
    print("🎬 DEMO 1: Individual Agent Performances")
    print("-" * 50)
    
    print("🐭 Mickey's solo performance:")
    print("-" * 30)
    result = coordinator.ask_mickey_to_perform("sing", song_name="It's a Small World")
    print(f"Result: {result}")
    print()
    
    time.sleep(1)
    
    print("🦆 Donald's solo performance:")
    print("-" * 30)
    result = coordinator.ask_donald_to_perform("dance", dance_move="The Quack Attack")
    print(f"Result: {result}")
    print()
    
    time.sleep(1)
    
    # Demo 2: Duet Performances
    print("🎬 DEMO 2: Duet Performances")
    print("-" * 50)
    
    print("🎵 Mickey and Donald singing together:")
    print("-" * 40)
    result = coordinator.perform_duet_song("Mickey and Donald's Friendship Song")
    print(f"Result: {result}")
    print()
    
    time.sleep(1)
    
    print("💃 Mickey and Donald dancing together:")
    print("-" * 40)
    result = coordinator.perform_duet_dance("The Mickey-Donald Shuffle")
    print(f"Result: {result}")
    print()
    
    time.sleep(1)
    
    # Demo 3: Ensemble Show
    print("🎬 DEMO 3: Full Ensemble Show")
    print("-" * 50)
    result = coordinator.perform_ensemble_show()
    print(f"Result: {result}")
    print()
    
    time.sleep(1)
    
    # Demo 4: Management Functions
    print("🎬 DEMO 4: Management Functions")
    print("-" * 50)
    
    print("📊 Status Check:")
    print("-" * 20)
    status = coordinator.get_agent_status()
    for agent, info in status.items():
        print(f"   {agent.title()}: {info}")
    print()
    
    print("🔋 Energy Check:")
    print("-" * 20)
    energy_result = coordinator.check_energy_levels()
    print(f"Result: {energy_result}")
    print()
    
    print("😴 Rest Both Agents:")
    print("-" * 25)
    rest_result = coordinator.rest_both_agents()
    print(f"Result: {rest_result}")
    print()
    
    # Demo 5: Available Performances
    print("🎬 DEMO 5: Available Performances")
    print("-" * 50)
    performances = coordinator.get_available_performances()
    for category, items in performances.items():
        print(f"   {category.title()}:")
        if isinstance(items, dict):
            for agent, actions in items.items():
                print(f"     {agent.title()}: {', '.join(actions)}")
        else:
            print(f"     {', '.join(items)}")
    print()
    
    # Demo 6: Coordinator Status
    print("🎬 DEMO 6: Coordinator Status")
    print("-" * 50)
    coord_status = coordinator.get_coordinator_status()
    for key, value in coord_status.items():
        print(f"   {key.replace('_', ' ').title()}: {value}")
    print()
    
    print("🎭 Demo complete! Disney Coordinator Agent is working perfectly!")
    print("🐭🦆 Thanks for watching the magical Disney performances!")
    print("✨ The coordinator successfully managed both agents individually and together!")

if __name__ == "__main__":
    main()