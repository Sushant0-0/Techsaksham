import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
from datetime import datetime

class Workout:
    def __init__(self, date, exercise_type, duration, calories_burned):
        self.date = date
        self.exercise_type = exercise_type
        self.duration = duration
        self.calories_burned = calories_burned

    def __str__(self):
        return f"{self.date}: {self.exercise_type} for {self.duration} minutes, {self.calories_burned} calories burned"

class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def view_workouts(self):
        for workout in self.workouts:
            print(workout)

    def save_data(self, filename):
        with open(filename, 'w') as file:
            for workout in self.workouts:
                file.write(f"{workout.date},{workout.exercise_type},{workout.duration},{workout.calories_burned}\n")

    def load_data(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                date, exercise_type, duration, calories_burned = line.strip().split(',')
                workout = Workout(date, exercise_type, int(duration), int(calories_burned))
                self.workouts.append(workout)

def add_workout(user):
    date = date_entry.get()
    exercise_type = exercise_entry.get()
    duration = int(duration_entry.get())
    calories_burned = int(calories_entry.get())
    workout = Workout(date, exercise_type, duration, calories_burned)
    user.add_workout(workout)
    update_workout_list()
    messagebox.showinfo("Success", "Workout added successfully!")

def view_workouts(user):
    workout_list.delete(0, tk.END)
    for workout in user.workouts:
        workout_list.insert(tk.END, str(workout))

def save_data(user):
    filename = "workouts.json"
    user.save_data(filename)
    messagebox.showinfo("Success", "Data saved successfully!")

def load_data(user):
    filename = "workouts.json"
    user.load_data(filename)
    update_workout_list()
    messagebox.showinfo("Success", "Data loaded successfully!")

def update_workout_list():
    workout_list.delete(0, tk.END)
    for workout in user.workouts:
        workout_list.insert(tk.END, str(workout))

def gym_project(user):
    messagebox.showinfo("Gym Project", "Gym project functionality is under construction.")

def main():
    global user, date_entry, exercise_entry, duration_entry, calories_entry, workout_list

    def initialize_user():
        global user
        name = name_entry.get()
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        user = User(name, age, weight)
        user_info_frame.pack_forget()
        main_frame.pack(pady=10)

    root = tk.Tk()
    root.title("Personal Fitness Tracker")
    root.geometry("600x400")
    root.configure(bg="#1e1e1e")

    user_info_frame = tk.Frame(root, bg="#1e1e1e")
    user_info_frame.pack(pady=10)

    tk.Label(user_info_frame, text="Name:", bg="#1e1e1e", fg="#ffffff").grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(user_info_frame, bg="#2e2e2e", fg="#ffffff")
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(user_info_frame, text="Age:", bg="#1e1e1e", fg="#ffffff").grid(row=1, column=0, padx=5, pady=5)
    age_entry = tk.Entry(user_info_frame, bg="#2e2e2e", fg="#ffffff")
    age_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(user_info_frame, text="Weight:", bg="#1e1e1e", fg="#ffffff").grid(row=2, column=0, padx=5, pady=5)
    weight_entry = tk.Entry(user_info_frame, bg="#2e2e2e", fg="#ffffff")
    weight_entry.grid(row=2, column=1, padx=5, pady=5)

    start_button = tk.Button(user_info_frame, text="Start", command=initialize_user, bg="#e74c3c", fg="#ffffff")
    start_button.grid(row=3, column=0, columnspan=2, pady=10)

    main_frame = tk.Frame(root, bg="#1e1e1e")

    tk.Label(main_frame, text="Date (YYYY-MM-DD):", bg="#1e1e1e", fg="#ffffff").grid(row=0, column=0, padx=5, pady=5)
    date_entry = tk.Entry(main_frame, bg="#2e2e2e", fg="#ffffff")
    date_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(main_frame, text="Exercise Type:", bg="#1e1e1e", fg="#ffffff").grid(row=1, column=0, padx=5, pady=5)
    exercise_entry = tk.Entry(main_frame, bg="#2e2e2e", fg="#ffffff")
    exercise_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(main_frame, text="Duration (minutes):", bg="#1e1e1e", fg="#ffffff").grid(row=2, column=0, padx=5, pady=5)
    duration_entry = tk.Entry(main_frame, bg="#2e2e2e", fg="#ffffff")
    duration_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(main_frame, text="Calories Burned:", bg="#1e1e1e", fg="#ffffff").grid(row=3, column=0, padx=5, pady=5)
    calories_entry = tk.Entry(main_frame, bg="#2e2e2e", fg="#ffffff")
    calories_entry.grid(row=3, column=1, padx=5, pady=5)

    button_frame = tk.Frame(main_frame, bg="#1e1e1e")
    button_frame.grid(row=4, column=0, columnspan=2, pady=10)

    add_button = tk.Button(button_frame, text="Add Workout", command=lambda: add_workout(user), bg="#e74c3c", fg="#ffffff")
    add_button.grid(row=0, column=0, padx=5, pady=5)

    view_button = tk.Button(button_frame, text="View Workouts", command=lambda: view_workouts(user), bg="#3498db", fg="#ffffff")
    view_button.grid(row=0, column=1, padx=5, pady=5)

    save_button = tk.Button(button_frame, text="Save Data", command=lambda: save_data(user), bg="#2ecc71", fg="#ffffff")
    save_button.grid(row=0, column=2, padx=5, pady=5)

    load_button = tk.Button(button_frame, text="Load Data", command=lambda: load_data(user), bg="#f1c40f", fg="#ffffff")
    load_button.grid(row=0, column=3, padx=5, pady=5)

    gym_button = tk.Button(button_frame, text="Gym Project", command=lambda: gym_project(user), bg="#9b59b6", fg="#ffffff")
    gym_button.grid(row=0, column=4, padx=5, pady=5)

    workout_list = tk.Listbox(main_frame, width=80, height=10, bg="#2e2e2e", fg="#ffffff")
    workout_list.grid(row=5, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
