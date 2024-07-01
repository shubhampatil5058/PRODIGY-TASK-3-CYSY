import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageEncryptGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption Tool")

        self.image_label = tk.Label(self.root)
        self.image_label.pack(padx=10, pady=10)

        self.encrypt_button = tk.Button(self.root, text="Encrypt Image", command=self.encrypt_image)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = tk.Button(self.root, text="Decrypt Image", command=self.decrypt_image)
        self.decrypt_button.pack(pady=5)

        self.load_image_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        self.load_image_button.pack(pady=10)

        self.load_encrypted_button = tk.Button(self.root, text="Load Encrypted Image", command=self.load_encrypted_image)
        self.load_encrypted_button.pack(pady=5)

        self.save_encrypted_button = tk.Button(self.root, text="Save Encrypted Image", command=self.save_encrypted_image)
        self.save_encrypted_button.pack(pady=5)

        self.save_decrypted_button = tk.Button(self.root, text="Save Decrypted Image", command=self.save_decrypted_image)
        self.save_decrypted_button.pack(pady=5)

        self.loaded_image = None
        self.encrypted_image = None
        self.decrypted_image = None

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                image = Image.open(file_path)
                self.loaded_image = image
                self.encrypted_image = None  
                self.decrypted_image = None  
                self.display_image(image)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image:\n{str(e)}")

    def display_image(self, image):
        image.thumbnail((400, 400))  
        img_tk = ImageTk.PhotoImage(image)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

    def encrypt_image(self):
        if self.loaded_image:
            self.encrypted_image = self.loaded_image.copy()  

            
            r, g, b = self.encrypted_image.split()
            self.encrypted_image = Image.merge("RGB", (b, g, r))

            self.display_image(self.encrypted_image)
            messagebox.showinfo("Encryption", "Image Encrypted Successfully!")
        else:
            messagebox.showerror("Error", "No image loaded!")

    def save_encrypted_image(self):
        if self.encrypted_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                try:
                    self.encrypted_image.save(file_path)
                    messagebox.showinfo("Save", "Encrypted Image Saved Successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save image:\n{str(e)}")
        else:
            messagebox.showerror("Error", "No image encrypted!")

    def load_encrypted_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                image = Image.open(file_path)
                self.loaded_image = None  
                self.encrypted_image = image
                self.decrypted_image = None  
                self.display_image(image)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load encrypted image:\n{str(e)}")

    def decrypt_image(self):
        if self.encrypted_image:
            self.decrypted_image = self.encrypted_image.copy()  

            
            r, g, b = self.decrypted_image.split()
            self.decrypted_image = Image.merge("RGB", (b, g, r))

            self.display_image(self.decrypted_image)
            messagebox.showinfo("Decryption", "Image Decrypted Successfully!")
        else:
            messagebox.showerror("Error", "No image encrypted!")

    def save_decrypted_image(self):
        if self.decrypted_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                try:
                    self.decrypted_image.save(file_path)
                    messagebox.showinfo("Save", "Decrypted Image Saved Successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save image:\n{str(e)}")
        else:
            messagebox.showerror("Error", "No image decrypted!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptGUI(root)
    root.mainloop()
