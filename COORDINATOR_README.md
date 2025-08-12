# 🎭 Disney Coordinator Agent

A magical coordinator agent that manages both Mickey Mouse and Donald Duck agents, enabling individual and collaborative performances!

## ✨ Features

### 🎭 Individual Agent Management
- **Mickey Mouse Control**: Ask Mickey to sing, dance, wave, perform shows, or rest
- **Donald Duck Control**: Ask Donald to sing, dance, wave, perform shows, or rest
- **Real-time Status**: Monitor energy levels and performance status of both agents

### 🎵 Duet Performances
- **Duet Songs**: Mickey and Donald sing together in perfect harmony
- **Duet Dances**: Synchronized dance routines performed by both agents
- **Ensemble Shows**: Complete performances featuring both individual and collaborative acts

### ⚙️ Management Features
- **Energy Monitoring**: Track energy levels of both agents
- **Coordinated Rest**: Both agents rest together to regain energy
- **Performance Scheduling**: Prevent conflicts when agents are already performing
- **Status Reporting**: Comprehensive status information for all agents

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install flask requests
```

### 2. Run the Coordinator Agent
```bash
python coordinator_app.py
```

### 3. Access the Web Interface
Open your browser and go to: `http://localhost:5002`

### 4. Run the Demo
```bash
python coordinator_demo.py
```

### 5. Test the API
```bash
python test_coordinator.py
```

## 🎬 Available Performances

### Individual Performances
Each agent can perform individually:

**Mickey Mouse:**
- 🎤 Sing (with various Disney songs)
- 💃 Dance (with unique Mickey dance moves)
- 👋 Wave (in different styles)
- 🎭 Full Show (complete performance)
- 😴 Rest (regain energy)

**Donald Duck:**
- 🎤 Sing (with Donald-themed songs)
- 💃 Dance (with energetic duck moves)
- 👋 Wave (with Donald's style)
- 🎭 Full Show (complete performance)
- 😴 Rest (regain energy)

### Duet Performances
Both agents perform together:

**Duet Songs:**
- "Mickey and Donald's Friendship Song"
- "The Disney Duet"
- "Best Friends Forever"
- "Magical Partners"
- "Disney Harmony"

**Duet Dances:**
- "The Mickey-Donald Shuffle"
- "Friendship Waltz"
- "Disney Duo Dance"
- "Magical Partners Spin"
- "Best Friends Bounce"

**Ensemble Shows:**
- Complete performances featuring:
  - Synchronized opening waves
  - Duet songs
  - Individual spotlight moments
  - Duet dance finale
  - Coordinated closing bows

## 🌐 API Endpoints

### Individual Agent Management
```
POST /api/mickey/{action}     # Control Mickey (sing, dance, wave, show, rest)
POST /api/donald/{action}     # Control Donald (sing, dance, wave, show, rest)
```

### Duet Performances
```
POST /api/duet/song           # Perform duet song
POST /api/duet/dance          # Perform duet dance
POST /api/ensemble/show       # Perform full ensemble show
```

### Management
```
GET  /api/status              # Get status of coordinator and agents
GET  /api/energy              # Check energy levels
POST /api/rest/both           # Rest both agents
GET  /api/available           # Get available performance types
```

## 🎭 Web Interface Features

### Agent Cards
- Real-time status display for each agent
- Energy level indicators
- Performance status (Available/Performing)
- Individual action buttons for each agent

### Duet Section
- Dedicated section for collaborative performances
- Easy-to-use buttons for duet songs, dances, and ensemble shows
- Visual indicators showing both agents working together

### Management Panel
- Status monitoring
- Energy level checking
- Coordinated rest functionality
- Real-time status display

## 🔧 Technical Details

### Architecture
- **Coordinator Agent**: Manages both Mickey and Donald agents
- **Web Interface**: Beautiful, responsive UI built with HTML/CSS/JavaScript
- **API Layer**: RESTful API for programmatic access
- **Threading**: Non-blocking performances using background threads

### Agent Integration
- **Minimal Changes**: Original Mickey and Donald agents remain largely unchanged
- **Wrapper Functions**: Coordinator provides wrapper methods for agent actions
- **State Management**: Tracks performance states to prevent conflicts
- **Energy Management**: Monitors and manages energy levels across agents

### Performance Features
- **Synchronization**: Ensures both agents are available before duet performances
- **Visual Feedback**: Rich console output with emojis and animations
- **Error Handling**: Graceful handling of conflicts and errors
- **Real-time Updates**: Live status updates in the web interface

## 🎪 Example Usage

### Python API Usage
```python
from disney_coordinator_agent import DisneyCoordinatorAgent

# Create coordinator
coordinator = DisneyCoordinatorAgent()

# Individual performances
coordinator.ask_mickey_to_perform("sing", song_name="It's a Small World")
coordinator.ask_donald_to_perform("dance", dance_move="The Quack Attack")

# Duet performances
coordinator.perform_duet_song("Mickey and Donald's Friendship Song")
coordinator.perform_duet_dance("The Mickey-Donald Shuffle")
coordinator.perform_ensemble_show()

# Management
coordinator.check_energy_levels()
coordinator.rest_both_agents()
status = coordinator.get_agent_status()
```

### HTTP API Usage
```bash
# Get status
curl http://localhost:5002/api/status

# Ask Mickey to sing
curl -X POST http://localhost:5002/api/mickey/sing \
  -H "Content-Type: application/json" \
  -d '{"song_name": "It\'s a Small World"}'

# Perform duet song
curl -X POST http://localhost:5002/api/duet/song \
  -H "Content-Type: application/json" \
  -d '{"song_name": "Mickey and Donald\'s Friendship Song"}'

# Rest both agents
curl -X POST http://localhost:5002/api/rest/both
```

## 🎨 Customization

### Adding New Duet Songs
```python
# In disney_coordinator_agent.py, add to duet_songs list:
self.duet_songs.append("Your New Duet Song")

# Add lyrics in _get_duet_lyrics method:
lyrics_dict["Your New Duet Song"] = [
    "Mickey: Your lyrics here...",
    "Donald: Donald's part here...",
    # ... more lyrics
]
```

### Adding New Duet Dances
```python
# In disney_coordinator_agent.py, add to duet_dances list:
self.duet_dances.append("Your New Duet Dance")

# Add steps in _get_duet_dance_steps method:
steps_dict["Your New Duet Dance"] = [
    "💃 Step description 1",
    "💃 Step description 2",
    # ... more steps
]
```

## 🐛 Troubleshooting

### Common Issues
1. **Port Already in Use**: Change port in `coordinator_app.py`
2. **Agent Conflicts**: Check if agents are already performing
3. **Energy Issues**: Use rest functions to restore energy
4. **Web Interface Not Loading**: Ensure Flask is running and port is accessible

### Debug Mode
Run with debug enabled:
```bash
python coordinator_app.py
```
Check console output for detailed performance information.

## 🎉 Contributing

Feel free to enhance the coordinator agent with:
- New duet performances
- Additional management features
- Enhanced web interface
- More agent integrations
- Performance optimizations

## 📄 License

This project is part of the Disney Agent ecosystem. Enjoy the magic! ✨

---

**🎭 Disney Coordinator Agent** - Orchestrating Disney Magic Together! 🐭🦆✨