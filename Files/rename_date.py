import os
import re

# Define a regular expression to match American-style dates
date_pattern = re.compile(r"""
    (0[1-9]|1[0-2])    # Month (01 to 12)
    -                  # Separator
    (0[1-9]|[12][0-9]|3[01])  # Day (01 to 31)
    -                  # Separator
    (\d{4})            # Year (four digits)
""", re.VERBOSE)

# Loop over the files in the current working directory
for filename in os.listdir('.'):
    # Check if the file name matches the American-style date pattern
    match = date_pattern.search(filename)

    if match:
        # Get the different parts of the date
        month, day, year = match.groups()

        # Form the European-style date
        european_date = f"{day}-{month}-{year}"

        # Get the parts of the filename before and after the date
        before_date = filename[:match.start()]
        after_date = filename[match.end():]

        # Form the new filename
        new_filename = f"{before_date}{european_date}{after_date}"

        # Rename the file
        os.rename(filename, new_filename)

        print(f"Renamed '{filename}' to '{new_filename}'")

#print("Renaming complete.")