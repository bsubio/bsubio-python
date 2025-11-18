#!/usr/bin/env python3
"""
Batch processing example using the BSUB.IO Python SDK.

This example demonstrates:
- Processing multiple files in parallel
- Managing multiple jobs
- Waiting for all jobs to complete
- Collecting results
"""

import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from bsubio import BsubClient, Job
from bsubio.exceptions import BsubError


def process_file(client: BsubClient, file_path: Path, job_type: str = "passthru") -> Job:
    """
    Process a single file.

    Args:
        client: BSUB.IO client
        file_path: Path to file to process
        job_type: Processing type

    Returns:
        Completed job
    """
    print(f"Processing {file_path.name}...")

    # Create job
    job = client.create_job(job_type)

    # Upload file
    client.upload_file(job.id, job.upload_token, file_path)

    # Submit
    client.submit_job(job.id)

    # Wait for completion
    job = client.wait_for_job(job.id, poll_interval=1.0, timeout=120.0)

    return job


def main() -> None:
    """Run batch processing example."""
    api_key = os.environ.get("BSUB_API_KEY")
    if not api_key:
        print("Error: BSUB_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    print("=" * 60)
    print("BSUB.IO Python SDK - Batch Processing Example")
    print("=" * 60)

    # Create test files
    print("\nCreating test files...")
    test_files = []
    for i in range(5):
        file_path = Path(f"/tmp/batch_test_{i}.txt")
        file_path.write_text(f"Batch test file #{i}\nContent from BSUB.IO Python SDK")
        test_files.append(file_path)
    print(f"✓ Created {len(test_files)} test files")

    # Initialize client
    client = BsubClient(api_key=api_key)

    try:
        # Process files in parallel
        print("\n" + "=" * 60)
        print("Processing Files in Parallel:")
        print("=" * 60)

        start_time = time.time()
        completed_jobs = []
        failed_jobs = []

        # Use ThreadPoolExecutor for parallel processing
        with ThreadPoolExecutor(max_workers=3) as executor:
            # Submit all tasks
            future_to_file = {
                executor.submit(process_file, client, file_path): file_path
                for file_path in test_files
            }

            # Collect results as they complete
            for future in as_completed(future_to_file):
                file_path = future_to_file[future]
                try:
                    job = future.result()
                    if job.is_successful():
                        print(f"✓ {file_path.name}: Success")
                        completed_jobs.append(job)
                    else:
                        print(f"✗ {file_path.name}: Failed - {job.error_message}")
                        failed_jobs.append(job)
                except Exception as e:
                    print(f"✗ {file_path.name}: Error - {e}")

        end_time = time.time()

        # Summary
        print("\n" + "=" * 60)
        print("Results Summary:")
        print("=" * 60)
        print(f"Total files: {len(test_files)}")
        print(f"Successful: {len(completed_jobs)}")
        print(f"Failed: {len(failed_jobs)}")
        print(f"Total time: {end_time - start_time:.2f}s")

        # Retrieve outputs
        if completed_jobs:
            print("\n" + "=" * 60)
            print("Sample Outputs:")
            print("=" * 60)
            for i, job in enumerate(completed_jobs[:3]):  # Show first 3
                output = client.get_output(job.id)
                print(f"\nJob {job.id}:")
                print(output.decode("utf-8")[:100])  # First 100 chars

        # Cleanup
        print("\n" + "=" * 60)
        print("Cleanup:")
        print("=" * 60)
        for file_path in test_files:
            file_path.unlink()
        print(f"✓ Deleted {len(test_files)} test files")

        print("\n✓ Batch processing example completed!")

    except BsubError as e:
        print(f"\n✗ BSUB.IO Error: {e.message}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        client.close()


if __name__ == "__main__":
    main()
