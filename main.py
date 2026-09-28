from load_nput_data import read_email
from classify_email import email_classifier,client
import csv




OUTPUT_FILE = "results.csv"
def save_results(results):
    """Write the classification results to a CSV file."""

    fieldnames = [
        "id",
        "subject",
        "category",
        "status",
        "error"
    ]

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to {OUTPUT_FILE}")

async def main():


    try:
        emails = read_email()

        results = await email_classifier(emails)

        save_results(results)

        successful = sum(
            result["status"] == "Success"
            for result in results
        )

        failed = len(results) - successful

        print("\nClassification completed.")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")

    finally:
        await client.close()

