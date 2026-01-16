import tkinter as tk
from tkinter import messagebox
import time
import winsound  # Standard for Windows chimes/alarms

# --- ROYAL THEME CONFIG ---
WIDTH, HEIGHT = 800, 550
BG_COLOR = "#000000"     # Pure Black
GOLD_COLOR = "#D4AF37"   # Royal Metallic Gold
DARK_GOLD = "#5C4B1C"

class RoyalWatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Royal Digital Onyx Multi-Watch")
        self.root.configure(bg=BG_COLOR)
        
        # Variables
        self.last_chime_hour = -1
        self.stopwatch_running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.alarm_time = None  # Format: "HH:MM"
        
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR, highlightthickness=0)
        self.canvas.pack(pady=10)
        
        # UI Control Frame
        self.ui_frame = tk.Frame(root, bg=BG_COLOR)
        self.ui_frame.pack(pady=10)
        
        # Stopwatch Controls
        self.create_button(self.ui_frame, "START/STOP", self.toggle_stopwatch)
        self.create_button(self.ui_frame, "RESET SW", self.reset_stopwatch)
        
        # Alarm Input
        self.alarm_label = tk.Label(self.ui_frame, text="SET ALARM (HH:MM):", fg=GOLD_COLOR, bg=BG_COLOR, font=("Arial", 10, "bold"))
        self.alarm_label.pack(side="left", padx=5)
        
        self.alarm_entry = tk.Entry(self.ui_frame, width=8, bg="#1A1A1A", fg=GOLD_COLOR, insertbackground=GOLD_COLOR, font=("Arial", 12))
        self.alarm_entry.pack(side="left", padx=5)
        
        self.create_button(self.ui_frame, "SET ALARM", self.set_alarm)
        
        self.update_all()

    def create_button(self, frame, text, command):
        btn = tk.Button(frame, text=text, command=command, 
                        fg=GOLD_COLOR, bg=BG_COLOR, font=("Arial", 9, "bold"),
                        activebackground=GOLD_COLOR, activeforeground=BG_COLOR,
                        relief="flat", highlightbackground=GOLD_COLOR, highlightthickness=1)
        btn.pack(side="left", padx=5)

    def set_alarm(self):
        entry_val = self.alarm_entry.get()
        try:
            # Validate format HH:MM
            time.strptime(entry_val, "%H:%M")
            self.alarm_time = entry_val
            messagebox.showinfo("Royal Watch", f"Alarm set for {self.alarm_time}")
        except ValueError:
            messagebox.showerror("Error", "Use HH:MM format (e.g., 08:30)")

    def trigger_alarm(self):
        # Play a sequence of beeps for the alarm
        for _ in range(5):
            winsound.Beep(1500, 500)
            time.sleep(0.1)
        messagebox.showinfo("ALARM", f"It is {self.alarm_time}! Your Royal Alarm is ringing.")
        self.alarm_time = None # Reset alarm after it rings

    def play_hourly_chime(self):
        winsound.Beep(800, 400) # Elegant low beep for the hour

    def toggle_stopwatch(self):
        if not self.stopwatch_running:
            self.start_time = time.time() - self.elapsed_time
            self.stopwatch_running = True
        else:
            self.stopwatch_running = False

    def reset_stopwatch(self):
        self.stopwatch_running = False
        self.elapsed_time = 0

    def update_all(self):
        self.canvas.delete("all")
        
        now_struct = time.localtime()
        current_time = time.strftime("%H:%M:%S")
        current_hm = time.strftime("%H:%M")
        current_date = time.strftime("%A • %B %d, %Y").upper()
        
        # --- LOGIC: ALARM & CHIME ---
        if self.alarm_time == current_hm and now_struct.tm_sec == 0:
            self.trigger_alarm()

        if now_struct.tm_min == 0 and now_struct.tm_sec == 0 and now_struct.tm_hour != self.last_chime_hour:
            self.play_hourly_chime()
            self.last_chime_hour = now_struct.tm_hour

        # --- DRAWING ---
        # Glass Border
        self.canvas.create_rectangle(40, 20, WIDTH-40, HEIGHT-20, outline=GOLD_COLOR, width=3)
        
        # Main Clock
        self.canvas.create_text(WIDTH/2, 180, text=current_time, fill=GOLD_COLOR, 
                                font=("Times New Roman", 110, "bold"))
        
        # Date Display
        self.canvas.create_text(WIDTH/2, 70, text=current_date, fill=GOLD_COLOR, 
                                font=("Times New Roman", 16, "bold"))

        # Stopwatch Display
        if self.stopwatch_running:
            self.elapsed_time = time.time() - self.start_time
        
        mins, secs = divmod(int(self.elapsed_time), 60)
        milli = int((self.elapsed_time % 1) * 100)
        self.canvas.create_text(WIDTH/2, 360, text=f"STOPWATCH: {mins:02}:{secs:02}.{milli:02}", 
                                fill=GOLD_COLOR, font=("Courier New", 24, "bold"))

        # Alarm Status
        status = f"ALARM: {self.alarm_time}" if self.alarm_time else "ALARM: OFF"
        self.canvas.create_text(WIDTH/2, 450, text=status, fill=DARK_GOLD, font=("Arial", 14, "italic"))

        self.root.after(50, self.update_all)

# Execution
root = tk.Tk()
app = RoyalWatch(root)
root.mainloop()