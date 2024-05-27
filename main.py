from recycle_system import RecyclingSystem

def main():
    system = RecyclingSystem()
    print("Welcome to the Automated Collection and Reward System for Recyclable Items")
    
    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. View Total Reward")
        print("3. Reset System")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            item_type = input("Enter item type (A, B, C): ").upper()
            if item_type in ['A', 'B', 'C']:
                system.add_item(item_type)
                print(f"Item of type {item_type} added.")
            else:
                print("Invalid item type. Please enter A, B, or C.")
        elif choice == '2':
            total_reward = system.get_total_reward()
            print(f"Total reward accumulated: INR{total_reward:.2f}")
        elif choice == '3':
            system.reset()
            print("System reset for a new user session.")
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
