def send_messages(messages, sent_messages):
    """Print messages from a list."""
    while messages:
        current_message = messages.pop()
        print(f"\nCurrent Message: {current_message}")
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    """Show all the messages that were sent"""
    print("\nThe following messages have been sent:")
    for sent_message in sent_messages:
        print(sent_message)

messages = ['hi', 'goodbye', 'how are you?', 'see you there!']
sent_messages = []

# copy of my list
send_messages(messages[:], sent_messages)
show_sent_messages(sent_messages)

print(messages)