import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os

class CredentialManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Credential Manager")
        self.master.geometry("1100x500")
        self.master.configure(bg='black')  # Light background color
        
        self.credentials = {
            "mega_email": "",
            "mega_password": "",
            "hugchat_email": "",
            "hugchat_password": "",
            "claude_cookie_header": "",
            "claude_user_agent": "",
            "reddit_client_id": "",
            "reddit_client_secret": "",
            "reddit_user_agent": "",
            "youtube_client_secrets_file": "",
            "speaker_wav_path": "",
            "tiktok_repo_username": "",
            "gpu usage (True or False)": ""
        }

        self.create_widgets()
        self.load_credentials()

    def create_widgets(self):
        # Dynamic form generation for credentials
        for i, (key, value) in enumerate(self.credentials.items()):
            tk.Label(
                self.master, 
                text=key.replace("_", " ").title() + ":", 
                bg='#f0f0f0'
            ).grid(row=i, column=0, sticky="e", padx=5, pady=2)
            
            entry = tk.Entry(self.master, width=150)
            entry.grid(row=i, column=1, padx=5, pady=2, sticky="ew")
            entry.insert(0, value)
            setattr(self, f"{key}_entry", entry)

        # Button for saving credentials
        save_button = tk.Button(self.master, text="Save", command=self.save_credentials, bg='#4CAF50', fg='white')
        save_button.grid(row=len(self.credentials), column=0, columnspan=2, pady=10, sticky="ew")
        
        # Button for loading credentials
        load_button = tk.Button(self.master, text="Load", command=self.load_credentials, bg='#008CBA', fg='white')
        load_button.grid(row=len(self.credentials) + 1, column=0, columnspan=2, pady=5, sticky="ew")

    def save_credentials(self):
        # Save the entered credentials to credentials.json
        for key in self.credentials:
            self.credentials[key] = getattr(self, f"{key}_entry").get()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "credentials.json")

        try:
            with open(file_path, "w") as f:
                json.dump(self.credentials, f, indent=4)
            messagebox.showinfo("Success", f"Credentials saved successfully to {file_path}!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save credentials: {str(e)}")

    def load_credentials(self):
        # Load credentials from credentials.json if it exists
        if os.path.exists("credentials.json"):
            with open("credentials.json", "r") as f:
                self.credentials = json.load(f)
            for key, value in self.credentials.items():
                getattr(self, f"{key}_entry").delete(0, tk.END)
                getattr(self, f"{key}_entry").insert(0, value)

def get_credential(key):
    # Utility function to fetch a specific credential
    if os.path.exists("credentials.json"):
        with open("credentials.json", "r") as f:
            credentials = json.load(f)
        return credentials.get(key, "")
    return ""

if __name__ == "__main__":
    root = tk.Tk()
    app = CredentialManager(root)
    root.mainloop()
