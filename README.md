# 🧠 StudyMate AI Chatbot

An intelligent study assistant chatbot with a modern dark UI, built with Python and Tkinter.

## ✨ Features

### 🤖 Smart Responses
- **JSON-driven knowledge base**: All chatbot data loaded from `chatbot_data.json`
- **Context-aware conversations**: Remembers the current subject during conversation
- **Intelligent matching**: Handles subject aliases (e.g., "mathematics" → "math")
- **Topic suggestions**: Prompts users with available topics when unclear
- **Clickable links**: YouTube video/playlist links are clickable in the chat

### 💬 Chat Management
- **Auto-save**: Conversation automatically saved to `chat_history.txt`
- **Clear Chat** 🗑️: Delete conversation history and start fresh
- **Save Chat** 💾: Export conversation to timestamped text file (`StudyMate_Chat_YYYYMMDD_HHMMSS.txt`)
- **Persistent history**: Chat history loads automatically on restart

### 🎨 Modern Dark UI
- Clean, professional dark theme
- Blue accent colors for user messages
- Clickable links with hover effects
- Smooth scrolling chat area
- Responsive design

## 📚 Available Subjects

### Physics 🔬
- Mechanics
- Thermodynamics
- Optics
- Waves
- Electricity

### Math 📐
- Algebra
- Calculus
- Geometry
- Probability
- Trigonometry

### Coding 💻
- Python basics
- Data Structures & Algorithms (DSA)
- Object-Oriented Programming (OOP)

## 🚀 How to Use

1. **Start the chatbot**:
   ```bash
   python chatbot.py
   ```

2. **Basic conversation flow**:
   - Say "hi" or "hello" to greet the bot
   - Choose a subject: "physics", "math", or "coding"
   - Ask about a topic: "mechanics", "calculus", "python", etc.
   - Type "resources" to get study material links

3. **Example conversation**:
   ```
   You: hi
   Bot: Hello 👋! I'm your StudyMate AI...
   
   You: physics
   Bot: Great! Let's dive into Physics 🔬...
   
   You: mechanics
   Bot: Mechanics ⚙️ — Study of motion and forces. (Formula: F = ma).
        Here's a great video/playlist: [YouTube link]
   
   You: resources
   Bot: Here are some great study resources 📚✨...
   ```

4. **Chat management**:
   - Click **💾 Save Chat** to export conversation to a file
   - Click **🗑️ Clear Chat** to delete history and start over

## 📁 File Structure

```
projectchatbot2.0/
├── chatbot.py              # Main application
├── chatbot_data.json       # Knowledge base (subjects, topics, links)
├── chat_history.txt        # Auto-saved conversation (created on first run)
├── StudyMate_Chat_*.txt    # Exported chat files (timestamped)
└── README.md               # This file
```

## 🛠️ Technical Details

### Dependencies
- Python 3.x
- `tkinter` (built-in)
- `json` (built-in)
- `os` (built-in)
- `webbrowser` (built-in)

### Key Functions
- `load_bot_knowledge()`: Loads chatbot data from JSON with error handling
- `get_bot_response()`: Processes user input and generates responses
- `normalize_text()`: Text preprocessing for better matching
- `find_partial_match()`: Flexible keyword detection
- `save_chat_history()`: Auto-saves conversation
- `clear_chat_history()`: Clears UI and deletes history file
- `export_chat_to_file()`: Exports chat with timestamp

### Customization
Edit `chatbot_data.json` to:
- Add new subjects
- Add new topics
- Update descriptions
- Change YouTube links
- Modify greetings and messages

## 🎯 Future Enhancements
- [ ] Search functionality within chat
- [ ] Multiple language support
- [ ] Voice input/output
- [ ] Quiz/practice mode
- [ ] Progress tracking
- [ ] Custom themes

## 📝 License
Free to use and modify for educational purposes.

---

**Made with ❤️ for students**
