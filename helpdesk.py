from ticket import Ticket

class HelpDesk:
    def __init__(self):
        # starting with help desk variables
        self.tickets = []
        self.ticket_number_counter = 2000
        self.submitted_tickets = 0
        self.resolved_tickets = 0
        self.open_tickets = 0

    def create_ticket(self, staff_id, creator_name, contact_email, issue_description):
        # Create a new ticket
        password = None
        
        # Create ticket object for it to add to the list 
        ticket_number = self.ticket_number_counter
        ticket = Ticket(ticket_number, staff_id, creator_name, contact_email, issue_description, password)
        self.tickets.append(ticket)
        if "Password Change" in issue_description or "password change" in issue_description:
            # Generate password for password change requests
            password = self.generate_password(staff_id, creator_name)
            ticket.status="resolved"

        # Update ticket and statistics counters
        self.ticket_number_counter += 1
        self.submitted_tickets += 1
        self.open_tickets += 1
        print("Ticket created successfully!")

    def respond_to_ticket(self, ticket_number, feedback_response ):
        # Respond to a ticket with feedback
        ticket_number = int(ticket_number)
        if ticket_number < 2000:
            print("Invalid ticket number.")
            return
        
        if 2000 <= ticket_number < self.ticket_number_counter:
            ticket_index = ticket_number - 2000
            if ticket_index < len(self.tickets):
                ticket = self.tickets[ticket_index]
                if ticket.status == "Resolved" or ticket.status == "Closed":
                    print("The ticket is already resolved.")
                    return
                ticket.feedback_response = feedback_response
                print(feedback_response)
                ticket.status = "Resolved"
                self.open_tickets -= 1
                self.resolved_tickets += 1
                
                print("Ticket resolved successfully!")
                print(f"Ticket Number: {ticket.ticket_number}")
                print(f"Ticket Creator Name: {ticket.creator_name}")
                print(f"Contact Email: {ticket.contact_email}")
                print(f"Issue Description: {ticket.issue_description}")
                print(f"Feedback Response: {ticket.feedback_response}")
                print(f"Status: {ticket.status}")
                print(f"Password: {ticket.password}")
                if "Password Change" in ticket.issue_description or "password change" in ticket.issue_description:
                    # Automatically close ticket if it's a password change request
                    feedback_response = print(f"The new password is {self.generate_password(ticket.staff_id, ticket.creator_name)}")
                    feedback_response = ticket.feedback_response
                    ticket.status == 'Closed'
                    if ticket.status == 'Closed':
                        feedback_response = print("The ticket is already closed.")
                    else:
                        feedback_response
                else:
                    print("Response added successfully")
            else:
                print("Invalid ticket number.")
        else:
            print("Invalid ticket number.")

    def reopen_ticket(self, ticket_number):
        # Reopen a closed ticket
        ticket_number = int(ticket_number)
        if 2000 <= ticket_number < self.ticket_number_counter:
            ticket_index = ticket_number - 2000
            if ticket_index < len(self.tickets):
                if self.tickets[ticket_index].status == "Resolved":
                    self.tickets[ticket_index].status = "Reopened"
                    self.open_tickets += 1
                    self.resolved_tickets -=1
                    print("Ticket reopened successfully!")
                else:
                    print("Ticket is not closed.")
            else:
                print("Invalid ticket number.")
        else:
            print("Invalid ticket number.")

    def display_ticket_info(self, ticket_number):
        # Display information about a specific ticket
        ticket_number = int(ticket_number)
        if 2000 <= ticket_number < self.ticket_number_counter:
            ticket_index = ticket_number - 2000
            if ticket_index < len(self.tickets):
                ticket = self.tickets[ticket_index]
                print(f"Ticket Number: {ticket.ticket_number}")
                print(f"Ticket Creator Name: {ticket.creator_name}")
                print(f"Staff ID: {ticket.staff_id}")
                print(f"Contact Email: {ticket.contact_email}")
                print(f"Issue Description: {ticket.issue_description}")
                print(f"Feedback Response: {ticket.feedback_response}")
                print(f"Status: {ticket.status}")
            else:
                print("Invalid ticket number.")
        else:
            print("Invalid ticket number.")

    def display_tickets(self):
        # Display information about all tickets
        if self.tickets:
            ticket_number = 2000
            for ticket in self.tickets:
                print(f"Ticket {ticket_number}: Staff ID: {ticket.staff_id}, Creator Name: {ticket.creator_name}, Contact Email: {ticket.contact_email}, Description: {ticket.issue_description}, Password: {ticket.password if ticket.password else 'N/A'}, Feedback Response: {ticket.feedback_response}, Status: {ticket.status}")
                ticket_number += 1
        else:
            print("No tickets found.")

    def display_statistics(self):
        # Display ticket statistics
        print("\nTicket Statistics:")
        print(f"Total Tickets Submitted: {self.submitted_tickets}")
        print(f"Total Resolved Tickets: {self.resolved_tickets}")
        print(f"Total Open Tickets: {self.open_tickets}")

    def generate_password(self, staff_id, creator_name):
        # Generate a password for a password change request
        password = staff_id[:2] + creator_name[:3]
        print(f"The new password is ({password})")
        print(f"Status = Closed")
        return password
#
##
###
