#!/usr/bin/env python3
"""
Basic example of using the BSUB.IO Python SDK.

This example demonstrates the simple workflow:
1. Create a job
2. Upload a file
3. Submit for processing
4. Wait for completion
5. Retrieve output
"""

import os
import sys
from pathlib import Path

from bsubio import BsubClient


def main() -> None:
    """Run basic example."""
    # Get API key from environment variable
    api_key = os.environ.get("BSUB_API_KEY")
    if not api_key:
        print("Error: BSUB_API_KEY environment variable not set", file=sys.stderr)
        print("Get your API key from https://app.bsub.io", file=sys.stderr)
        sys.exit(1)

    # Initialize client
    client = BsubClient(api_key=api_key)

    try:
        # Step 1: Create a job
        print("Creating job...")
        job = client.create_job("passthru")  # Using passthru type for demo
        print(f"✓ Job created: {job.id}")
        print(f"  Status: {job.status.value}")

        # Step 2: Upload a file
        print("\nUploading file...")
        # Create a simple test file
        test_file = Path("/tmp/bsub_test.txt")
        test_file.write_text("Hello from BSUB.IO Python SDK!")

        data_size = client.upload_file(job.id, job.upload_token, test_file)
        print(f"✓ File uploaded: {data_size} bytes")

        # Step 3: Submit for processing
        print("\nSubmitting job for processing...")
        client.submit_job(job.id)
        print("✓ Job submitted")

        # Step 4: Wait for completion
        print("\nWaiting for job to complete...")
        job = client.wait_for_job(job.id, poll_interval=1.0, timeout=60.0)
        print(f"✓ Job completed: {job.status.value}")

        # Step 5: Retrieve output
        if job.is_successful():
            print("\nRetrieving output...")
            output = client.get_output(job.id)
            print("✓ Output received:")
            print(output.decode("utf-8"))
        else:
            print(f"\n✗ Job failed: {job.error_message}", file=sys.stderr)
            logs = client.get_logs(job.id)
            print(f"Logs:\n{logs}", file=sys.stderr)
            sys.exit(1)

        # Cleanup
        test_file.unlink()
        print("\n✓ Example completed successfully!")

    except Exception as e:
        print(f"\n✗ Error: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        client.close()


if __name__ == "__main__":
    main()
