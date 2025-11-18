# BSUB.IO Python SDK Examples

This directory contains example scripts demonstrating how to use the BSUB.IO Python SDK.

## Prerequisites

1. Install the SDK:
   ```bash
   pip install bsubio
   ```

2. Get your API key from [https://app.bsub.io](https://app.bsub.io)

3. Set your API key as an environment variable:
   ```bash
   export BSUB_API_KEY="your-api-key-here"
   ```

## Examples

### basic.py

A simple example demonstrating the basic workflow:
- Creating a job
- Uploading a file
- Submitting for processing
- Waiting for completion
- Retrieving output

```bash
python examples/basic.py
```

### comprehensive.py

A comprehensive example showcasing all SDK features:
- Getting available processing types
- Listing existing jobs
- Creating and managing jobs
- Error handling
- Using the context manager

```bash
python examples/comprehensive.py
```

### batch.py

Demonstrates batch processing of multiple files in parallel:
- Processing multiple files simultaneously
- Managing multiple jobs
- Collecting results
- Performance optimization

```bash
python examples/batch.py
```

## Using the Makefile

You can also run examples using the Makefile:

```bash
# Run all examples
make examples

# Run a specific example
make example NAME=basic
make example NAME=comprehensive
make example NAME=batch
```

## Notes

- All examples use the `passthru` processing type by default, which simply returns the input
- For real use cases, use appropriate processing types (see `client.get_types()`)
- Make sure your API key is valid and has sufficient credits
- Examples create temporary files in `/tmp/` and clean them up automatically
