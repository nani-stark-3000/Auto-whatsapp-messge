# Auto-whatsapp-message
WhatsApp Auto-Responder

## Description
This is a simple Flask web application that allows you to automate sending messages on WhatsApp. When you submit the phone number, count, and delay time, the program sends a "hello" message to the phone number on WhatsApp, and then types a random message from a pre-defined list of messages at the specified interval for the specified number of times. 

## Installation
1. Clone the repository
2. Install the required packages using the following command:
   ```
   pip install -r requirements.txt
   ```
3. Run the application using the following command:
   ```
   python app.py
   ```
4. Open your web browser and go to http://localhost:34

## Usage
1. Enter the phone number to which you want to send the message.
2. Enter the number of times you want to send the message.
3. Enter the delay time (in seconds) between each message.
4. Click on the "Submit" button.

## Dependencies
- Flask
- pyautogui
- pywhatkit

