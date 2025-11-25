import time
import schedule
from main_pipeline import run_pipeline


def job():
    print("Scheduled run:")
    run_pipeline()


def main():
    # Run every 5 minutes
    schedule.every(5).minutes.do(job)

    print("Scheduler started. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
