#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_cell_magic('cmd', '', 'pip install language_tool_python\n')


# In[2]:


import tkinter as tk
from tkinter import messagebox, filedialog
import enchant

class SpellCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spell Checker")

        self.text_editor = tk.Text(root, wrap="word")
        self.text_editor.pack(expand=True, fill="both")

        self.dictionary = enchant.Dict("en_US")

        menu_bar = tk.Menu(root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menu_bar)

        self.check_button = tk.Button(root, text="Check Spelling", command=self.check_spelling)
        self.check_button.pack()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                text = file.read()
                self.text_editor.delete("1.0", tk.END)
                self.text_editor.insert(tk.END, text)

    def save_file(self):
        text_content = self.text_editor.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_content)
            messagebox.showinfo("Success", "File saved successfully.")

    def check_spelling(self):
        text_content = self.text_editor.get("1.0", tk.END)
        errors = []
        words = text_content.split()
        for word in words:
            if not self.dictionary.check(word):
                errors.append(word)

        if errors:
            messagebox.showwarning("Spelling Errors", f"The following words are misspelled:\n\n{', '.join(errors)}")
        else:
            messagebox.showinfo("No Errors", "No spelling errors found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpellCheckerApp(root)
    root.mainloop()


# In[ ]:


pip install pyenchant


# In[1]:


import tkinter as tk
from tkinter import messagebox
import string

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")

        self.text_entry = tk.Text(root)
        self.text_entry.pack(expand=True, fill="both")

        menu_bar = tk.Menu(root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Save", command=self.save_document)
        file_menu.add_command(label="Check Spelling", command=self.check_spelling)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menu_bar)

    def save_document(self):
        document_content = self.text_entry.get("1.0", "end-1c")
        filename = tk.filedialog.asksaveasfilename(defaultextension=".txt",
                                                    filetypes=[("Text files", "*.txt"),
                                                               ("All files", "*.*")])
        if filename:
            with open(filename, "w") as file:
                file.write(document_content)
            messagebox.showinfo("Success", "Document saved successfully.")

    def check_spelling(self):
        document_content = self.text_entry.get("1.0", "end-1c")
        words = document_content.split()
        misspelled_words = []

        for word in words:
            # Remove punctuation from the word
            word = word.translate(str.maketrans('', '', string.punctuation))

            # Check if the word is in a dictionary (simple implementation)
            if not self.is_valid_word(word):
                misspelled_words.append(word)

        if misspelled_words:
            messagebox.showinfo("Spelling Errors", "Misspelled words: {}".format(", ".join(misspelled_words)))
        else:
            messagebox.showinfo("Spelling Errors", "No spelling errors found.")

    def is_valid_word(self, word):
        # Simple dictionary of valid words (replace with your own dictionary)
        valid_words = {"apple", "banana", "cherry", "grape", "orange", "pineapple"}
        return word.lower() in valid_words

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()


# In[ ]:




