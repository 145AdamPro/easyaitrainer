# groq_tool.py

def update_conditions():
    condition = input("Enter a condition (e.g., 'hello') to check: ")
    response = input(f"What should the AI respond when the condition '{condition}' is met? ")

    with open('conditions.py', 'r') as file:
        lines = file.readlines()

    # Find where the last elif or else statement is, and insert the new condition before it.
    insert_position = None
    for i, line in enumerate(lines):
        if line.strip().startswith('else:'):
            insert_position = i
            break
        elif line.strip().startswith('elif'):
            insert_position = i + 1

    # Insert the new condition at the appropriate position
    new_condition = f"    elif user_input.lower() == '{condition}':\n"
    new_response = f"        return '{response}'\n"

    if insert_position is not None:
        lines.insert(insert_position, new_condition)
        lines.insert(insert_position + 1, new_response)

    # Rewrite the conditions file with the updated conditions
    with open('conditions.py', 'w') as file:
        file.writelines(lines)

    print(f"Condition for '{condition}' updated successfully!")

def interact_with_user():
    while True:
        command = input("\nDo you want to add a new condition? (yes/no): ").lower()
        if command == 'yes':
            update_conditions()
        elif command == 'no':
            print("Returning to main menu...")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    interact_with_user()
