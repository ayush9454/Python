import os
import re

date_pattern = re.compile(r"""
    (0[1-9]|1[0-2])    
    -                  
    (0[1-9]|[12][0-9]|3[01])  
    -                  
    (\d{4})            
""", re.VERBOSE)

for filename in os.listdir('.'):
    match = date_pattern.search(filename)

    if match:
        month, day, year = match.groups()

        european_date = f"{day}-{month}-{year}"

        before_date = filename[:match.start()]
        after_date = filename[match.end():]

        new_filename = f"{before_date}{european_date}{after_date}"

        os.rename(filename, new_filename)

        print(f"Renamed '{filename}' to '{new_filename}'")

