import tkinter as tk
from PIL import Image, ImageTk
from utils.loader import (
    get_random_affirmation,
    get_emergency_message,
    get_random_love_note,
    get_proof_item
)

class AnchorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Nolan’s Safe Space")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.show_welcome_screen()

    def show_welcome_screen(self):
        self.welcome_frame = tk.Frame(self.root, width=800, height=600)
        self.welcome_frame.pack_propagate(False)
        self.welcome_frame.pack()

        try:
            bg = Image.open("assets/welcome_bg.png").resize((800, 600))
            self.welcome_bg = ImageTk.PhotoImage(bg)
            canvas = tk.Canvas(self.welcome_frame, width=800, height=600)
            canvas.pack()
            canvas.create_image(0, 0, anchor="nw", image=self.welcome_bg)
        except:
            canvas = tk.Canvas(self.welcome_frame, width=800, height=600, bg="#F8F6F3")
            canvas.pack()

        welcome_text = (
            "Welcome to your safe space.\n\n"
            "Take a moment to breathe.\n\n"
            "Sophie made this for you — for the tough moments.\n"
            "Because she loves you and wants to be here, even when she can't be.\n\n"
            "You are enough.\n"
            "You are so much more than you can see right now.\n"
            "You are so loved."
        )

        msg_label = tk.Label(
            canvas,
            text=welcome_text,
            bg="#FFFFFF",
            fg="#000000",
            font=("Georgia", 14),
            wraplength=680,
            justify="center",
            padx=20,
            pady=20,
            relief="ridge",
            bd=2
        )
        canvas.create_window(400, 200, window=msg_label)

        enter_btn = tk.Button(self.root, text="🧭 Enter Your Trail", font=("Georgia", 12, "bold"),
                              bg="#2E3B28", fg="#FFFFFF", activebackground="#3F5540",
                              relief="raised", padx=20, pady=10, command=self.load_trail_map)
        canvas.create_window(400, 420, window=enter_btn)

    def load_trail_map(self):
        self.welcome_frame.destroy()

        bg_image = Image.open("assets/topo_map.png").resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="#000000", highlightthickness=0)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)

        self.trail_points = []

        self.message = tk.StringVar()
        self.message.set("Welcome to Nolan’s Safe Space 🧭\nChoose your next trail post.")
        message_box = tk.Label(
            self.root,
            textvariable=self.message,
            wraplength=740,
            bg="#1A1A1A",
            fg="#EAEAEA",
            font=("Georgia", 12),
            justify="center",
            padx=20,
            pady=15,
            relief="ridge",
            bd=2
        )
        self.canvas.create_window(400, 545, window=message_box)

        # ✅ Properly indented trail markers with emojis
        self.add_trail_marker("💪 Boost Me", self.boost, 120, 480)
        self.add_trail_marker("🏕️ Emergency Shelter", self.emergency, 240, 400)
        self.add_trail_marker("📜 Mark Wins", self.proof, 380, 310)
        self.add_trail_marker("💌 Love Letters from Sophie", self.love_letter, 520, 240)
        self.add_trail_marker("📸 Our Moments", self.our_moments, 660, 180)
        self.add_trail_marker("🚰 Water & Rest", self.water_me, 760, 140)

        # Connect trail posts with dotted line
        coords = []
        for pt in self.trail_points:
            coords.extend(pt)
        self.canvas.create_line(*coords, width=3, fill="#6E9E6A", dash=(6, 4), smooth=True)

    def add_trail_marker(self, label, command, x, y):
        self.trail_points.append((x, y))

        frame = tk.Frame(self.root, bg="", bd=0)

        tk.Label(
            frame,
            text=label,
            font=("Georgia", 10, "bold"),
            fg="#2E3B28",
            bg="#F8F6F3",
            wraplength=100,
            justify="center"
        ).pack()

        tk.Button(
            frame,
            text="Open",
            command=command,
            font=("Georgia", 9),
            bg="#2E3B28",
            fg="#FFFFFF",
            activebackground="#3F5540",
            bd=0
        ).pack(pady=2)

        self.canvas.create_window(x, y, window=frame)

    def boost(self):
        self.message.set("🧠 Trail Post: Boost Me\n\n" + get_random_affirmation())

    def emergency(self):
        self.message.set("❤️ Trail Post: Emergency Shelter\n\n" + get_emergency_message())

    def proof(self):
        self.message.set("📜 Trail Post: Mark Wins\n\n" + get_proof_item())

    def love_letter(self):
        try:
            self.message.set("💌 Trail Post: Love Letters from Sophie\n\n" + get_random_love_note())
        except FileNotFoundError:
            self.message.set("💌 Trail Post: Love Letters from Sophie\n\n(Sophie hasn't added letters yet!)")

    def our_moments(self):
        self.message.set("📸 Trail Post: Our Moments\n\n" +
            "• That hike where we got lost but kept laughing\n"
            "• The night we stayed up talking with no lights\n"
            "• Your birthday surprise\n"
            "• The first time you said you felt safe with me\n"
            "• Every time you look at me like I’m home\n\n"
            "We’ve built something beautiful here, and we’re still on the trail.")

    def water_me(self):
        self.message.set("🚰 Trail Post: Water & Rest\n\nYou don’t have to summit today, Nolan.\n"
                         "Take your water, breathe deep, and rest.\nYou’re still on your path.")

    def run(self):
        self.root.mainloop()
