import random

# Expanded list of first and last names
first_names = [
    "john", "jane", "alex", "emily", "michael", "sarah", "david", "laura", "chris", "megan",
    "james", "mary", "robert", "linda", "william", "barbara", "charles", "susan", "joseph", "jessica",
    "daniel", "karen", "thomas", "lisa", "matthew", "nancy", "anthony", "betty", "mark", "sandra",
    "donald", "ashley", "steven", "kimberly", "paul", "donna", "andrew", "carol", "joshua", "michelle",
    "kevin", "patricia", "brian", "jennifer", "george", "amy", "edward", "angela", "ronald", "melissa",
    "timothy", "deborah", "jason", "stephanie", "jeffrey", "rebecca", "ryan", "sharon", "jacob", "kathleen",
    "gary", "helen", "nicholas", "pamela", "eric", "katherine", "jonathan", "emma", "stephen", "christine"
]

last_names = [
    "smith", "johnson", "williams", "brown", "jones", "miller", "davis", "garcia", "rodriguez", "wilson",
    "martinez", "anderson", "taylor", "thomas", "hernandez", "moore", "martin", "jackson", "thompson", "white",
    "lopez", "lee", "gonzalez", "harris", "clark", "lewis", "robinson", "walker", "perez", "hall",
    "young", "allen", "sanchez", "wright", "king", "scott", "green", "baker", "adams", "nelson",
    "hill", "ramirez", "campbell", "mitchell", "roberts", "carter", "phillips", "evans", "turner", "torres",
    "parker", "collins", "edwards", "stewart", "flores", "morris", "nguyen", "murphy", "rivera", "cook",
    "rogers", "morgan", "peterson", "cooper", "reed", "bailey", "bell", "gomez", "kelly", "howard"
]

# List of company domains
company_domains = [
    "techcorp.com", "innovatech.com", "globalindustries.com", "finservices.com",
    "medsolutions.com", "edutech.com", "greenenergy.com", "marketleaders.com", "creativeworks.com"
]

# Generate AOL email addresses
email_addresses = set()
while len(email_addresses) < 7000:
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    
    # Random chance to create an email with initials
    if random.random() < 0.2:  # 20% chance
        first_initial = first_name[0]
        last_initial = last_name[0]
        email = f"{first_initial}{last_initial}{random.randint(1, 1000)}@aol.com"
    else:
        if random.random() < 0.7:  # 70% chance of creating a personal AOL email
            number = random.randint(1, 1000)
            email = f"{first_name}.{last_name}{number}@aol.com"
        else:  # 30% chance of creating a corporate email
            company = random.choice(company_domains)
            email = f"{first_name}.{last_name}@{company}"
            
    email_addresses.add(email)

# Save to a file
with open("aol_emails.txt", "w") as file:
    for email in email_addresses:
        file.write(email + "\n")

print("Generated 7000 AOL email addresses.")
