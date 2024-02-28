import os
from datetime import datetime

def create_files():
    files = ["dreams.txt", "entry_counter.txt", "lucidity.txt"]
    for file in files:
        if not os.path.exists(file):
            with open(file, "w") as f:
                f.write("0")

def newEntry():
    create_files()

    # Increment dreams remembered
    with open("dreams.txt", "r+") as dreams_file:
        dreams_num = int(dreams_file.read())
        dreams_file.seek(0)
        dreams_remembered = int(input("How many dreams do you remember? "))
        dreams_num += dreams_remembered
        dreams_file.write(str(dreams_num))

    # Increment lucid dreams
    with open("lucidity.txt", "r+") as lucidity_file:
        lucidity_num = int(lucidity_file.read())
        lucidity_file.seek(0)
        lucid_dreams = int(input("How many dreams were lucid? "))
        lucidity_num += lucid_dreams
        lucidity_file.write(str(lucidity_num))

    # Create new entry file
    filename = input("Enter entry title: ")
    filename = filename.replace(" ", "_") + ".txt"
    with open(filename, "w") as entry_file:
        entry_file.write(f"Date and Time: {datetime.now()}\n")
        entry_title = input("Enter entry title: ")
        entry_file.write(f"Title: {entry_title}\n")
        entry_text = input("Write your entry: ")
        entry_file.write(entry_text)

    # Increment entry counter
    with open("entry_counter.txt", "r+") as entry_counter_file:
        entry_count = int(entry_counter_file.read())
        entry_count += 1
        entry_counter_file.seek(0)
        entry_counter_file.write(str(entry_count))

def dreamStatistics():
    create_files()

    # Calculate statistics
    with open("dreams.txt", "r") as dreams_file, \
            open("entry_counter.txt", "r") as entry_counter_file, \
            open("lucidity.txt", "r") as lucidity_file:
        dreams_num = int(dreams_file.read())
        entry_num = int(entry_counter_file.read())
        lucidity_num = int(lucidity_file.read())

    if entry_num != 0:
        avg_dreams = dreams_num / entry_num
        avg_lucid_dreams = lucidity_num / entry_num
    else:
        avg_dreams = 0
        avg_lucid_dreams = 0

    # Print statistics
    print(f"Number of dreams remembered: {dreams_num}")
    print(f"Average dreams remembered: {avg_dreams}")
    print(f"Number of lucid dreams: {lucidity_num}")
    print(f"Average lucid dreams per night: {avg_lucid_dreams}")
    print(f"Number of entries: {entry_num}")

def readEntries():
    # List all entries
    entries = os.listdir('.')
    print("Available entries:")
    for entry in entries:
        if entry.endswith('.txt'):
            print(entry)

    # Read chosen entry
    entry_choice = input("Enter the filename you'd like to read: ")
    if entry_choice in entries:
        with open(entry_choice, "r") as chosen_entry:
            print(chosen_entry.read())
    else:
        print("Entry not found.")

# Main program
while True:
    print("\n[1] Record entry\n[2] Dream statistics\n[3] Read entries")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        newEntry()
    elif choice == '2':
        dreamStatistics()
    elif choice == '3':
        readEntries()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
