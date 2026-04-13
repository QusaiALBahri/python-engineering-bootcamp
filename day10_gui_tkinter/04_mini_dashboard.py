"""
Day 10, Lesson 4: Building a Mini Dashboard
A complete functional application combining:
  - Multiple widgets
  - Grid layout
  - Event handling
  - Data management
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class MiniDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Dashboard")
        self.root.geometry("600x500")
        self.root.config(bg="#f0f0f0")
        
        # Application data
        self.tasks = []
        self.balance = 1000.0
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        
        # ============================================
        # Header
        # ============================================
        
        header = tk.Frame(self.root, bg="#2c3e50")
        header.grid(row=0, column=0, columnspan=3, sticky="ew", padx=0, pady=0)
        
        title = tk.Label(header, text="Financial Dashboard", 
                        font=("Arial", 16, "bold"), bg="#2c3e50", fg="white")
        title.pack(pady=10)
        
        # ============================================
        # Balance Display (Top-left)
        # ============================================
        
        balance_frame = tk.LabelFrame(self.root, text="Your Balance", 
                                      font=("Arial", 11, "bold"), padx=10, pady=10)
        balance_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        tk.Label(balance_frame, text="Current Balance:", font=("Arial", 10)).pack()
        
        self.balance_label = tk.Label(balance_frame, text=f"${self.balance:.2f}",
                                     font=("Arial", 24, "bold"), fg="green")
        self.balance_label.pack(pady=10)
        
        # ============================================
        # Add Transaction (Top-middle)
        # ============================================
        
        transaction_frame = tk.LabelFrame(self.root, text="Add Transaction",
                                         font=("Arial", 11, "bold"), padx=10, pady=10)
        transaction_frame.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=10, pady=10)
        
        tk.Label(transaction_frame, text="Amount:").pack(side="left", padx=5)
        self.amount_entry = tk.Entry(transaction_frame, width=15)
        self.amount_entry.pack(side="left", padx=5)
        
        tk.Label(transaction_frame, text="Type:").pack(side="left", padx=5)
        self.type_var = tk.StringVar(value="expense")
        tk.Radiobutton(transaction_frame, text="Expense", variable=self.type_var, 
                      value="expense").pack(side="left")
        tk.Radiobutton(transaction_frame, text="Income", variable=self.type_var,
                      value="income").pack(side="left")
        
        tk.Button(transaction_frame, text="Add", command=self.add_transaction,
                 bg="blue", fg="white").pack(side="left", padx=5)
        
        # ============================================
        # Task Management (Bottom-left)
        # ============================================
        
        task_frame = tk.LabelFrame(self.root, text="Tasks",
                                   font=("Arial", 11, "bold"), padx=10, pady=10)
        task_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        
        tk.Label(task_frame, text="New Task:").pack(side="left", padx=5)
        self.task_entry = tk.Entry(task_frame, width=20)
        self.task_entry.pack(side="left", padx=5)
        
        tk.Button(task_frame, text="Add Task", command=self.add_task,
                 bg="green", fg="white").pack(side="left", padx=5)
        
        # ============================================
        # Transaction List (Bottom-right)
        # ============================================
        
        list_frame = tk.LabelFrame(self.root, text="Recent Transactions",
                                   font=("Arial", 11, "bold"), padx=10, pady=10)
        list_frame.grid(row=2, column=1, columnspan=2, sticky="nsew", padx=10, pady=10)
        
        # Create scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")
        
        self.transaction_list = tk.Listbox(list_frame, height=8, width=40, yscrollcommand=scrollbar.set)
        self.transaction_list.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.transaction_list.yview)
        
        # ============================================
        # Status Bar
        # ============================================
        
        status_frame = tk.Frame(self.root, bg="#ecf0f1", relief="sunken", borderwidth=1)
        status_frame.grid(row=3, column=0, columnspan=3, sticky="ew", padx=0, pady=0)
        
        self.status_label = tk.Label(status_frame, text="Ready", 
                                    bg="#ecf0f1", font=("Arial", 9))
        self.status_label.pack(anchor="w", padx=10, pady=5)
        
        # ============================================
        # Action Buttons
        # ============================================
        
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=4, column=0, columnspan=3, pady=10)
        
        tk.Button(button_frame, text="Clear All", command=self.clear_all,
                 bg="orange", fg="white", width=12).pack(side="left", padx=5)
        
        tk.Button(button_frame, text="About", command=self.show_about,
                 bg="gray", fg="white", width=12).pack(side="left", padx=5)
        
        tk.Button(button_frame, text="Exit", command=self.root.destroy,
                 bg="red", fg="white", width=12).pack(side="left", padx=5)
        
        # Configure grid weights
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        
    def add_transaction(self):
        """Add a new transaction"""
        try:
            amount = float(self.amount_entry.get())
            trans_type = self.type_var.get()
            
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be positive!")
                return
            
            # Update balance
            if trans_type == "income":
                self.balance += amount
                self.transaction_list.insert(0, f"+ ${amount:.2f} (Income) - {datetime.now().strftime('%H:%M')}")
            else:
                self.balance -= amount
                self.transaction_list.insert(0, f"- ${amount:.2f} (Expense) - {datetime.now().strftime('%H:%M')}")
            
            # Update display
            self.balance_label.config(text=f"${self.balance:.2f}",
                                     fg="green" if self.balance >= 0 else "red")
            
            # Clear entry
            self.amount_entry.delete(0, tk.END)
            
            # Update status
            self.update_status(f"Transaction added! Balance: ${self.balance:.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
    
    def add_task(self):
        """Add a new task"""
        task = self.task_entry.get().strip()
        
        if not task:
            messagebox.showwarning("Warning", "Please enter a task!")
            return
        
        self.tasks.append(task)
        self.transaction_list.insert(0, f"📋 {task}")
        self.task_entry.delete(0, tk.END)
        self.update_status(f"Task added! Total tasks: {len(self.tasks)}")
    
    def clear_all(self):
        """Clear all data"""
        if messagebox.askyesno("Confirm", "Are you sure you want to clear everything?"):
            self.transaction_list.delete(0, tk.END)
            self.tasks = []
            self.balance = 1000.0
            self.balance_label.config(text=f"${self.balance:.2f}", fg="green")
            self.amount_entry.delete(0, tk.END)
            self.task_entry.delete(0, tk.END)
            self.update_status("All data cleared!")
    
    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo("About", 
                           "Mini Dashboard v1.0\n\n"
                           "A simple Tkinter application for\n"
                           "managing finances and tasks.\n\n"
                           "Built with Python & Tkinter")
    
    def update_status(self, message):
        """Update status bar"""
        self.status_label.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniDashboard(root)
    print("✅ Lesson 4 Complete! Interactive dashboard is running.")
    root.mainloop()
