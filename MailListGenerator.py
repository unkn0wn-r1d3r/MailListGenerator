def generate_email_from_file(file_path, domain):
    """
    Reads a file containing first and last names, generates email addresses
    by appending the last name with the first letter of the first name and
    a specified domain, and prints each email address.

    Args:
    - file_path: Path to the text file with names.
    - domain: The domain to use for the email addresses, defaults to 'local.co'.
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into first and last names
                parts = line.strip().split()
                if len(parts) == 2:  # Ensure there are exactly 2 parts
                    first_name, last_name = parts
                    # Generate the email address
                    email_address = f"{last_name}{first_name[0].lower()}@{domain.lower()}"
                    print(email_address)
                else:
                    print(f"Invalid line format: {line}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = "names.txt"  # Replace with your actual file path
domain=input("\n Domain name: ")
generate_email_from_file(file_path,domain)
