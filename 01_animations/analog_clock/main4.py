import tkinter as tk
import time
import math

# --- ROYAL THEME CONFIG ---
WIDTH = 600
HEIGHT = 600
BG_COLOR = "#000000"     # Pure "Shiny" Black
GOLD_COLOR = "#D4AF37"   # Royal Metallic Gold
SHADOW_GOLD = "#8B7355"  # Muted Gold for ticks

root = tk.Tk()
root.title("Royal Gold Clock")
# Setting highlightthickness to 0 removes the border around the canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR, highlightthickness=0)
canvas.pack()

def update_clock():
    canvas.delete("all")
    
    # Get high-precision time for smooth sweeping hands
    curr_time = time.time()
    local_t = time.localtime(curr_time)
    
    # Calculate fractional units so the second hand moves smoothly
    ms = curr_time % 1
    second = local_t.tm_sec + ms
    minute = local_t.tm_min + (second / 60)
    hour = (local_t.tm_hour % 12) + (minute / 60)

    center_x, center_y = WIDTH / 2, HEIGHT / 2
    radius = WIDTH * 0.44

    # 1. Outer Shiny Gold Ring (The Frame)
    canvas.create_oval(center_x - radius, center_y - radius, 
                       center_x + radius, center_y + radius, 
                       outline=GOLD_COLOR, width=5)

    # 2. Draw Numbers and Tick Marks
    for i in range(60):
        # We subtract pi/2 because math.sin/cos starts at 3 o'clock
        angle = i * math.pi/30 - math.pi/2
        
        if i % 5 == 0:
            # Drawing the Gold Numbers (1-12)
            num = i // 5
            if num == 0: num = 12
            
            # Position numbers slightly inside the rim
            nx = center_x + (radius * 0.78) * math.cos(angle)
            ny = center_y + (radius * 0.78) * math.sin(angle)
            
            # Using Times New Roman to match the high-end font in the image
            canvas.create_text(nx, ny, text=str(num), fill=GOLD_COLOR, 
                               font=("Times New Roman", 28, "bold"))
            
            # Larger Gold Dots at every Hour
            tx = center_x + (radius * 0.92) * math.cos(angle)
            ty = center_y + (radius * 0.92) * math.sin(angle)
            canvas.create_oval(tx-4, ty-4, tx+4, ty+4, fill=GOLD_COLOR, outline=GOLD_COLOR)
        else:
            # Small Gold Dots for the seconds/minutes ticks
            tx = center_x + (radius * 0.92) * math.cos(angle)
            ty = center_y + (radius * 0.92) * math.sin(angle)
            canvas.create_oval(tx-1, ty-1, tx+1, ty+1, fill=SHADOW_GOLD, outline=SHADOW_GOLD)

    # 3. Royal Hour Hand (Short & Thick)
    h_angle = hour * math.pi/6 - math.pi/2
    hx = center_x + (radius * 0.5) * math.cos(h_angle)
    hy = center_y + (radius * 0.5) * math.sin(h_angle)
    canvas.create_line(center_x, center_y, hx, hy, fill=GOLD_COLOR, width=12, capstyle="round")

    # 4. Royal Minute Hand (Long & Medium Thick)
    m_angle = minute * math.pi/30 - math.pi/2
    mx = center_x + (radius * 0.8) * math.cos(m_angle)
    my = center_y + (radius * 0.8) * math.sin(m_angle)
    canvas.create_line(center_x, center_y, mx, my, fill=GOLD_COLOR, width=7, capstyle="round")

    # 5. Slim Gold Second Hand (Sweeping)
    s_angle = second * math.pi/30 - math.pi/2
    sx = center_x + (radius * 0.88) * math.cos(s_angle)
    sy = center_y + (radius * 0.88) * math.sin(s_angle)
    canvas.create_line(center_x, center_y, sx, sy, fill=GOLD_COLOR, width=2)
    
    # 6. Center Pin (Cap)
    canvas.create_oval(center_x-8, center_y-8, center_x+8, center_y+8, fill=GOLD_COLOR, outline=BG_COLOR, width=2)

    # Update every 50ms for that smooth movement
    canvas.after(50, update_clock)

# Start the clock loop
update_clock()
root.mainloop()