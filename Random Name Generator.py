import random
import time

def display_intro():
    print("🎓 Welcome to the Random Student Selector Program!")
    print("--------------------------------------------------")
    print("This program will randomly select a student from the class.")
    print()

def select_random_student(students):
    """Randomly selects and returns one student from the list."""
    return random.choice(students)

def main():
    # Step 1: List of students
    students = [
        "Asher Ader",
        "Nathaniel Chao",
        "Caspian Farman-Farmaian",
        "Shaan Glazer",
        "Alexander Graves",
        "Naoki Izumi",
        "Seth Lieberman",
        "David Lozado",
        "Rayan Mohammadinia",
        "Colin Poirier",
        "Maddox Prata",
        "Dennis Riley",
        "Evan Sherman-Chan",
        "Blake Slobodsky"
    ]
    
    display_intro()
    
    input("Press ENTER to randomly select a student...")
    print("\nSelecting a student", end="", flush=True)
    
    # Add suspense animation
    for i in range(3):
        time.sleep(0.8)
        print(".", end="", flush=True)
    print("\n")

    # Step 2: Select a random name
    chosen_student = select_random_student(students)
    
    # Step 3: Display result
    print(f"🎉 The selected student is: {chosen_student} 🎉")
    print("\nGood luck, and great job participating today!")

# Run the program
if __name__ == "__main__":
    main()
