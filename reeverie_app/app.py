from flask import Flask, request, abort
from app import create_app
import os

# Import the function to send a message to GPT-3.5
from reeverie.llm import ask_gpt

app = create_app()


@app.route("/webhook", methods=["POST"])
def webhook():
    # Ensure there is JSON data and it has the expected fields
    if not request.json or not "events" in request.json:
        abort(400)

    events = request.json["events"]

    # Process each event
    for event in events:
        # Check if the event is a message and is text
        if event["type"] == "message" and event["message"]["type"] == "text":
            user_message = event["message"]["text"]

            # Here we'll send the message to GPT-3.5 and get a response
            gpt_response = ask_gpt(user_message)

            # Logic to reply to the user using the LINE Messaging API
            # You'll need to implement this using your LINE bot credentials
            # For example: line_bot_api.reply_message(...)
            print(f"Responding with: {gpt_response}")

    return "OK", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
