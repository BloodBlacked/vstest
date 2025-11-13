import tkinter as tk
from tkinter import scrolledtext
import os
import json
import webbrowser

# -------------------------------
# Bot Knowledge Base (from JSON)
# -------------------------------
def load_bot_knowledge():
    """Load chatbot knowledge from JSON file with error handling."""
    try:
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_file = os.path.join(script_dir, "chatbot_data.json")
        
        if not os.path.exists(json_file):
            print(f"⚠️ Warning: {json_file} not found. Using minimal fallback data.")
            return {
                "initial_greeting": "Hello! I'm StudyMate AI.",
                "fallback": "Sorry, I couldn't understand that.",
                "greetings": ["hi", "hello", "hey"],
                "resources": "No resources available.",
                "subjects": {}
            }
        
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"✅ Successfully loaded {json_file}")
            return data
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON: {e}")
        return {
            "initial_greeting": "Hello! I'm StudyMate AI (data error).",
            "fallback": "Sorry, there was an error loading my knowledge base.",
            "greetings": ["hi", "hello"],
            "resources": "",
            "subjects": {}
        }
    except Exception as e:
        print(f"❌ Unexpected error loading data: {e}")
        return {
            "initial_greeting": "Hello! I'm StudyMate AI.",
            "fallback": "Sorry, I couldn't understand that.",
            "greetings": ["hi"],
            "resources": "",
            "subjects": {}
        }

# Load knowledge base at startup
BOT_KNOWLEDGE_OLD = {
  "initial_greeting": "Hello 👋! I’m your StudyMate AI.\nWhat subject do you want to study — Physics, Math, or Coding?",
  "fallback": "Hmm 🤔 I didn’t catch that.\nTry saying 'Mechanics', 'Calculus', or type 'resources' for links.",
  "greetings": [
    "hi",
    "hello",
    "hey"
  ],
  "resources": "Here are some great study resources 📚✨\n\n1️⃣ ATC First Year Study Hub:\nhttps://bento.me/atc-first-year\n\n2️⃣ 10CGPA Notes & Practice Platform:\nhttps://10cgpa.vercel.app\n\nBoth have organized notes and materials for B.Tech 1st year! 🚀",
  "subjects": {
    "physics": {
      "aliases": [],
      "greeting": "Great! Let's dive into Physics 🔬\nTopics: Mechanics, Thermodynamics, Optics, Waves, Electricity.",
      "topics": {
        "mechanics": {
          "description": "Mechanics ⚙️ — Study of motion and forces. (Formula: F = ma).",
          "link": "https://www.youtube.com/watch?v=-6IgkG5yZfo"
        },
        "thermo": {
          "description": "Thermodynamics 🔥 — Heat and energy relation. (Formula: ΔU = Q - W).",
          "link": "https://www.youtube.com/watch?v=yNK3x-vZ8hA"
        },
        "optic": {
          "description": "Optics 🔭 — Study of light. (Example: Snell’s Law n₁sinθ₁ = n₂sinθ₂).",
          "link": "https://www.youtube.com/watch?v=Oh4m8Ees-3Q"
        },
        "wave": {
          "description": "Waves 🌊 — Energy transfer through oscillations. (Formula: v = fλ).",
          "link": "https://www.youtube.com/watch?v=KWzyQKcJBYg"
        },
        "electric": {
          "description": "Electricity ⚡ — Flow of charge. (Formula: I = V/R).",
          "link": "https://www.youtube.com/watch?v=gl_WPHDmK8o"
        }
      }
    },
    "math": {
      "aliases": [
        "mathematics"
      ],
      "greeting": "Awesome! 📐 Math it is.\nTopics: Algebra, Calculus, Geometry, Probability, Trigonometry.",
      "topics": {
        "algebra": {
          "description": "Algebra ➕ — Equations and expressions using variables.",
          "link": "https://www.youtube.com/watch?v=i6sbjtJjJ-A"
        },
        "calculus": {
          "description": "Calculus 📈 — Study of change. (Example: d/dx(x²)=2x).",
          "link": "https://www.youtube.com/playlist?list=PLF797E961509B4EB5"
        },
        "geometry": {
          "description": "Geometry 📐 — Shapes and areas. (Example: Area=½×base×height).",
          "link": "https://www.youtube.com/watch?v=302eJ3TzJQU"
        },
        "probability": {
          "description": "Probability 🎲 — P(E)=Favorable outcomes / Total outcomes.",
          "link": "https://www.youtube.com/watch?v=KzfWUEJjG18"
        },
        "trigo": {
          "description": "Trigonometry 📏 — (Example: sin²θ + cos²θ = 1).",
          "link": "https://www.youtube.com/watch?v=Jsiy4TxgIME"
        }
      }
    },
    "coding": {
      "aliases": [
        "python",
        "programming"
      ],
      "greeting": "Cool! 💻 Let's start coding.\nTopics: Python basics, DSA, OOP concepts.",
      "topics": {
        "python": {
          "description": "Python 🐍 — A high-level programming language. (Example: print('Hello, World!')).",
          "link": "https://www.youtube.com/watch?v=rfscVS0vtbw"
        },
        "dsa": {
          "description": "DSA 📚 — Data structures and algorithms for efficient problem solving.",
          "link": "https://www.youtube.com/playlist?list=PLfqMhTWNBTe137I_EPQd34TsgV6IO55pt"
        },
        "oop": {
          "description": "OOP ☕ — Object-Oriented Programming, a paradigm using classes and objects.",
          "link": "https://www.youtube.com/watch?v=HeW-D6KpDwY"
        }
      }
    }
  }
}

# Now load from JSON file (this will override the fallback above if JSON exists)
BOT_KNOWLEDGE = load_bot_knowledge()

# -------------------------------
# Save & Load Chat Automatically
# -------------------------------
CHAT_HISTORY_FILE = "chat_history.txt"

def save_chat_history():
    with open(CHAT_HISTORY_FILE, "w", encoding="utf-8") as f:
        f.write(chat_box.get("1.0", tk.END))

def load_chat_history():
    if os.path.exists(CHAT_HISTORY_FILE):
        with open(CHAT_HISTORY_FILE, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def clear_chat_history():
    """Clear the chat history from the UI and the file."""
    chat_box.config(state=tk.NORMAL)
    chat_box.delete("1.0", tk.END)
    # Re-insert initial greeting
    chat_box.insert(tk.END, f"🤖 StudyMate: {BOT_KNOWLEDGE.get('initial_greeting', 'Hello!')}\n", "bot")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)
    # Clear the history file
    if os.path.exists(CHAT_HISTORY_FILE):
        os.remove(CHAT_HISTORY_FILE)
    # Reset subject context
    global current_subject
    current_subject = ""
    # Save the new greeting to a fresh history file
    save_chat_history()

def export_chat_to_file():
    """Export current chat to a timestamped text file."""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"StudyMate_Chat_{timestamp}.txt"
    
    # Get the script directory to save in the same location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(chat_box.get("1.0", tk.END))
        
        # Show success message in chat
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, f"\n✅ Chat saved to: {filename}\n", "system")
        chat_box.config(state=tk.DISABLED)
        chat_box.yview(tk.END)
        save_chat_history()
    except Exception as e:
        # Show error message in chat
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, f"\n❌ Error saving chat: {str(e)}\n", "system")
        chat_box.config(state=tk.DISABLED)
        chat_box.yview(tk.END)

# -------------------------------
# Enhanced Chatbot Logic
# -------------------------------
current_subject = ""

def normalize_text(text):
    """Normalize text for better matching."""
    return text.lower().strip()

def find_partial_match(user_text, keywords):
    """Check if any keyword is contained in user text."""
    user_text = normalize_text(user_text)
    for keyword in keywords:
        if normalize_text(keyword) in user_text:
            return True
    return False

def get_bot_response(user_input):
    global current_subject
    text = normalize_text(user_input)

    # Check for greetings
    greetings = BOT_KNOWLEDGE.get("greetings", [])
    if any(normalize_text(word) in text for word in greetings):
        current_subject = ""  # Reset subject on greeting
        return BOT_KNOWLEDGE.get("initial_greeting", "Hello! What subject do you want to study?")

    # Check for resource request
    resource_keywords = ["resource", "resources", "link", "links", "note", "notes", "material", "materials", "study", "hub", "platform"]
    if find_partial_match(text, resource_keywords):
        return BOT_KNOWLEDGE.get("resources", "Sorry, I don't have any resources available.")

    # If a subject is already selected, prioritize checking for topics first
    if current_subject:
        subjects = BOT_KNOWLEDGE.get("subjects", {})
        subject_data = subjects.get(current_subject, {})
        topics = subject_data.get("topics", {})
        
        # Check each topic
        for topic_key, topic_data in topics.items():
            # Check if topic name is in user text (partial match)
            if normalize_text(topic_key) in text:
                description = topic_data.get("description", "No description available.")
                link = topic_data.get("link", "")
                
                if link:
                    return f"{description}\n\nHere's a great video/playlist: {link}"
                else:
                    return description
        
        # If no specific topic found, prompt user with available topics
        topic_list = ", ".join([t.title() for t in topics.keys()])
        if topic_list:
            return f"I didn't catch which topic you want. Try asking about: {topic_list}"
        else:
            return subject_data.get("greeting", f"What about {current_subject.title()} would you like to know?")

    # Check for subject selection (only if no subject is currently active)
    subjects = BOT_KNOWLEDGE.get("subjects", {})
    for subject_key, subject_data in subjects.items():
        # Check if subject name matches
        if normalize_text(subject_key) in text:
            current_subject = subject_key
            return subject_data.get("greeting", f"Great! Let's study {subject_key.title()}.")
        
        # Check aliases
        aliases = subject_data.get("aliases", [])
        for alias in aliases:
            if normalize_text(alias) in text:
                current_subject = subject_key
                return subject_data.get("greeting", f"Great! Let's study {subject_key.title()}.")

    # Fallback: suggest available subjects
    subject_names = ", ".join([s.title() for s in subjects.keys()])
    if subject_names:
        fallback_with_hint = BOT_KNOWLEDGE.get("fallback", "I'm not sure how to help with that.")
        return f"{fallback_with_hint}\n\nAvailable subjects: {subject_names}"
    else:
        return BOT_KNOWLEDGE.get("fallback", "I'm not sure how to help with that.")

# -------------------------------
# Tkinter Dark UI Setup
# -------------------------------
root = tk.Tk()
root.title("StudyMate AI")
root.geometry("700x600")
root.configure(bg="#0f1116")

# Header Frame (contains title and buttons)
header_frame = tk.Frame(root, bg="#16181d")
header_frame.pack(fill="x")

# Title
header = tk.Label(header_frame, text="🧠 StudyMate AI", font=("Poppins", 18, "bold"),
                  bg="#16181d", fg="#3b82f6", pady=10)
header.pack(side="left", padx=10)

# Button container (right side)
button_container = tk.Frame(header_frame, bg="#16181d")
button_container.pack(side="right", padx=10, pady=10)

# Save Chat button
save_chat_btn = tk.Button(button_container, text="💾 Save Chat", command=export_chat_to_file,
                          bg="#10b981", fg="white", font=("Poppins", 10, "bold"),
                          relief="flat", activebackground="#059669", activeforeground="white",
                          padx=12, pady=6, cursor="hand2")
save_chat_btn.pack(side="left", padx=5)

# Clear Chat button
clear_chat_btn = tk.Button(button_container, text="🗑️ Clear Chat", command=clear_chat_history,
                           bg="#ef4444", fg="white", font=("Poppins", 10, "bold"),
                           relief="flat", activebackground="#dc2626", activeforeground="white",
                           padx=12, pady=6, cursor="hand2")
clear_chat_btn.pack(side="left", padx=5)

# Chat area
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Poppins", 12),
                                     bg="#1a1c22", fg="#e5e7eb", insertbackground="white",
                                     borderwidth=0, highlightthickness=0)
chat_box.pack(padx=10, pady=10, fill="both", expand=True)

# Load history and insert it
initial_history = load_chat_history()
if initial_history:
    chat_box.insert(tk.END, initial_history)
else:
    # Greet user only if there's no history
    chat_box.insert(tk.END, f"🤖 StudyMate: {BOT_KNOWLEDGE.get('initial_greeting', 'Hello!')}\n", "bot")

chat_box.config(state=tk.DISABLED)
chat_box.yview(tk.END) # Ensure it starts scrolled to the bottom

# Input area
input_frame = tk.Frame(root, bg="#16181d")
input_frame.pack(fill="x", padx=10, pady=10)

user_input = tk.Entry(input_frame, font=("Poppins", 12), bg="#1a1c22",
                      fg="white", insertbackground="white", relief="flat")
user_input.pack(side="left", fill="x", expand=True, padx=(0, 10), ipady=8)

def send_message(event=None):
    user_msg = user_input.get().strip()
    if not user_msg:
        return

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"\n🧑 You: {user_msg}\n", "user")
    
    # Get response and add it
    bot_response = get_bot_response(user_msg)
    chat_box.insert(tk.END, f"🤖 StudyMate: ", "bot")  # Insert prefix
    
    # Check for links in the response to make them clickable
    if "https://" in bot_response or "http://" in bot_response:
        # Split by both http and https
        parts = bot_response.replace("https://", "|||https://").replace("http://", "|||http://").split("|||")
        
        for part in parts:
            if part.startswith("http://") or part.startswith("https://"):
                # Find end of URL (space, newline, or tab)
                url_end = len(part)
                for char in ['\n', ' ', '\t']:
                    found_end = part.find(char)
                    if found_end != -1 and found_end < url_end:
                        url_end = found_end
                
                url = part[:url_end]
                rest_of_text = part[url_end:]
                
                # Insert the URL with a clickable tag
                tag_name = f"link_{abs(hash(url))}"  # Unique tag for each link
                chat_box.insert(tk.END, url, ("link", tag_name))
                chat_box.tag_config(tag_name, foreground="#60a5fa", underline=True)
                # Use a lambda to capture the current URL for the binding
                chat_box.tag_bind(tag_name, "<Button-1>", lambda e, h_url=url: webbrowser.open_new(h_url))
                chat_box.tag_bind(tag_name, "<Enter>", lambda e: chat_box.config(cursor="hand2"))
                chat_box.tag_bind(tag_name, "<Leave>", lambda e: chat_box.config(cursor=""))
                
                chat_box.insert(tk.END, rest_of_text)  # Insert text after the link
            else:
                # Not a URL, just insert normally
                chat_box.insert(tk.END, part)
        
        chat_box.insert(tk.END, "\n")  # Add newline at the end
    else:
        # No links, just insert the response normally
        chat_box.insert(tk.END, f"{bot_response}\n", "bot_text_only")

    
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)
    user_input.delete(0, tk.END)
    save_chat_history()

# Styling tags for user and bot messages
chat_box.tag_config("user", foreground="#3b82f6", font=("Poppins", 12, "bold"))
chat_box.tag_config("bot", foreground="#e5e7eb", font=("Poppins", 12))
chat_box.tag_config("bot_text_only", foreground="#e5e7eb", font=("Poppins", 12)) # For non-link bot text
chat_box.tag_config("link", foreground="#60a5fa", underline=True) # General link style
chat_box.tag_config("system", foreground="#10b981", font=("Poppins", 11, "italic")) # System messages

# Send button
send_btn = tk.Button(input_frame, text="Send", command=send_message,
                     bg="#3b82f6", fg="white", font=("Poppins", 12, "bold"),
                     relief="flat", activebackground="#2563eb", activeforeground="white", padx=15)
send_btn.pack(side="right")

# Bind Enter key
user_input.bind("<Return>", send_message)

# Auto-save when window closes
def on_close():
    save_chat_history()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()