# run.py
import os

def run_train_tool():
    os.system('python train_tool.py')

def run_ai_chat():
    os.system('python main.py')

def main():
    while True:
        print("\nWelcome! Please choose an option:")
        print("1. Run Train Tool (to define new conditions)")
        print("2. Run AI Chat")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            run_train_tool()
        elif choice == '2':
            run_ai_chat()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
