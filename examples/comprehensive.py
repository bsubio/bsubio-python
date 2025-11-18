#!/usr/bin/env python3
"""
Comprehensive example showcasing all BSUB.IO SDK features.

This example demonstrates:
- Getting available processing types
- Creating and managing jobs
- Uploading files
- Monitoring job status
- Retrieving results and logs
- Error handling
- Context manager usage
"""

import os
import sys
from pathlib import Path

from bsubio import BsubClient
from bsubio.exceptions import BsubError


def main() -> None:
    """Run comprehensive example."""
    api_key = os.environ.get("BSUB_API_KEY")
    if not api_key:
        print("Error: BSUB_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    # Use context manager for automatic cleanup
    with BsubClient(api_key=api_key) as client:
        # Display API information
        print("=" * 60)
        print("BSUB.IO Python SDK - Comprehensive Example")
        print("=" * 60)

        # Get API version
        version = client.get_version()
        print(f"\nAPI Version: {version.get('version')}")
        print(f"Server: {version.get('server')}")

        # Get available processing types
        print("\n" + "=" * 60)
        print("Available Processing Types:")
        print("=" * 60)
        types = client.get_types()
        for proc_type in types:
            print(f"\n{proc_type.name} ({proc_type.type})")
            print(f"  {proc_type.description}")
            if proc_type.example:
                print(f"  Example: {proc_type.example.cmd}")

        # List existing jobs
        print("\n" + "=" * 60)
        print("Existing Jobs:")
        print("=" * 60)
        jobs, total = client.list_jobs(limit=5)
        print(f"Total jobs: {total}")
        for job in jobs:
            print(f"  {job.id}: {job.status.value} ({job.type})")

        # Create a new job
        print("\n" + "=" * 60)
        print("Creating New Job:")
        print("=" * 60)
        try:
            job = client.create_job("passthru")
            print(f"✓ Job created: {job.id}")
            print(f"  Type: {job.type}")
            print(f"  Status: {job.status.value}")
            print(f"  Created: {job.created_at}")

            # Upload file
            print("\n" + "=" * 60)
            print("Uploading File:")
            print("=" * 60)
            test_file = Path("/tmp/comprehensive_test.txt")
            test_file.write_text("Comprehensive test data from BSUB.IO Python SDK")

            data_size = client.upload_file(job.id, job.upload_token, test_file)
            print(f"✓ Uploaded {data_size} bytes")

            # Get updated job details
            job = client.get_job(job.id)
            print(f"✓ Job status updated: {job.status.value}")

            # Submit job
            print("\n" + "=" * 60)
            print("Submitting Job:")
            print("=" * 60)
            client.submit_job(job.id)
            print("✓ Job submitted for processing")

            # Monitor progress
            print("\n" + "=" * 60)
            print("Monitoring Progress:")
            print("=" * 60)
            previous_status = None
            job = client.wait_for_job(job.id, poll_interval=1.0, timeout=60.0)

            if job.status != previous_status:
                print(f"  Status: {job.status.value}")
                previous_status = job.status

            # Get results
            print("\n" + "=" * 60)
            print("Results:")
            print("=" * 60)
            if job.is_successful():
                output = client.get_output(job.id)
                print(f"✓ Output ({len(output)} bytes):")
                print(output.decode("utf-8"))

                # Get logs
                logs = client.get_logs(job.id)
                if logs:
                    print("\nLogs:")
                    print(logs)

                print("\n✓ Job finished successfully!")
                print(
                    f"  Processing time: {(job.finished_at - job.created_at).total_seconds():.2f}s"
                )
            else:
                print(f"✗ Job failed: {job.error_message}", file=sys.stderr)
                print(f"  Error code: {job.error_code}", file=sys.stderr)
                logs = client.get_logs(job.id)
                print(f"\nError logs:\n{logs}", file=sys.stderr)

            # Cleanup test file
            test_file.unlink()

        except BsubError as e:
            print(f"\n✗ BSUB.IO Error: {e.message}", file=sys.stderr)
            print(f"  Status code: {e.status_code}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"\n✗ Unexpected error: {e}", file=sys.stderr)
            sys.exit(1)

    print("\n" + "=" * 60)
    print("✓ Comprehensive example completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
