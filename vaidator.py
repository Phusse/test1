import re

def validate_email(email):
    """
    Validate an email address using a regular expression.
    """
    # Define the regex pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use the re.match() function to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

def extract_emails(text):
    """
    Extract all valid email addresses from a given text.
    """
    # Define the regex pattern for finding email addresses
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    
    # Use the re.findall() function to extract all email addresses from the text
    emails = re.findall(pattern, text)
    return emails

def main():
    print("Email Validator and Extractor")
    print("-----------------------------")
    
    text = input("Enter a text: ")
    
    # Extract and print all valid email addresses
    emails = extract_emails(text)
    if emails:
        print("\nValid Email Addresses Found:")
        for email in emails:
            print(email)
    else:
        print("\nNo valid email addresses found in the text.")
    
    email_to_validate = input("\nEnter an email to validate: ")
    if validate_email(email_to_validate):
        print(f"{email_to_validate} is a valid email address.")
    else:
        print(f"{email_to_validate} is not a valid email address.")

if __name__ == "__main__":
    main()
