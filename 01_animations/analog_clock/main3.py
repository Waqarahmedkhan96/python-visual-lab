import tkinter as tk
import time
import math

# --- ROYAL THEME CONFIG ---
WIDTH = 600
HEIGHT = 600
BG_COLOR = "#000000"     # Pure Black Shiny
GOLD_COLOR = "#D4AF37"   # Royal Metallic Gold
TICK_COLOR = "#8B7355"   # Muted Bronze for small ticks

root = tk.Tk()
root.title("Royal Gold Clock")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR, highlightthickness=0)
canvas.pack()

def update_clock():
    canvas.delete("all")
    
    curr_time = time.time()
    local_t = time.localtime(curr_time)
    
    # Calculate smooth sweeping values
    ms = curr_time % 1
    second = local_t.tm_sec + ms
    minute = local_t.tm_min + (second / 60)
    hour = (local_t.tm_hour % 12) + (minute / 60)

    center_x, center_y = WIDTH / 2, HEIGHT / 2
    radius = WIDTH * 0.42

    # 1. Outer Shiny Gold Ring
    canvas.create_oval(center_x - radius, center_y - radius, 
                       center_x + radius, center_y + radius, 
                       outline=GOLD_COLOR, width=4)

    # 2. Draw Numbers and Ticks
    for i in range(60):
        angle = i * math.pi/30 - math.pi/2
        
        if i % 5 == 0:
            # Drawing Numbers (1, 2, 3...)
            num = i // 5
            if num == 0: num = 12
            
            # Position numbers slightly inside the rim
            nx = center_x + (radius * 0.8) * math.cos(angle)
            ny = center_y + (radius * 0.8) * math.sin(angle)
            
            canvas.create_text(nx, ny, text=str(num), fill=GOLD_COLOR, 
                               font=("Times New Roman", 24, "bold"))
            
            # Larger Gold Dots for Hours
            tx = center_x + (radius * 0.92) * math.cos(angle)
            ty = center_y + (radius * 0.92) * math.sin(angle)
            canvas.create_oval(tx-3, ty-3, tx+3, ty+3, fill=GOLD_COLOR, outline=GOLD_COLOR)
        else:
            # Small Ticks for seconds/minutes
            tx = center_x + (radius * 0.92) * math.cos(angle)
            ty = center_y + (radius * 0.92) * math.sin(angle)
            canvas.create_oval(tx-1, ty-1, tx+1, ty+1, fill=TICK_COLOR, outline=TICK_COLOR)

    # 3. Royal Hour Hand
    h_angle = hour * math.pi/6 - math.pi/2
    hx = center_x + (radius * 0.5) * math.cos(h_angle)
    hy = center_y + (radius * 0.5) * math.sin(h_angle)
    canvas.create_line(center_x, center_y, hx, hy, fill=GOLD_COLOR, width=10, capstyle="round")

    # 4. Royal Minute Hand
    m_angle = minute * math.pi/30 - math.pi/2
    mx = center_x + (radius * 0.75) * math.cos(m_angle)
    my = center_y + (radius * 0.75) * math.sin(m_angle)
    canvas.create_line(center_x, center_y, mx, my, fill=GOLD_COLOR, width=6, capstyle="round")

    # 5. Slim Gold Second Hand
    s_angle = second * math.pi/30 - math.pi/2
    sx = center_x + (radius * 0.85) * math.cos(s_angle)
    sy = center_y + (radius * 0.85) * math.sin(s_angle)
    canvas.create_line(center_x, center_y, sx, sy, fill=GOLD_COLOR, width=2)
    
    # Elegant Center Cap
    canvas.create_oval(center_x-8, center_y-8, center_x+8, center_y+8, fill=GOLD_COLOR, outline=BG_COLOR, width=2)

    canvas.after(50, update_clock)

update_clock()
root.mainloop()