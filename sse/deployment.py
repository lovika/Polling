import time


def start_deployment(log_file_path):
    log_lines = [
        "Starting deployment...",
        "Pulling Docker image...",
        "Docker image pulled successfully",
        "Creating containers...",
        "Running database migrations...",
        "Waiting",
        "Hello there",
        "Welcome to server sent events demo",
        "This is a prototype",
        "Lorem ipsum dolor sit amet",
        "Lorem ipsum dolor sit amet",
        "Ipsum dolor sit amet",
        "Dolor sit amet",
        "abcdefghijklmnop",
        "abcdefghijklmnop",
        "qwertyuiop",
        "qwertyuiop",
        "zxcvbnm",
        "zxcvbnm",
        "asdfghjkl",
        "asdfghjkl",
        "asdfghjkl",
        "asdfghjkl",
        "Hello there",
        "Welcome to server sent events demo",
        "This is a prototype",
        "Lorem ipsum dolor sit amet",
        "Lorem ipsum dolor sit amet",
        "Ipsum dolor sit amet",
        "Dolor sit amet",
        "Hello there",
        "Welcome to server sent events demo",
        "This is a prototype",
        "Lorem ipsum dolor sit amet",
        "Lorem ipsum dolor sit amet",
        "Ipsum dolor sit amet",
        "Dolor sit amet",
        "Hello there",
        "Welcome to server sent events demo",
        "This is a prototype",
        "Lorem ipsum dolor sit amet",
        "Lorem ipsum dolor sit amet",
        "Ipsum dolor sit amet",
        "Dolor sit amet",
        "Starting application...",
        "Health check passed",
        "Deployment successful 🎉"
    ]

    with open(log_file_path, "a") as log_file:
        for line in log_lines:
            print(line)
            log_file.write(line + "\n")
            log_file.flush()
            time.sleep(2)