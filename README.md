Binance Gift Card Creator

This application provides a simple GUI interface to create gift cards using the Binance API. It allows users to select a token, input an amount, and generate a gift card. Additionally, it displays the user's spot balances from their Binance account.
Features

    API Key Management: Users can input their Binance API key and secret for authentication.
    Token Selection: Users can select a token from a dropdown list of available tokens.
    Amount Input: Users can specify the amount for the gift card.
    Gift Card Creation: On submission, the application interacts with the Binance API to create a gift card.
    Balance Display: The application fetches and displays the user's spot balances from their Binance account.
    Error Handling: Proper error messages are displayed for issues like insufficient balance or API errors.

Setup

    Ensure you have Python installed.
    Install the required packages:

    bash

    pip install binance-python

    Clone this repository or download the source code.
    Run api_generator.py to input and save your Binance API key and secret.
    Run main.py to launch the Binance Gift Card Creator application.

Usage

    Select a token from the dropdown list.
    Input the desired amount for the gift card.
    Click on "Create Gift Card". If successful, a confirmation message will be displayed.
    Check your spot balances by looking at the displayed list or by clicking the "Refresh Balances" button.

Notes

    Ensure you have the necessary permissions to read/write to the directory where the application is stored, especially for the keys.txt file which stores the API keys.
    Always keep your API keys secure. Do not share the keys.txt file.

This is a basic README. Depending on the actual scope and features of your application, you might want to expand on certain sections, add screenshots, or provide more detailed setup and usage instructions.
