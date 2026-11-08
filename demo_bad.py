def safe_query(connection, username):
    return connection.execute(
        "SELECT * FROM users WHERE name = ?",
        (username,)
    )