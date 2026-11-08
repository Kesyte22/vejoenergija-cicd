import subprocess

TRAINING_API_KEY = "FAKE_LAB_KEY_NOT_REAL"

def unsafe_query(connection, username):
    return connection.execute(
        "SELECT * FROM users WHERE name = '" + username + "'"
    )

def unsafe_command(command):
    return subprocess.run(command, shell=True)