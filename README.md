# 🎭 Disney Coordinator Agent

A magical agent that coordinates Mickey Mouse and Donald Duck performances with rich visual audio experience!

## 🎵 Features

- **Individual Performances**: Mickey and Donald can sing, dance, wave, perform shows, and rest
- **Duet Performances**: Mickey and Donald perform together in harmony
- **Visual Audio System**: Rich musical experience through visual symbols and animations
- **Web Interface**: Beautiful HTML interface with real-time visual feedback
- **Command Line Interface**: Interactive CLI for direct control
- **Energy Management**: Track and manage agent energy levels

## 📁 Repository Structure

```
disney-coordinator/
├── mickey_mouse_agent.py      # Mickey Mouse agent
├── donald_duck_agent.py       # Donald Duck agent
├── disney_coordinator.py      # Main coordinator with visual audio
├── web_server.py              # Web server with HTML interface
├── cli.py                     # Command line interface
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Choose Your Interface

#### **Web Interface (Recommended)**
```bash
python3 web_server.py
```
Then open: http://localhost:8081

#### **Command Line Interface**
```bash
python3 cli.py
```

## 🎭 Available Performances

### Individual Actions
- **Mickey**: sing, dance, wave, show, rest
- **Donald**: sing, dance, wave, show, rest

### Duet Performances
- **Duet Song**: Mickey and Donald sing together
- **Duet Dance**: Mickey and Donald dance together
- **Ensemble Show**: Complete performance with both agents

### Management
- **Status Check**: View agent status and energy
- **Energy Management**: Monitor and restore energy levels

## 🎵 Visual Audio System

The coordinator uses a rich visual audio system that works in any environment:

### Musical Symbols
- **Notes**: ♪ ♫ ♬ ♩ ♭ ♮ ♯
- **Harmony**: 🎵 🎶 🎼 🎤 🎧 🎹 🎸 🎺 🎻

### Example Performance
```
🎵 Mickey and Donald are performing duet with visual audio!
🎼 Playing melody: ♪ ♬ ♭ ♪ ♬ ♭ ♮ ♭ 
🎵 ♪ Playing note C ♪....
🎵 ♬ Playing note E ♬....
🎵 DUET HARMONY:
🐭 Mickey: We're the best of friends, you and me!
🦆 Donald: Quack quack, that's how it should be!
🎶 Harmony: 🎧 🎶 🎺 🎸 
```

## 🖥️ Web Interface Features

- **Beautiful UI**: Modern, responsive design
- **Real-time Feedback**: See performances as they happen
- **Visual Console**: Watch musical symbols and animations
- **Interactive Buttons**: Easy-to-use controls
- **Status Display**: Real-time agent information

## 💻 CLI Commands

### Quick Commands
```bash
duet              # Mickey and Donald sing together
mickey sing       # Mickey sings
donald dance      # Donald dances
ensemble          # Complete ensemble show
status            # Check agent status
energy            # Check energy levels
help              # Show all commands
quit              # Exit
```

### Full Command List
```bash
# Individual Actions
mickey sing       # Mickey sings with visual audio
mickey dance      # Mickey dances with visual audio
mickey wave       # Mickey waves with visual audio
mickey show       # Mickey performs a show
mickey rest       # Mickey takes a rest
donald sing       # Donald sings with visual audio
donald dance      # Donald dances with visual audio
donald wave       # Donald waves with visual audio
donald show       # Donald performs a show
donald rest       # Donald takes a rest

# Duet Performances
duet              # Mickey and Donald sing together
duet song         # Mickey and Donald sing together
duet dance        # Mickey and Donald dance together
ensemble          # Complete ensemble show

# Management
status            # Check agent status
energy            # Check energy levels
rest both         # Both agents rest
help              # Show this help
quit              # Exit the program
```

## 🎯 Usage Examples

### Web Interface
1. Start the server: `python3 web_server.py`
2. Open browser: http://localhost:8081
3. Click buttons to trigger performances
4. Watch the visual console for musical feedback

### Command Line
```bash
# Start CLI
python3 cli.py

# Quick duet performance
🎭 Enter command: duet

# Check status
🎭 Enter command: status

# Mickey sings
🎭 Enter command: mickey sing

# Donald dances
🎭 Enter command: donald dance
```

## 🔧 Technical Details

### Architecture
- **Loose Coupling**: Original Mickey and Donald agents unchanged
- **Visual Audio**: Musical experience through symbols and animations
- **Threading**: Non-blocking performances in web interface
- **State Management**: Prevents overlapping performances

### Audio System
- **Visual Notes**: Musical symbols represent different notes
- **Harmony Display**: Multiple symbols for duet performances
- **Animation**: Animated dots show note duration
- **Environment Independent**: Works in any system

### Web Server
- **Port**: 8081
- **Framework**: Python http.server
- **API**: RESTful endpoints for all actions
- **Real-time**: Immediate visual feedback

## 🎉 Why This Works

1. **No Audio Dependencies**: Works in any environment
2. **Rich Visual Experience**: Musical symbols and animations
3. **Real-time Feedback**: See performances as they happen
4. **Interactive Interfaces**: Both web and CLI options
5. **Consolidated Code**: Clean, maintainable structure

## 🚀 Getting Started

1. **Clone the repository**
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Choose your interface**:
   - Web: `python3 web_server.py` → http://localhost:8081
   - CLI: `python3 cli.py`
4. **Enjoy the performances!**

## 🎭 Example Session

```bash
$ python3 cli.py

🎭🎵🦆🐭
============================================================
    DISNEY COORDINATOR CLI - VISUAL AUDIO
============================================================
🎭🎵🦆🐭

🎉 Welcome! Disney Coordinator (Visual Audio) is ready!
✨ This version uses rich visual audio simulation!
🎵 Musical symbols and animations create the audio experience!

🎭 Quick Start:
   • Type 'duet' for Mickey and Donald to perform together
   • Type 'mickey sing' for Mickey to sing
   • Type 'donald dance' for Donald to dance
   • Type 'help' for all commands
   • Type 'quit' to exit

🎭 Enter command: duet

🎵 Performing duet song with visual audio!
🎵 Mickey and Donald are performing duet 'The Disney Duet' with visual audio!
🎼 Playing melody: ♪ ♬ ♭ ♪ ♬ ♭ ♮ ♭ 
🎵 ♪ Playing note C ♪....
🎵 ♬ Playing note E ♬....
🎵 DUET HARMONY:
🐭 Mickey: Disney magic in the air!
🦆 Donald: Quack quack, everywhere!
🎶 Harmony: 🎧 🎶 🎺 🎸 

🎵 Mickey Mouse and Donald Duck finished their duet 'The Disney Duet'! What a magical performance! ✨
```

## 🎵 Enjoy the Magic!

Experience Mickey and Donald's musical performances with rich visual audio feedback. Whether you prefer the web interface or command line, you'll get a magical Disney experience with musical symbols, harmonies, and animations!

**🎭 Run `python3 web_server.py` and open http://localhost:8081 for the full experience! 🐭🦆🎵**