"""
Title: MediaFlex Title Matching Script

Description:
    This script matches titles from two Excel files using fuzzy string matching. 
    It loads titles from the NTLC Collection Output and the Mediaflex MDD MoveList, 
    performs fuzzy matching to find the best match for each title, 
    and merges relevant metadata from the MDD MoveList to the NTLC data. 
    The results are saved to a new Excel file.

Dependencies:
    - pandas
    - numpy
    - fuzzywuzzy
    - python-Levenshtein
    - joblib
    - tqdm
    - openpyxl

Usage:
    python match_titles.py

Functions:
    - get_best_match_title(row_title, choices):
        Computes the best match and the corresponding score for a given title from a list of choices.

    - main():
        Main function to execute the matching process.

Setting n_jobs:
    To improve processing speed, you can adjust the n_jobs parameter in the Parallel call.
    - n_jobs=-1: Use all available cores.
    - n_jobs=<number>: Use the specified number of cores.
    Example: 
        results = Parallel(n_jobs=4, backend="multiprocessing")(
            delayed(get_best_match_title)(title, choices) for title in tqdm(df_ntlc['FTITLE'], desc="Processing", unit="record")
        )
    This will use 4 cores for parallel processing.

Checking CPU Cores:
    To check the number of physical cores and logical processors in your CPU, you can use the following command in the Windows Command Prompt:
        wmic CPU get NumberOfCores,NumberOfLogicalProcessors
    This will output the number of physical cores and logical processors, which can help you decide on the appropriate value for n_jobs.

Author:
    Tao Ling 

Date:
    2024-07-30
"""

import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from joblib import Parallel, delayed
from tqdm import tqdm
import time

# Function to get the best match title and score using fuzz.ratio
def get_best_match_title(row_title, choices):
    """
    Computes the best match and the corresponding score for a given title from a list of choices.

    Parameters:
        row_title (str): The title to be matched.
        choices (list): A list of potential matching titles.

    Returns:
        tuple: The best matching title and its corresponding fuzzy matching score.
    """
    title = row_title.lower()
    scores = np.array([fuzz.ratio(title, choice.lower()) for choice in choices])
    best_match_index = scores.argmax()
    return choices[best_match_index], scores[best_match_index]

def main():
    """
    Main function to execute the matching process.

    Loads the Excel files, converts necessary columns to strings, performs fuzzy matching,
    merges metadata from MDD MoveList, and saves the results to a new Excel file.
    """
    # Load the Excel files
    file_path_ntlc = 'data/NTLC/NTLC Collection Output April 2020.xlsx'
    # file_path_mdd = 'data/Mediaflex/MDD-MoveList-All-20240717.xlsx'
    file_path_mdd = 'data/Mediaflex/MDD-MoveList-Form-20240717.xlsx'

    df_ntlc = pd.read_excel(file_path_ntlc)
    df_mdd = pd.read_excel(file_path_mdd, sheet_name='Export Worksheet')

    # Convert FTITLE and MOVIETITLE columns to strings
    df_ntlc['FTITLE'] = df_ntlc['FTITLE'].astype(str)
    df_mdd['MOVIETITLE'] = df_mdd['MOVIETITLE'].astype(str)

    # Convert choices to a list
    choices = df_mdd['MOVIETITLE'].tolist()

    # Measure start time
    start_time = time.time()

    # Apply get_best_match_title in parallel with progress bar (see header for n_jobs setting)
    results = Parallel(n_jobs=-1, backend="multiprocessing")(
        delayed(get_best_match_title)(title, choices) for title in tqdm(df_ntlc['FTITLE'], desc="Processing", unit="record")
    )

    # Convert results to DataFrame
    results_df = pd.DataFrame(results, columns=['MOVIETITLE', 'FuzzyMatchingScore'])

    # Add results to df_ntlc
    df_ntlc[['MOVIETITLE', 'FuzzyMatchingScore']] = results_df

    # Merge df_ntlc with the relevant columns from df_mdd
    df_mdd_subset = df_mdd[['MOVIETITLE', 'VERSION_ID', 'TITLE_ID_FK', 'VERSIONNO', 'PROGRAMTITLE', 'PROGRAMYEAR', 'CONCATENATED_COUNTRIES', 'CONCATENATED_LANGUAGES', 'CONCATENATED_FORMS']]
    result = pd.merge(df_ntlc, df_mdd_subset, on='MOVIETITLE', how='left')

    # Save the result to a new Excel file
    output_file_path = 'data/output/matching_results.xlsx'
    result.to_excel(output_file_path, index=False)

    # Measure end time
    end_time = time.time()

    print(f"Results saved to {output_file_path}")
    print(f"Processing time: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()
