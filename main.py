from helpdesk import HelpDesk
from ticket import Ticket

def main():
    # Create an instance of HelpDesk
    help_desk = HelpDesk()

    # LOOP to create ticket system 
    while True:
        print("\nIT HELP DESK TICKETING SYSTEM")
        print("WRITE YOUR CHOICE")
        print("1. Create Ticket")
        print("2. Respond to Ticket")
        print("3. Reopen Ticket")
        print("4. Display Ticket Information")
        print("5. Display Tickets")
        print("6. Display Statistics")
        print("7. Quit the program")

        choice = input("Enter your choice-> ")

        if choice == "1":
            # Create a new ticket
            staff_id = input("Enter Staff ID-> ")
#loop if the field is blank
            while True:
                if not staff_id:
                    print("(ERROR: please enter your staff id as this field cannot be blank)")
                elif len(staff_id) < 2:
                    print("(ERROR: Staff ID must be at least 2 characters)")
                elif not staff_id.isalpha():
                    print("(ERROR: Staff ID can only contain alphabetic characters)")
                else:
                    break
                staff_id = input("Enter Staff ID-> ")
#creator name
            creator_name = input("Enter Ticket Creator Name-> ")
#loop if the field is blank
            while True:
                if not creator_name:
                    print("(ERROR: Please enter your full name as this field cannot be blank)")
                elif creator_name.isnumeric():
                    print("(ERROR: Name cannot be numeric)")
                elif len(creator_name) < 2:
                    print("(ERROR: Name must be at least 2 characters)")
                elif len(creator_name) > 30:
                    print("(ERROR: Name cannot be more than 30 characters)")
                elif not creator_name.isalpha():
                    print("(ERROR: Name can only contain alphabetic characters)")
                else:
                    break
                
                creator_name = input("Enter Ticket Creator Name-> ")
#CONTACT EMAIL
            contact_email = input("Enter Contact Email-> ")
#loop if the field is blank
            while True:
                if not contact_email:
                    print("(ERROR: Please enter your contact email as this field cannot be blank)")
                elif "@" not in contact_email:
                    print("(ERROR: Please enter a valid email address)")
                elif len(contact_email) < 2:
                    print("(ERROR: Email must be at least 2 characters)")
                else:
                    break
                contact_email = input("Enter Contact Email-> ")
#ISSUE DESCRIPTION
            issue_description = input("Enter Description of the Issue->")
#Loop
            while True:
                if not issue_description:
                    print("(ERROR: Please enter a description of the issue as this field cannot be blank)")
                elif len(issue_description) < 1:
                    print("(ERROR: Description must be at least 1 characters)")
                else:
                    break
                issue_description = input("Enter Description of the Issue->")
            help_desk.create_ticket(staff_id, creator_name, contact_email, issue_description)
        elif choice == "2":
# Responding to a ticket with feedback
            password = ""
            while password != "12345":
                print("Please provide password to enter this seciton")
                password = input("Enter password: ")
                if password == "12345":
                    print("Password accepted.")
                else:
                    print("Invalid password.")
            ticket_number = input("Enter the ticket number to respond to-> ")
            feedback_response = input("Enter feedback response-> ")
            if feedback_response == "":
                print("Feedback response cannot be empty")
                continue
            help_desk.respond_to_ticket(ticket_number, feedback_response)
        elif choice == "3":
            # Reopening a ticket
            ticket_number = input("Enter the ticket number to reopen-> ")
            help_desk.reopen_ticket(ticket_number)
        elif choice == "4":
            # Display information about a ticket
            ticket_number = input("Enter the ticket number to display information-> ")
            help_desk.display_ticket_info(ticket_number)
        elif choice == "5":
            # Display information about all tickets
            help_desk.display_tickets()
        elif choice == "6":
            # for displaying ticket statistics
            help_desk.display_statistics()
        elif choice == "7":
            # to exit
            print("Exiting")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


#
#
#
#
#
#
#
#