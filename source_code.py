# Importing Modules 
import csv
import os
from datetime import datetime

ATTENDANCE_FILE = "attendance.csv"


# Function to create file if not exists 

def initialize_file():
    if not os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll Number", "Name", "Date", "Time"])
        print("Attendance file created.\n")


# Function to mark attendance 

def mark_attendance():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ") 

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    with open(ATTENDANCE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, date, time])

    print(f"\n✔ Attendance marked for {name} at {time} on {date}\n")


# Function to view attendance

def view_attendance():
    if not os.path.exists(ATTENDANCE_FILE):
        print("No attendance data found.\n")
        return

    with open(ATTENDANCE_FILE, "r") as file:
        reader = csv.reader(file)
        print("\n--- Attendance Records ---")
        for row in reader:
            print(row)
    print()


# Main Menu

def main():
    initialize_file()

    while True:
        print("===== Attendance System =====")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run the program
main() 


#testing 1 