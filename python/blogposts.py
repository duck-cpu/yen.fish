import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
from datetime import datetime

def generate_json():
    post_id = id_entry.get() or str(int(datetime.now().timestamp()))  # Generate id from timestamp if not provided
    title = title_entry.get()
    date = date_entry.get()
    content = content_text.get("1.0", tk.END).strip()  # Get all content from the text box and remove excess newlines
    image = image_entry.get()

    # Validate date format (yyyy-mm-dd)
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter the date in the format YYYY-MM-DD.")
        return

    post_data = {
        "id": post_id,
        "title": title,
        "date": date,
        "content": content,
        "image": image
    }

    # Open the existing posts.json file and append the new post
    existing_file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if existing_file_path:
        try:
            with open(existing_file_path, "r") as f:
                data = json.load(f)  # Load existing data from the file

            # Ensure it's a list; if it's empty or invalid, make it a list
            if not isinstance(data, list):
                data = []

            # Insert the new post at the beginning of the list
            data.insert(0, post_data)

            # Write the updated list back to the file
            with open(existing_file_path, "w") as f:
                json.dump(data, f, indent=4)

            messagebox.showinfo("Success", "Post added successfully at the top!")

        except json.JSONDecodeError:
            messagebox.showerror("Error", "Failed to load JSON. Please make sure it's a valid JSON file.")


# Create the main window
root = tk.Tk()
root.title("Blog Post Creator")

# Use ttk for modern styling
style = ttk.Style()
style.theme_use("default")  # You can change the theme here if needed (e.g., 'clam', 'alt', 'classic')

# Define the window layout using ttk
frame = ttk.Frame(root, padding="20")
frame.pack(fill="both", expand=True)

# ID input
ttk.Label(frame, text="ID (leave blank to auto-generate):").grid(row=0, column=0, sticky="e")
id_entry = ttk.Entry(frame, width=40)
id_entry.grid(row=0, column=1)

# Title input
ttk.Label(frame, text="Title:").grid(row=1, column=0, sticky="e")
title_entry = ttk.Entry(frame, width=40)
title_entry.grid(row=1, column=1)

# Date input
ttk.Label(frame, text="Date (YYYY-MM-DD):").grid(row=2, column=0, sticky="e")
date_entry = ttk.Entry(frame, width=40)
date_entry.grid(row=2, column=1)

# Content input (multiline)
ttk.Label(frame, text="Content (Markdown):").grid(row=3, column=0, sticky="ne")
content_text = tk.Text(frame, width=40, height=10)
content_text.grid(row=3, column=1, pady=10)

# Image URL input
ttk.Label(frame, text="Image URL (optional):").grid(row=4, column=0, sticky="e")
image_entry = ttk.Entry(frame, width=40)
image_entry.grid(row=4, column=1)

# Generate JSON button
generate_button = ttk.Button(frame, text="Add to JSON File", command=generate_json)
generate_button.grid(row=5, columnspan=2, pady=10)

# Run the application
root.mainloop()
