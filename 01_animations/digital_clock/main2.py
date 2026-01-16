import tkinter as tk
import time

# --- ROYAL THEME CONFIG ---
WIDTH = 700
HEIGHT = 400
BG_COLOR = "#000000"     # Pure Black
GOLD_COLOR = "#D4AF37"   # Royal Metallic Gold

root = tk.Tk()
root.title("Royal Digital Watch")
root.configure(bg=BG_COLOR)

# Creating a canvas for the "Glass" effect
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR, highlightthickness=0)
canvas.pack(expand=True)

def update_watch():
    canvas.delete("all")
    
    # Get high-precision current time
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A • %B %d, %Y").upper()
    
    # 1. Draw Royal Border (The Frame)
    # This matches the outer gold ring of your analog clock
    canvas.create_rectangle(50, 50, WIDTH-50, HEIGHT-50, outline=GOLD_COLOR, width=3)
    
    # 2. Top Banner: Date
    # Letter spacing and serif fonts create a premium feel
    canvas.create_text(WIDTH/2, 100, text=current_date, fill=GOLD_COLOR, 
                       font=("Times New Roman", 16, "bold"))

    # 3. Main Display: Digital Time
    # Bold, elegant serif numbers
    canvas.create_text(WIDTH/2, HEIGHT/2 + 20, text=current_time, fill=GOLD_COLOR, 
                       font=("Times New Roman", 100, "bold"))

    # 4. Modern Detail: Subtle Reflection
    # Adds a "shine" line to make the black background look like glass
    canvas.create_line(70, 70, WIDTH-70, 70, fill=GOLD_COLOR, width=1)
    canvas.create_line(70, HEIGHT-70, WIDTH-70, HEIGHT-70, fill=GOLD_COLOR, width=1)
    
    # Refresh every 1 second
    canvas.after(1000, update_watch)

# Initialize
update_watch()
root.mainloop()