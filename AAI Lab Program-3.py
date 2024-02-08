#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class AutoSuggest:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def suggest(self, partial_word):
        suggestions = []
        partial_word = partial_word.lower()
        for word in self.dictionary:
            if word.startswith(partial_word):
                suggestions.append(word)
        return suggestions

if __name__ == "__main__":
    # Example dictionary
    dictionary = ["apple", "banana", "cherry", "grape", "orange", "pineapple"]
    
    # Initialize AutoSuggest with the dictionary
    auto_suggest = AutoSuggest(dictionary)
    
    while True:
        partial_word = input("Enter partial word: ")
        suggestions = auto_suggest.suggest(partial_word)
        print("Suggestions:", suggestions)


# In[1]:


class WordProcessor:
    def __init__(self):
        self.document = ""

    def input_text(self):
        text = input("Enter text: ")
        self.document += text

    def edit_text(self):
        print("Current Document:\n", self.document)
        choice = input("Edit (1: Append, 2: Replace, 3: Delete): ")
        if choice == "1":
            text = input("Enter text to append: ")
            self.document += text
        elif choice == "2":
            old_text = input("Enter text to replace: ")
            new_text = input("Enter new text: ")
            self.document = self.document.replace(old_text, new_text)
        elif choice == "3":
            text_to_delete = input("Enter text to delete: ")
            self.document = self.document.replace(text_to_delete, "")

    def format_text(self):
        print("Current Document:\n", self.document)
        choice = input("Format (1: Uppercase, 2: Lowercase): ")
        if choice == "1":
            self.document = self.document.upper()
        elif choice == "2":
            self.document = self.document.lower()

    def save_document(self):
        filename = input("Enter filename to save: ")
        with open(filename, "w") as file:
            file.write(self.document)
        print("Document saved successfully.")

if __name__ == "__main__":
    word_processor = WordProcessor()
    while True:
        print("\nWord Processor Menu:")
        print("1. Input Text")
        print("2. Edit Text")
        print("3. Format Text")
        print("4. Save Document")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            word_processor.input_text()
        elif choice == "2":
            word_processor.edit_text()
        elif choice == "3":
            word_processor.format_text()
        elif choice == "4":
            word_processor.save_document()
        elif choice == "5":
            print("Exiting Word Processor.")
            break
        else:
            print("Invalid choice. Please try again.")


# In[2]:


import tkinter as tk
from tkinter import messagebox

class WordProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Processor")

        self.document = tk.StringVar()
        self.text_entry = tk.Text(root)
        self.text_entry.pack(expand=True, fill="both")

        menu_bar = tk.Menu(root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Save", command=self.save_document)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menu_bar)

        format_menu = tk.Menu(menu_bar, tearoff=0)
        format_menu.add_command(label="Uppercase", command=self.format_uppercase)
        format_menu.add_command(label="Lowercase", command=self.format_lowercase)
        menu_bar.add_cascade(label="Format", menu=format_menu)
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

    def format_uppercase(self):
        document_content = self.text_entry.get("1.0", "end-1c")
        self.text_entry.delete("1.0", "end")
        self.text_entry.insert("1.0", document_content.upper())

    def format_lowercase(self):
        document_content = self.text_entry.get("1.0", "end-1c")
        self.text_entry.delete("1.0", "end")
        self.text_entry.insert("1.0", document_content.lower())

if __name__ == "__main__":
    root = tk.Tk()
    app = WordProcessorApp(root)
    root.mainloop()


# In[2]:


import tkinter as tk
from tkinter import messagebox
import tkinter.filedialog

class WordProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Processor")

        self.document = tk.StringVar()
        self.text_entry = tk.Text(root)
        self.text_entry.pack(expand=True, fill="both")
        self.text_entry.bind("<KeyRelease>", self.auto_suggest)  # Bind auto-suggestion to key release event

        menu_bar = tk.Menu(root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Save", command=self.save_document)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menu_bar)

        format_menu = tk.Menu(menu_bar, tearoff=0)
        format_menu.add_command(label="Uppercase", command=self.format_uppercase)
        format_menu.add_command(label="Lowercase", command=self.format_lowercase)
        menu_bar.add_cascade(label="Format", menu=format_menu)
        root.config(menu=menu_bar)

        # Suggestions listbox
        self.suggestions_listbox = tk.Listbox(root)
        self.suggestions_listbox.pack(side=tk.RIGHT, fill=tk.Y)
        self.suggestions_listbox.bind("<<ListboxSelect>>", self.select_suggestion)

    def auto_suggest(self, event):
        # Clear existing suggestions
        self.suggestions_listbox.delete(0, tk.END)

        # Get the current text in the text entry
        current_text = self.text_entry.get("1.0", tk.END).strip().split()[-1]

        # Suggestions based on current text
        suggestions = self.get_suggestions(current_text)

        # Display suggestions
        for suggestion in suggestions:
            self.suggestions_listbox.insert(tk.END, suggestion)

    def get_suggestions(self, partial_word):
        # Sample suggestions based on the partial word
        dictionary = ["apple", "banana", "cherry", "grape", "orange", "pineapple"]
        partial_word = partial_word.lower()
        suggestions = [word for word in dictionary if word.startswith(partial_word)]
        return suggestions

    def select_suggestion(self, event):
        # Get the selected suggestion and insert it into the text entry
        selected_index = self.suggestions_listbox.curselection()
        if selected_index:
            suggestion = self.suggestions_listbox.get(selected_index)
            current_text = self.text_entry.get("1.0", tk.END).strip()
            previous_text = " ".join(current_text.split()[:-1])
            self.text_entry.delete("1.0", tk.END)
            self.text_entry.insert(tk.END, previous_text + " " + suggestion)

    def save_document(self):
        document_content = self.text_entry.get("1.0", "end-1c")
        filename = tk.filedialog.asksaveasfilename(defaultextension=".txt",
                                                    filetypes=[("Text files", "*.txt"),
                                                               ("All files", "*.*")])
        if filename:
            with open(filename, "w") as file:
                file.write(document_content)
            messagebox.showinfo("Success", "Document saved successfully.")

    def format_uppercase(self):
        document_content = self.text_entry.get("1.0", "end-1c")
        self.text_entry.delete("1.0", "end")
        self.text_entry.insert("1.0", document_content.upper())

    def format_lowercase(self):
        document_content = self.text_entry.get("1.0", "end-1c")
        self.text_entry.delete("1.0", "end")
        self.text_entry.insert("1.0", document_content.lower())

if __name__ == "__main__":
    root = tk.Tk()
    app = WordProcessorApp(root)
    root.mainloop()


# In[ ]:




