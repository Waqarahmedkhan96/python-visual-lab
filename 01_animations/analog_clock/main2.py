import tkinter as tk
import time
import math

# --- MODERN THEME CONFIG ---
WIDTH = 500
HEIGHT = 500
BG_COLOR = "#121212"    # Deep Charcoal
ACCENT_COLOR = "#00ADB5" # Teal Neon
HOUR_COLOR = "#EEEEEE"   # Soft White
TEXT_COLOR = "#393E46"   # Muted Gray

root = tk.Tk()
root.title("Modern Analog Clock")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR, highlightthickness=0)
canvas.pack()

def update_clock():
    canvas.delete("all")
    
    # Get high-precision time for smooth sweeping
    curr_time = time.time()
    local_t = time.localtime(curr_time)
    
    # Calculate fractional units for smoothness
    ms = curr_time % 1
    second = local_t.tm_sec + ms
    minute = local_t.tm_min + (second / 60)
    hour = (local_t.tm_hour % 12) + (minute / 60)

    center_x, center_y = WIDTH / 2, HEIGHT / 2
    radius = WIDTH * 0.4

    # 1. Draw Subtle Outer Ring
    canvas.create_oval(center_x - radius, center_y - radius, 
                       center_x + radius, center_y + radius, 
                       outline=TEXT_COLOR, width=1)

    # 2. Draw Modern Ticks (Dots instead of lines)
    for i in range(60):
        angle = i * math.pi/30 - math.pi/2
        dot_radius = 1 if i % 5 != 0 else 3
        color = ACCENT_COLOR if i % 5 == 0 else TEXT_COLOR
        
        tx = center_x + (radius * 0.9) * math.cos(angle)
        ty = center_y + (radius * 0.9) * math.sin(angle)
        
        canvas.create_oval(tx-dot_radius, ty-dot_radius, tx+dot_radius, ty+dot_radius, 
                           fill=color, outline=color)

    # 3. Hour Hand (Thick & Short)
    h_angle = hour * math.pi/6 - math.pi/2
    hx = center_x + (radius * 0.5) * math.cos(h_angle)
    hy = center_y + (radius * 0.5) * math.sin(h_angle)
    canvas.create_line(center_x, center_y, hx, hy, fill=HOUR_COLOR, width=8, capstyle="round")

    # 4. Minute Hand (Slim & Long)
    m_angle = minute * math.pi/30 - math.pi/2
    mx = center_x + (radius * 0.8) * math.cos(m_angle)
    my = center_y + (radius * 0.8) * math.sin(m_angle)
    canvas.create_line(center_x, center_y, mx, my, fill=HOUR_COLOR, width=4, capstyle="round")

    # 5. Second Hand (Neon Accent)
    s_angle = second * math.pi/30 - math.pi/2
    sx = center_x + (radius * 0.85) * math.cos(s_angle)
    sy = center_y + (radius * 0.85) * math.sin(s_angle)
    canvas.create_line(center_x, center_y, sx, sy, fill=ACCENT_COLOR, width=2)
    
    # Center Pin
    canvas.create_oval(center_x-5, center_y-5, center_x+5, center_y+5, fill=BG_COLOR, outline=ACCENT_COLOR, width=2)

    # Update frequently (50ms) for smooth "sweep" movement
    canvas.after(50, update_clock)

update_clock()
root.mainloop()