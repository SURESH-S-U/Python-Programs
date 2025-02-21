def get_user_preferences():
    print("Welcome to the Vacation Destination Decision Maker!")
    
    budget = input("What is your budget for the vacation? (low/medium/high): ").lower()
    climate = input("What type of climate do you prefer? (tropical/cold/mild): ").lower()
    activity = input("What activities are you interested in? (beach/adventure/culture/nature): ").lower()
    location = input("Do you have a preference for location? (domestic/international): ").lower()
    
    return budget, climate, activity, location


def suggest_destination(budget, climate, activity, location):
    suggestions = []

    if budget == "low":
        if climate == "tropical":
            suggestions.append("Goa, India" if location == "domestic" else "Bali, Indonesia")
        elif climate == "cold":
            suggestions.append("Manali, India" if location == "domestic" else "Nepal")
        elif climate == "mild":
            suggestions.append("Coorg, India" if location == "domestic" else "Vietnam")
    elif budget == "medium":
        if climate == "tropical":
            suggestions.append("Andaman Islands" if location == "domestic" else "Phuket, Thailand")
        elif climate == "cold":
            suggestions.append("Shimla, India" if location == "domestic" else "Switzerland")
        elif climate == "mild":
            suggestions.append("Ooty, India" if location == "domestic" else "Italy")
    elif budget == "high":
        if climate == "tropical":
            suggestions.append("Lakshadweep" if location == "domestic" else "Maldives")
        elif climate == "cold":
            suggestions.append("Kashmir, India" if location == "domestic" else "Iceland")
        elif climate == "mild":
            suggestions.append("Udaipur, India" if location == "domestic" else "France")

    if activity == "beach":
        suggestions.append("Goa" if location == "domestic" else "Hawaii")
    elif activity == "adventure":
        suggestions.append("Rishikesh, India" if location == "domestic" else "New Zealand")
    elif activity == "culture":
        suggestions.append("Jaipur, India" if location == "domestic" else "Japan")
    elif activity == "nature":
        suggestions.append("Munnar, India" if location == "domestic" else "Norway")

    print("\nBased on your preferences, here are some suggested vacation destinations:")
    for suggestion in suggestions:
        print(suggestion)


def main():
    budget, climate, activity, location = get_user_preferences()
    suggest_destination(budget, climate, activity, location)


if __name__ == "__main__":
    main()
