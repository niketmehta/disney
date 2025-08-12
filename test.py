#!/usr/bin/env python3
"""
Simple test script to verify Disney Coordinator components work together
"""

def test_imports():
    """Test that all modules can be imported."""
    print("🧪 Testing imports...")
    
    try:
        from mickey_mouse_agent import MickeyMouseAgent
        print("✅ Mickey Mouse agent imported")
    except Exception as e:
        print(f"❌ Mickey Mouse agent import failed: {e}")
        return False
    
    try:
        from donald_duck_agent import DonaldDuckAgent
        print("✅ Donald Duck agent imported")
    except Exception as e:
        print(f"❌ Donald Duck agent import failed: {e}")
        return False
    
    try:
        from disney_coordinator import DisneyCoordinatorVisualAudio
        print("✅ Disney Coordinator imported")
    except Exception as e:
        print(f"❌ Disney Coordinator import failed: {e}")
        return False
    
    try:
        from web_server import DisneyVisualAudioHandler
        print("✅ Web Server imported")
    except Exception as e:
        print(f"❌ Web Server import failed: {e}")
        return False
    
    return True

def test_coordinator():
    """Test basic coordinator functionality."""
    print("\n🧪 Testing coordinator functionality...")
    
    try:
        from disney_coordinator import DisneyCoordinatorVisualAudio
        coordinator = DisneyCoordinatorVisualAudio()
        
        # Test status
        status = coordinator.get_coordinator_status()
        print(f"✅ Coordinator status: {status['coordinator_name']}")
        
        # Test agent status
        agents = coordinator.get_agent_status()
        print(f"✅ Mickey energy: {agents['mickey']['energy']}%")
        print(f"✅ Donald energy: {agents['donald']['energy']}%")
        
        return True
    except Exception as e:
        print(f"❌ Coordinator test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🎭 Disney Coordinator Test Suite")
    print("=" * 40)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed!")
        return
    
    # Test coordinator
    if not test_coordinator():
        print("\n❌ Coordinator tests failed!")
        return
    
    print("\n🎉 All tests passed!")
    print("\n🚀 Ready to use:")
    print("   • Web Interface: python3 web_server.py")
    print("   • CLI Interface: python3 cli.py")
    print("   • Then open: http://localhost:8081")

if __name__ == "__main__":
    main()