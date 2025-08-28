"""
File: utils_batyrov.py

Purpose: Reusable header/tagline module for analytics projects.

Description:
A short, first-week module to demonstrate key skills:
- declare basic variables (bool, int, str, list)
- compose a reusable f-string "tagline" (a formatted-string header block)
- expose a function named get_tagline() that can be imported into other modules
- run this file as a script via main() using the if __name__ == '__main__' pattern

Author: Bakhrom Botirov



#####################################
# Import Modules
#####################################

import statistics
import loguru  # Easy logging
import pyttsx3  # type: ignore # Text-to-speech engine

#####################################
# Configure Simple Logger
#####################################

logger = loguru.logger
logger.add(
    "project.log",
    level="INFO",
    rotation="100 KB",
    backtrace=False,
    diagnose=False,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{line} | {message}",
)
logger.info("Logger loaded.")

#####################################
# Declare Global Variables
#####################################

# Boolean variables
is_accepting_clients: bool = True
offers_remote_workshops: bool = True
is_hiring: bool = False  # new boolean

# Integer variables
current_year: int = 2025
year_started: int = 2020
number_of_employees: int = 25  # new integer

# String variables
author: str = "Bakhrom Botirov"  # updated
organization: str = "Batyrov Analytics"  # updated
motto: str = "Clear. Precise. Reliable."  # updated
location: str = "Tashkent, Uzbekistan"  # new string

# List variables
services: list[str] = ["Data Analysis", "Machine Learning", "Business Intelligence"]
satisfaction_scores: list[float] = [4.8, 4.6, 4.9, 5.0, 4.7]
office_locations: list[str] = ["Tashkent", "Samarkand", "Bukhara"]  # new list

# Calculated variables
years_active: int = current_year - year_started
min_score: float = min(satisfaction_scores)
max_score: float = max(satisfaction_scores)
count_of_services: int = len(services)
count_of_scores: int = len(satisfaction_scores)
count_of_locations: int = len(office_locations)  # new calculated variable

# Statistics
mean_score: float = statistics.mean(satisfaction_scores)
stdev_score: float = statistics.stdev(satisfaction_scores)

#####################################
# Compose Byline (formatted string)
#####################################

byline: str = f"""
**********************************************************
{organization} — Project Header
**********************************************************
Author:                     {author}
Motto:                      {motto}
Location:                   {location}
Years Active:               {years_active}
Number of Employees:        {number_of_employees}
Accepting New Clients?:     {is_accepting_clients}
Hiring?:                    {is_hiring}
Remote Workshops?:          {offers_remote_workshops}
Services:                   {services}
Office Locations:           {office_locations}
Client Satisfaction Scores: {satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score:    {mean_score:.2f}
     Standard Deviation:    {stdev_score:.2f}
**********************************************************
"""

#####################################
# Define Global Functions
#####################################

def get_byline() -> str:
    """Return the reusable byline/tagline string."""
    return byline


def read_byline_aloud() -> None:
    """Use text-to-speech to read the byline aloud."""
    engine = pyttsx3.init()
    if engine is not None:
        engine.say(str(get_byline()))
        engine.runAndWait()

#####################################
# Define main() for testing
#####################################

def main() -> None:
    """Test this module when running it as a script."""
    logger.info("STARTING main()..")
    logger.info("Byline:\n" + get_byline())

    try:
        # Uncomment next line if you want audio feedback (use CTRL+C to stop)
        # read_byline_aloud()
        pass
    except KeyboardInterrupt:
        logger.info("Speech interrupted by user (Ctrl+C).")
    except Exception as ex:
        logger.warning(f"Text-to-speech skipped: {ex}")

    logger.info("This module is organized like all Python modules.")
    logger.info("We write professional Python from the start.")
    logger.info("END main()...")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()
"""