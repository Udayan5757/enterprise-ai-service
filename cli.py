import sys

from src.services.ingestion_service import IngestionService


def main():

    if len(sys.argv) < 2:

        print("Usage: python cli.py ingest")

        return

    command = sys.argv[1]

    if command == "ingest":

        IngestionService().ingest()

        print("Ingestion Completed.")

    else:

        print("Unknown command.")


if __name__ == "__main__":

    main()