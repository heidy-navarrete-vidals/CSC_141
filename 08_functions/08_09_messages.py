def show_messages(messages):
    """Print messages from a list."""
    for message in messages:
        msg = f"{message}"
        print(msg)



messages = ['hi', 'goodbye', 'how are you?', 'see you there!']
show_messages(messages)