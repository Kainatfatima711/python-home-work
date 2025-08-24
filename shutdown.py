def shutdown(command):
    if command == "yes":
        return "Shutting down..."
    elif command == "no":
        return "Shutdown cancelled."
    else:
        return "Invalid command."


user_input = input("Do you want to shutdown? (yes/no): ")
print(shutdown(user_input))