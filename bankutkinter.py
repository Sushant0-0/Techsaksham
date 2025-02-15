import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient funds. Available balance is {self.balance}.")
        elif amount > 0:
            self.balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"

class BankingSystem:
    def __init__(self, root):
        self.accounts = {}

        self.root = root
        self.root.title("Banking System")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
        style.map("TButton", background=[("active", "#45a049")])

        # Widgets for account creation
        self.create_account_frame = ttk.Frame(root)
        self.create_account_frame.pack(pady=10)

        self.acc_num_label = ttk.Label(self.create_account_frame, text="Account Number:")
        self.acc_num_label.grid(row=0, column=0, padx=5, pady=5)
        self.acc_num_entry = ttk.Entry(self.create_account_frame)
        self.acc_num_entry.grid(row=0, column=1, padx=5, pady=5)

        self.acc_holder_label = ttk.Label(self.create_account_frame, text="Account Holder:")
        self.acc_holder_label.grid(row=1, column=0, padx=5, pady=5)
        self.acc_holder_entry = ttk.Entry(self.create_account_frame)
        self.acc_holder_entry.grid(row=1, column=1, padx=5, pady=5)

        self.initial_balance_label = ttk.Label(self.create_account_frame, text="Initial Balance:")
        self.initial_balance_label.grid(row=2, column=0, padx=5, pady=5)
        self.initial_balance_entry = ttk.Entry(self.create_account_frame)
        self.initial_balance_entry.grid(row=2, column=1, padx=5, pady=5)

        self.create_acc_button = ttk.Button(self.create_account_frame, text="Create Account", command=self.create_account, style="Accent.TButton")
        self.create_acc_button.grid(row=3, columnspan=2, pady=10)

        # Widgets for transactions
        self.transaction_frame = ttk.Frame(root)
        self.transaction_frame.pack(pady=10)

        self.trans_acc_num_label = ttk.Label(self.transaction_frame, text="Account Number:")
        self.trans_acc_num_label.grid(row=0, column=0, padx=5, pady=5)
        self.trans_acc_num_entry = ttk.Entry(self.transaction_frame)
        self.trans_acc_num_entry.grid(row=0, column=1, padx=5, pady=5)

        self.amount_label = ttk.Label(self.transaction_frame, text="Amount:")
        self.amount_label.grid(row=1, column=0, padx=5, pady=5)
        self.amount_entry = ttk.Entry(self.transaction_frame)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.deposit_button = ttk.Button(self.transaction_frame, text="Deposit", command=self.deposit, style="Accent.TButton")
        self.deposit_button.grid(row=2, column=0, pady=10)

        self.withdraw_button = ttk.Button(self.transaction_frame, text="Withdraw", command=self.withdraw, style="Accent.TButton")
        self.withdraw_button.grid(row=2, column=1, pady=10)

        # Widgets for account information
        self.info_frame = ttk.Frame(root)
        self.info_frame.pack(pady=10)

        self.info_acc_num_label = ttk.Label(self.info_frame, text="Account Number:")
        self.info_acc_num_label.grid(row=0, column=0, padx=5, pady=5)
        self.info_acc_num_entry = ttk.Entry(self.info_frame)
        self.info_acc_num_entry.grid(row=0, column=1, padx=5, pady=5)

        self.info_button = ttk.Button(self.info_frame, text="Display Info", command=self.display_info, style="Accent.TButton")
        self.info_button.grid(row=1, columnspan=2, pady=10)

    def create_account(self):
        acc_num = self.acc_num_entry.get()
        acc_holder = self.acc_holder_entry.get()
        initial_balance = float(self.initial_balance_entry.get())

        if acc_num and acc_holder:
            self.accounts[acc_num] = Account(acc_num, acc_holder, initial_balance)
            messagebox.showinfo("Success", "Account created successfully!")
        else:
            messagebox.showwarning("Error", "Account number and holder name cannot be empty!")

    def deposit(self):
        acc_num = self.trans_acc_num_entry.get()
        amount = float(self.amount_entry.get())

        if acc_num in self.accounts:
            try:
                self.accounts[acc_num].deposit(amount)
                messagebox.showinfo("Success", f"Deposited {amount}. New balance is {self.accounts[acc_num].get_balance()}.")
            except ValueError as e:
                messagebox.showwarning("Error", str(e))
        else:
            messagebox.showwarning("Error", "Account not found!")

    def withdraw(self):
        acc_num = self.trans_acc_num_entry.get()
        amount = float(self.amount_entry.get())

        if acc_num in self.accounts:
            try:
                self.accounts[acc_num].withdraw(amount)
                messagebox.showinfo("Success", f"Withdrew {amount}. New balance is {self.accounts[acc_num].get_balance()}.")
            except InsufficientFundsError as e:
                messagebox.showwarning("Error", str(e))
            except ValueError as e:
                messagebox.showwarning("Error", str(e))
        else:
            messagebox.showwarning("Error", "Account not found!")

    def display_info(self):
        acc_num = self.info_acc_num_entry.get()

        if acc_num in self.accounts:
            account_info = self.accounts[acc_num].display_account_info()
            messagebox.showinfo("Account Info", account_info)
        else:
            messagebox.showwarning("Error", "Account not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingSystem(root)
    root.mainloop()
