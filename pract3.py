import tkinter as tk
from tkinter import ttk
class SteamUI(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configure the main window
        self.title("Basic Steam-Like UI")
        self.geometry("800x600")
        self.configure(bg="#2b2b2b")  # Dark background
        # Create top bar
        self.create_top_bar()
        # Create sidebar and content area
        self.create_layout()
    def create_top_bar(self):
        top_frame = tk.Frame(self, bg="#1e1e1e", height=40)
        top_frame.pack(side="top", fill="x")
        # Add buttons to the top bar
        account_btn = tk.Button(top_frame, text="Account", bg="#3e3e3e", fg="white", relief="flat")
        store_btn = tk.Button(top_frame, text="Store", bg="#3e3e3e", fg="white", relief="flat")
        library_btn = tk.Button(top_frame, text="Library", bg="#3e3e3e", fg="white", relief="flat")
        account_btn.pack(side="left", padx=10)
        store_btn.pack(side="left", padx=10)
        library_btn.pack(side="left", padx=10)
    def create_layout(self):
        # Create the main frame to hold sidebar and content
        main_frame = tk.Frame(self, bg="#2b2b2b")
        main_frame.pack(side="top", fill="both", expand=True)
        # Sidebar
        sidebar = tk.Frame(main_frame, bg="#1e1e1e", width=200)
        sidebar.pack(side="left", fill="y")
        # Content Area
        self.content_frame = tk.Frame(main_frame, bg="#2b2b2b")
        self.content_frame.pack(side="right", fill="both", expand=True)
        # Add buttons to the sidebar
        home_btn = tk.Button(sidebar, text="Home", bg="#3e3e3e", fg="white", width=20, relief="flat", command=self.show_home)
        library_btn = tk.Button(sidebar, text="Library", bg="#3e3e3e", fg="white", width=20, relief="flat", command=self.show_library)
        store_btn = tk.Button(sidebar, text="Store", bg="#3e3e3e", fg="white", width=20, relief="flat", command=self.show_store)
        home_btn.pack(pady=10)
        library_btn.pack(pady=10)
        store_btn.pack(pady=10)
    def clear_content(self):
        # Clear content frame before displaying new content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    def show_home(self):
        self.clear_content()
        label = tk.Label(self.content_frame, text="Welcome to Home!", bg="#2b2b2b", fg="white", font=("Arial", 18))
        label.pack(pady=20)
    def show_library(self):
        self.clear_content()
        label = tk.Label(self.content_frame, text="This is your Library!", bg="#2b2b2b", fg="white", font=("Arial", 18))
        label.pack(pady=20)
    def show_store(self):
        self.clear_content()
        label = tk.Label(self.content_frame, text="Welcome to the Store!", bg="#2b2b2b", fg="white", font=("Arial", 18))
        label.pack(pady=20)
if __name__ == "__main__":
    app = SteamUI()
    app.mainloop()
