class ReliefTeam:
    def __init__(self, name):
        self.name = name
        self.distributed = {
            "sanitary supplies": 0,
            "food": 0,
            "clothing": 0,
            "homeware": 0,
            "entertainment items": 0
        }

    def report_distribution(self, category, amount):
        if category in self.distributed:
            self.distributed[category] += amount
            print(f"Updated: {category} +{amount} units recorded for Team {self.name}.")
        else:
            print(f"Invalid category '{category}'. Please choose from: {', '.join(self.distributed.keys())}.")

    def show_progress(self):
        print(f"\n  Distribution Progress — Team {self.name}:")
        for category, amount in self.distributed.items():
            print(f"  {category.capitalize():<25} {amount:>6} units")


class Donor:
    VALID_TYPES = ["country", "individual", "organization"]

    def __init__(self, name, donor_type, amount):
        self.name = name
        self.donor_type = donor_type
        self.amount = amount

    def describe_donation(self):
        print(f"\n  Donor:  {self.name}")
        print(f"  Type:   {self.donor_type.capitalize()}")
        print(f"  Amount: ${self.amount:,.2f}")

relief_teams = {
    "A": ReliefTeam("A"),
    "B": ReliefTeam("B"),
    "C": ReliefTeam("C"),
}

donations = {}

def add_donation():
    print("\nDonation Portal:")
    name = input("  Enter donor name: ").strip()
    if not name:
        print("  Donor name cannot be empty.")
        return

    donor_type = input("  Enter donor type (country / individual / organization): ").strip().lower()
    if donor_type not in Donor.VALID_TYPES:
        print(f"  Invalid donor type. Must be one of: {', '.join(Donor.VALID_TYPES)}.")
        return

    try:
        amount = float(input("  Enter donation amount ($): ").strip())
        if amount <= 0:
            raise ValueError
        if not isinstance(amount, float):
            raise ValueError

    except ValueError:
        print("Invalid amount. Please enter a positive number.")
        return

    donor = Donor(name, donor_type, amount)
    donor.describe_donation()

    if name in donations:
        donations[name] += amount
        print(f"  Existing donor — updated total: ${donations[name]:,.2f}")
    else:
        donations[name] = amount
        print("  Donation recorded successfully. Thank you!")


def team_login():
    print("\nRelief Team Login:")
    team_id = input("  Enter your team (A / B / C): ").strip().upper()

    if team_id not in relief_teams:
        print("Invalid team. Please choose A, B, or C.")
        return
    
    if team_id == "A":
        password = input("Input password:")
        if password != "glbl5050a":
            print("Invalid password")
            return

    
    if team_id == "B":
        password = input("Input password:")
        if password != "glbl5050b":
            print("Invalid password")
            return
    
    if team_id == "C":
        password = input("Input password:")
        if password != "glbl5050c":
            print("Invalid password")
            return

    team = relief_teams[team_id]
    print(f"Welcome, Team {team_id}!")
    

    CATEGORIES = list(team.distributed.keys())

    while True:
        print(f"\n  Team {team_id} Menu")
        print("  1. Report distribution")
        print("  2. View progress")
        print("  3. Log out")
        choice = input("\n  Select an option: ").strip()

        if choice == "1":
            print(f"\nCategories: {', '.join(CATEGORIES)}")
            category = input("  Enter category: ").strip().lower()
            try:
                amount = int(input("  Enter quantity distributed: ").strip())
                if amount <= 0:
                    raise ValueError
                
            except ValueError:
                print("  Invalid quantity. Please enter a positive whole number.")
                continue
            team.report_distribution(category, amount)

        elif choice == "2":
            team.show_progress()

        elif choice == "3":
            print(f"  Team {team_id} logged out.")
            break

        else:
            print("  Invalid option. Please select 1, 2, or 3.")


def admin_portal():
    print("\n--- Administrator Portal ---")

    while True:
        print("\n  Admin Menu")
        print("  1. View total donations")
        print("  2. List all donors")
        print("  3. View all teams' distribution progress")
        print("  4. Return to main menu")
        choice = input("\n  Select an option: ").strip()

        if choice == "1":
            total = sum(donations.values())
            print(f"\n  Total donations received: ${total:,.2f}")

        elif choice == "2":
            if not donations:
                print("\n  No donations recorded yet.")
            else:
                print(f"\n  {'Donor':<30} {'Amount':>12}")
                for name, amount in donations.items():
                    print(f"  {name:<30} ${amount:>10,.2f}")
                print(f"  {'TOTAL':<30} ${sum(donations.values()):>10,.2f}")

        elif choice == "3":
            for team in relief_teams.values():
                team.show_progress()

        elif choice == "4":
            print("  Returning to main menu.")
            break

        else:
            print("  Invalid option. Please select 1–4.")


def main():
    print("Disaster Relief Resource Tracking System:")

    while True:
        print("\nMain Menu:")
        print("  1. Donate to the relief effort")
        print("  2. Log in as a relief team")
        print("  3. Access the administrator portal")
        print("  4. Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            add_donation()
        elif choice == "2":
            team_login()
        elif choice == "3":
            admin_portal()
        elif choice == "4":
            print("\nThank you for supporting disaster relief. Goodbye!\n")
        else:
            print("Invalid option. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

# Link to chatlog: https://chatgpt.com/share/69ab0354-1914-8007-a62a-2778b4640aae 