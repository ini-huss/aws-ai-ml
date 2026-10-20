from pathlib import Path

import numpy as np
import pandas as pd


# Find the CSV file relative to this Python script.
DATA_FILE = Path(__file__).parent / "student_scores.csv"


def load_data(file_path):
    """Load the raw dataset from a CSV file."""
    return pd.read_csv(file_path, na_values=["NA", ""])


def clean_data(df):
    """Clean missing, invalid, and duplicate records."""
    df = df.copy()

    # Remove rows with missing or empty names.
    df["name"] = df["name"].astype("string").str.strip()
    df = df.dropna(subset=["name"])
    df = df[df["name"] != ""]

    # Convert scores to numbers.
    # Invalid text values become missing values.
    df["score"] = pd.to_numeric(df["score"], errors="coerce")

    # Remove rows without a valid score.
    df = df.dropna(subset=["score"])

    # Keep scores within the range 0 to 100.
    df = df[df["score"].between(0, 100)]

    # Remove identical records.
    df = df.drop_duplicates()

    # Reset row numbering after cleaning.
    return df.reset_index(drop=True)


def process_data(df):
    """Calculate statistics using NumPy."""
    scores = df["score"].to_numpy(dtype=float)

    if scores.size == 0:
        raise ValueError("No valid scores remain after cleaning.")

    results = {
        "total_students": int(scores.size),
        "average_score": float(np.mean(scores)),
        "highest_score": float(np.max(scores)),
        "lowest_score": float(np.min(scores)),
        "pass_rate": float(np.mean(scores >= 50) * 100),
    }

    return results


def main():
    # Step 1: Load the data.
    raw_data = load_data(DATA_FILE)

    # Step 2: Clean the data.
    cleaned_data = clean_data(raw_data)

    # Step 3: Process the cleaned data.
    results = process_data(cleaned_data)

    # Step 4: Display the results.
    print("========== RAW DATA ==========")
    print(raw_data.to_string(index=False))

    print("\n========== CLEANED DATA ==========")
    print(cleaned_data.to_string(index=False))

    print("\n========== STATISTICS ==========")

    for key, value in results.items():
        label = key.replace("_", " ").title()

        if key in ("average_score", "pass_rate"):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")


if name == "__main__":
    main()