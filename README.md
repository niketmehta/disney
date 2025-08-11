# 🐭 Mickey Mouse Agent

A delightful and interactive Mickey Mouse agent that can sing, wave, and dance! This project features both a beautiful web interface and a command-line interface for interacting with everyone's favorite Disney character.

## ✨ Features

- **🎤 Singing**: Mickey can sing classic Disney songs with full lyrics
- **👋 Waving**: Multiple wave styles including friendly, excited, royal, magical, and goofy
- **💃 Dancing**: Various dance moves like the Mickey Shuffle, Hot Dog Dance, and more
- **🎭 Full Shows**: Complete performances combining singing, waving, and dancing
- **😴 Rest System**: Energy management with rest functionality
- **📊 Status Tracking**: Real-time status monitoring
- **🌐 Web Interface**: Beautiful, responsive web UI
- **💻 CLI Interface**: Command-line interface for direct interaction

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the web application**:
   ```bash
   python app.py
   ```

4. **Open your browser and visit**:
   ```
   http://localhost:5000
   ```

## 🎮 Usage

### Web Interface

The web interface provides a beautiful, modern UI with:

- **Status Dashboard**: Real-time display of Mickey's energy, mood, and performance status
- **Interactive Controls**: Easy-to-use buttons for all Mickey's actions
- **Song Selection**: Choose from classic Disney songs or let Mickey pick randomly
- **Wave Styles**: Select different wave styles for different occasions
- **Dance Moves**: Pick specific dances or enjoy random performances
- **Activity Log**: Track all of Mickey's activities in real-time

### Command Line Interface

For a more direct interaction, use the CLI:

```bash
python mickey_cli.py
```

The CLI provides:
- Interactive menu system
- Song and dance selection
- Status checking
- Full show performances

## 🎵 Available Songs

- "It's a Small World"
- "When You Wish Upon a Star"
- "Mickey Mouse Club March"
- "Zip-a-Dee-Doo-Dah"
- "Heigh-Ho"
- "Whistle While You Work"

## 💃 Available Dances

- The Mickey Shuffle
- The Hot Dog Dance
- The Sorcerer's Apprentice Spin
- The Steamboat Willie Jig
- The Fantasia Waltz
- The Clubhouse Bounce

## 👋 Wave Styles

- **Friendly**: Standard friendly wave
- **Excited**: Enthusiastic wave with sparkles
- **Royal**: Elegant wave with crown
- **Magical**: Mystical wave with stars
- **Goofy**: Silly wave with funny face

## 🏗️ Project Structure

```
mickey-mouse-agent/
├── mickey_mouse_agent.py    # Core Mickey Mouse agent class
├── app.py                   # Flask web application
├── mickey_cli.py           # Command-line interface
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Web interface template
└── README.md              # This file
```

## 🔧 API Endpoints

The web application provides the following REST API endpoints:

- `GET /` - Main web interface
- `POST /api/sing` - Make Mickey sing a song
- `POST /api/wave` - Make Mickey wave
- `POST /api/dance` - Make Mickey dance
- `POST /api/show` - Make Mickey perform a full show
- `POST /api/rest` - Make Mickey rest
- `GET /api/status` - Get Mickey's current status

## 🎨 Customization

### Adding New Songs

To add new songs, modify the `songs` list in the `MickeyMouseAgent` class and add corresponding lyrics in the `_get_song_lyrics` method.

### Adding New Dances

To add new dances, modify the `dance_moves` list and add corresponding dance steps in the `_get_dance_steps` method.

### Adding New Wave Styles

To add new wave styles, modify the `wave_styles` dictionary in the `wave` method.

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**: If port 5000 is busy, modify the port in `app.py`
2. **Dependencies not found**: Make sure to run `pip install -r requirements.txt`
3. **Permission errors**: Ensure you have write permissions in the project directory

### Debug Mode

To run in debug mode for development:

```bash
export FLASK_ENV=development
python app.py
```

## 🤝 Contributing

Feel free to contribute to this project by:

1. Adding new songs and dances
2. Improving the UI/UX
3. Adding new features
4. Fixing bugs
5. Improving documentation

## 📄 License

This project is for educational and entertainment purposes. Mickey Mouse is a trademark of The Walt Disney Company.

## 🙏 Acknowledgments

- Inspired by the magic of Disney
- Built with love for Mickey Mouse fans everywhere
- Special thanks to Walt Disney for creating such an iconic character

---

**🎭 Have a magical time with Mickey Mouse! 🐭**