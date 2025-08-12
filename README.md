# 🎭 Disney Agents - Mickey Mouse & Donald Duck

A delightful interactive Disney experience featuring **two independent agents** - Mickey Mouse and Donald Duck - each with their own unique personality, styling, and animations!

## 🎉 **Two Independent Disney Agents**

### 🐭 **Mickey Mouse Agent**
- **Port**: 5000
- **URL**: http://localhost:5000
- **Personality**: Happy, magical, friendly
- **Color Theme**: Red and purple gradients
- **Magic Element**: ✨ Disney Magic ✨

### 🦆 **Donald Duck Agent**
- **Port**: 5001
- **URL**: http://localhost:5001
- **Personality**: Energetic, feisty, quack-tastic
- **Color Theme**: Orange and yellow gradients
- **Magic Element**: ✨ Quack-tastic Magic ✨

## 🚀 **Quick Start**

### **Install Dependencies:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **Start Mickey Mouse Agent:**
```bash
python app.py
```
Visit: http://localhost:5000

### **Start Donald Duck Agent:**
```bash
python donald_app.py
```
Visit: http://localhost:5001

### **Test Both Agents:**
```bash
python test_demo.py          # Test Mickey
python test_donald_demo.py   # Test Donald
```

## 🎭 **Features**

### **Both Agents Include:**
- 🎵 **Real Audio Playback** using Web Audio API
- 🎭 **Animated Visual Actions** with CSS animations
- 👋 **Enhanced Feedback** with emoji sequences
- 🎨 **Disney-Themed Styling** unique to each character
- 📱 **Responsive Design** for all devices
- 🔄 **Real-time Status Updates**

### **Mickey Mouse Unique Features:**
- Classic Disney songs (It's a Small World, When You Wish Upon a Star, etc.)
- Mickey-specific dance moves (The Mickey Shuffle, The Hot Dog Dance, etc.)
- Magical, friendly personality
- Red and purple color scheme
- "Disney magic in the air! ✨" messaging

### **Donald Duck Unique Features:**
- Donald-themed songs (Quack Quack Quack, Donald's Theme Song, etc.)
- Duck-specific dance moves (The Donald Shuffle, The Quack Attack, etc.)
- Energetic, feisty personality
- Orange and yellow color scheme
- "Quack-tastic performance! 👏" messaging

## 🎨 **Visual Experience**

### **Mickey Mouse Styling:**
- Purple to blue gradient backgrounds
- Red and purple button gradients
- Mickey Mouse emoji (🐭) avatar
- "✨ Disney Magic ✨" sparkle effects
- Mickey-specific CSS animations

### **Donald Duck Styling:**
- Orange to yellow gradient backgrounds
- Orange and yellow button gradients
- Donald Duck emoji (🦆) avatar
- "✨ Quack-tastic Magic ✨" sparkle effects
- Donald-specific CSS animations

## 🎯 **Independent Operation**

### **Key Benefits:**
- **Separate Processes**: Each agent runs independently
- **Different Ports**: No conflicts between agents
- **Unique Styling**: Completely different visual themes
- **Individual Status**: Each maintains its own state
- **Independent Actions**: Can perform simultaneously

## 📋 **API Endpoints**

Both agents have identical API endpoints but operate independently:

| Endpoint | Mickey (Port 5000) | Donald (Port 5001) |
|----------|-------------------|-------------------|
| Status | `GET /api/status` | `GET /api/status` |
| Sing | `POST /api/sing` | `POST /api/sing` |
| Wave | `POST /api/wave` | `POST /api/wave` |
| Dance | `POST /api/dance` | `POST /api/dance` |
| Show | `POST /api/show` | `POST /api/show` |
| Rest | `POST /api/rest` | `POST /api/rest` |

## 🎭 **Animation System**

### **Mickey Mouse Animations:**
- **Bounce**: Default idle animation
- **Mickey-Sing**: Scale and rotate with dynamic shadows
- **Mickey-Wave**: Side-to-side rotation with scaling
- **Mickey-Dance**: Jump and spin with multiple keyframes
- **Mickey-Rest**: Gentle pulse and fade
- **Mickey-Show**: Special show-time animation

### **Donald Duck Animations:**
- **Quack-Bounce**: Default idle animation
- **Donald-Sing**: Scale and rotate with dynamic shadows
- **Donald-Wave**: Side-to-side rotation with scaling
- **Donald-Dance**: Jump and spin with multiple keyframes
- **Donald-Rest**: Gentle pulse and fade
- **Donald-Show**: Special show-time animation

## 🧪 **Testing**

### **Test Mickey Mouse:**
```bash
python test_demo.py
```

### **Test Donald Duck:**
```bash
python test_donald_demo.py
```

### **Manual Testing:**
```bash
# Test Mickey
curl -X POST http://localhost:5000/api/sing \
  -H "Content-Type: application/json" \
  -d '{"song_name": "It'\''s a Small World"}'

# Test Donald
curl -X POST http://localhost:5001/api/sing \
  -H "Content-Type: application/json" \
  -d '{"song_name": "Quack Quack Quack"}'
```

## 🎉 **Experience the Magic**

1. **Start both agents** in separate terminals
2. **Open both URLs** in your browser
3. **Compare their personalities** and animations
4. **Enjoy the unique experience** of each character
5. **Test all features** with their individual styling

## 📁 **Project Structure**

```
├── app.py                 # Mickey Mouse Flask app (port 5000)
├── donald_app.py          # Donald Duck Flask app (port 5001)
├── mickey_mouse_agent.py  # Mickey Mouse agent class
├── donald_duck_agent.py   # Donald Duck agent class
├── templates/
│   ├── index.html         # Mickey Mouse UI
│   └── donald_index.html  # Donald Duck UI
├── test_demo.py           # Mickey Mouse test script
├── test_donald_demo.py    # Donald Duck test script
└── requirements.txt       # Python dependencies
```

## 🌟 **Future Enhancements**

- **More Disney Characters**: Goofy, Pluto, Minnie, Daisy
- **Collaborative Shows**: Multiple agents performing together
- **Character Interactions**: Agents responding to each other
- **Advanced Animations**: More complex visual effects
- **Voice Synthesis**: Character-specific voices

---

**🎭 Experience the Magic of Two Independent Disney Agents! ✨🌟**

*Mickey Mouse and Donald Duck - Each with their own unique personality and style!*