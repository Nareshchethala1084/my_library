import pandas as pd

# List of 100 business-related nouns
business_nouns = [
    "investment", "revenue", "market", "entrepreneur", "startup", 
    "profit", "dividend", "economy", "industry", "partnership",
    "equity", "merger", "budget", "capital", "client",
    "commerce", "commodity", "consumer", "corporation", "data",
    "demand", "enterprise", "entrepreneurship", "export", "finance",
    "franchise", "goods", "growth", "import", "income",
    "inflation", "innovation", "inventory", "investment", "labor",
    "logistics", "management", "manufacturing", "marketing", "monopoly",
    "network", "niche", "operation", "opportunity", "order",
    "organization", "ownership", "partnership", "patent", "portfolio",
    "practice", "price", "producer", "product", "production",
    "profitability", "project", "promotion", "retail", "revenue",
    "risk", "sales", "sector", "share", "stakeholder",
    "strategy", "supply", "trade", "trader", "transaction",
    "venture", "volume", "workforce", "workplace", "yield",
    "management", "leadership", "networking", "negotiation", "outsourcing",
    "benchmarking", "brainstorming", "businessman", "buyer", "capacity",
    "deal", "decision", "efficiency", "executive", "goal",
    "group", "growth", "guideline", "headquarters", "hierarchy",
    "idea", "impact", "improvement", "incentive", "income",
    "increase", "index", "industry", "influence", "initiative"
]

# Create a DataFrame from the list
df = pd.DataFrame(business_nouns, columns=["Business Nouns"])

# Save the DataFrame to a CSV file
df.to_csv('business_nouns.csv', index=False)

print("CSV file has been created and saved as 'business_nouns.csv'.")

