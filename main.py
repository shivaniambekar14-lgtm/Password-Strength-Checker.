
import tkinter as tk
import re

COMMON_PASSWORDS = {
    "password", "password123", "12345678",
    "qwerty123", "admin123", "iloveyou"
}

def check_password():
    password = password_entry.get()

    if not password:
        result_label.config(text="Please enter a password.", fg="orange")
        suggestions_label.config(text="")
        return

    if password.lower() in COMMON_PASSWORDS:
        result_label.config(text="Password Strength: Weak", fg="red")
        suggestions_label.config(
            text="This is a common password. Choose a unique one."
        )
        return

    checks = [
        (len(password) >= 12, "Use at least 12 characters."),
        (bool(re.search(r"[A-Z]", password)), "Add an uppercase letter."),
        (bool(re.search(r"[a-z]", password)), "Add a lowercase letter."),
        (bool(re.search(r"\d", password)), "Add a number."),
        (bool(re.search(r"[^A-Za-z0-9]", password)),
         "Add a special character.")
    ]

    score = sum(passed for passed, _ in checks)

    if len(password) < 8 or score <= 2:
        strength, color = "Weak", "red"
    elif score <= 3:
        strength, color = "Medium", "darkorange"
    else:
        strength, color = "Strong", "green"

    result_label.config(text=f"Password Strength: {strength}", fg=color)

    suggestions = [tip for passed, tip in checks if not passed]
    suggestions_label.config(
        text="Suggestions:\n" + "\n".join(suggestions)
        if suggestions else "Good character variety!"
    )

def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        toggle_button.config(text="Hide")
    else:
        password_entry.config(show="*")
        toggle_button.config(text="Show")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("480x360")
root.resizable(False, False)

tk.Label(
    root, text="Password Strength Checker",
    font=("Arial", 17, "bold")
).pack(pady=18)

tk.Label(root, text="Enter a sample password:").pack(pady=5)

password_frame = tk.Frame(root)
password_frame.pack(pady=8)

password_entry = tk.Entry(
    password_frame, width=27, font=("Arial", 12), show="*"
)
password_entry.pack(side="left", padx=5)

toggle_button = tk.Button(
    password_frame, text="Show", command=toggle_password
)
toggle_button.pack(side="left")

tk.Button(
    root, text="Check Strength", command=check_password
).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 13, "bold"))
result_label.pack(pady=8)

suggestions_label = tk.Label(
    root, text="", justify="left", wraplength=430
)
suggestions_label.pack(pady=5)

tk.Label(
    root, text="Demo only: passwords are not saved.",
    font=("Arial", 9), fg="gray"
).pack(side="bottom", pady=10)

root.mainloop()
