import csv
from pathlib import Path


REQUIRED_COLUMNS = {
    "concentration_uM",
    "replicate",
    "viability_percent",
}


def load_data(file_path):
    """Load and validate simulated cell-viability measurements."""
    with open(file_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        if not reader.fieldnames:
            raise ValueError("The CSV file is empty or has no header.")

        missing_columns = REQUIRED_COLUMNS - set(reader.fieldnames)
        if missing_columns:
            raise ValueError(
                f"Missing required columns: {sorted(missing_columns)}"
            )

        measurements = []

        for line_number, row in enumerate(reader, start=2):
            try:
                concentration = float(row["concentration_uM"])
                replicate = int(row["replicate"])
                viability = float(row["viability_percent"])
            except (TypeError, ValueError):
                raise ValueError(
                    f"Invalid numeric value on CSV line {line_number}."
                ) from None

            if concentration < 0:
                raise ValueError(
                    f"Concentration cannot be negative (line {line_number})."
                )

            if replicate < 1:
                raise ValueError(
                    f"Replicate must be at least 1 (line {line_number})."
                )

            if not 0 <= viability <= 100:
                raise ValueError(
                    f"Viability must be between 0 and 100 "
                    f"(line {line_number})."
                )

            measurements.append({
                "concentration_uM": concentration,
                "replicate": replicate,
                "viability_percent": viability,
            })

    if not measurements:
        raise ValueError("The CSV file contains no measurements.")

    return measurements


def main():
    data_path = Path(__file__).parent / "data" / "cell_viability.csv"

    try:
        measurements = load_data(data_path)
        print(f"Successfully loaded {len(measurements)} measurements.")
        print("All measurements passed the validation checks.")
    except (OSError, ValueError) as error:
        print(f"Data validation failed: {error}")


if __name__ == "__main__":
    main()
