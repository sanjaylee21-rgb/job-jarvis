import os

from dotenv import load_dotenv

load_dotenv()

TARGET_ROLES = [
    "Financial Analyst",
    "Investment Analyst",
    "Equity Research Analyst",
    "Research Associate",
    "Portfolio Analyst",
    "Finance Analyst",
    "Pricing Analyst",
    "Investment Banking Analyst",
]

TARGET_LOCATIONS = [
    "Chennai",
    "Coimbatore",
    "Bangalore",
    "Hyderabad",
    "Pune",
    "Gurgaon",
]

EXCLUDED_ROLES = [
    "Sales",
    "Field Sales",
    "Telecalling",
    "Direct Marketing",
    "Insurance Sales",
]

MIN_MATCH_SCORE = int(os.getenv("MIN_MATCH_SCORE", "75"))
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5")
