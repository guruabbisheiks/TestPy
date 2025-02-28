# Since I cannot directly create a Google Sheet, I'll provide a downloadable CSV template
# The user can upload it to Google Sheets and start using it.

import pandas as pd

# Create a structured dataframe for the baby medical journal
data = {
    "Date": [],
    "Doctor's Consultation": [],
    "Diagnosis/Observations": [],
    "Prescribed Medicines": [],
    "Vaccinations": [],
    "Medical Reports (File Links)": [],
    "Next Visit": [],
    "Notes": []
}

df = pd.DataFrame(data)

# Save as CSV
file_path = "/Users/guruabbisheiks/Desktop/PyData/Baby_Medical_Journal_Template.csv"
df.to_csv(file_path, index=False)

file_path
