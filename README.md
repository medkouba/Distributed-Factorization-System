# Distributed Factorization System

This project consists of a distributed system for factorizing large numbers. The system includes a server and two worker processes communicating over a network. Additionally, there's a script (`one_machine.py`) to test factorization on a single machine.

## Files:

### `one_machine.py`

This script contains functions for factorizing a given number. It demonstrates the factorization of two numbers and measures the time taken for the factorization process on a single machine.

### `server.py`

This script creates a server that listens for incoming connections from two workers. It distributes chunks of numbers to the workers, receives factorization results, and calculates the sum of the factors. The server also measures the total time taken for the entire distributed process.

### `worker.py`

This script represents a worker process that connects to the server, receives a chunk of numbers to factorize, performs factorization, and sends back the factorization results to the server.

## Usage:

1. Run `server.py` to start the server.
2. Run `worker.py` on other machines to simulate multiple worker processes.
3. `one_machine.py` demonstrates factorization on a single machine without distributed processing.

## Dependencies:

- Python 3.x

## Instructions:

1. Start the server by running `server.py`.
2. Run `worker.py` on other machines to simulate multiple worker processes.
3. The server will distribute chunks of numbers to workers, and each worker will factorize the given numbers.
4. The server will collect and aggregate the factorization results from the workers.
5. The total time taken for the process will be displayed.

**Note:** Ensure that Python 3.x is installed on your system before running the scripts.

Feel free to modify the code or extend the functionality as needed.
