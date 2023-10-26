# Logistic-service

## Running the Project Using Docker

### Start the project using Docker Compose:

1. Clone the project:

    ```bash
    git clone https://github.com/vladysllav/logistic-service.git
    ```

2. Change to the `logistic-service` directory:

    ```bash
    cd logistic-service
    ```

3. Install Poetry:

    ```bash
    pip install poetry
    ```

4. Install project dependencies using Poetry:

    ```bash
    poetry install
    ```

5. Create a `.env` file and copy the necessary environment variable values into it. You can use the `env.example` file in the project's root as a reference.

6. Build Docker containers (if not already built):

    ```bash
    docker-compose build
    ```

7. Start the project using Docker Compose:

    ```bash
    docker-compose up
    ```

8. To automatically run pre-commit before each commit, install the pre-commit hooks with the following command:

 ```bash
    poetry run pre-commit install
 ```

9. To run pre-commit checks, use the following command:

    ```bash
    poetry run pre-commit run
    ```
