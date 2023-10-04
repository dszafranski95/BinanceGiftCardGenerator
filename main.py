import csv
import time
from tkinter import *
from tkinter import messagebox
from binance.spot import Spot as Client
from binance.error import ClientError, ServerError
from tkinter import ttk

def save_to_csv(data):
    with open('my_card.csv', mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def create_gift_card():
    token_choice = token_entry.get()
    amount = amount_entry.get()

    if not token_choice:
        messagebox.showerror("Error", "Please select a token")
        return

    if not amount:
        messagebox.showerror("Error", "Please enter an amount")
        return

    params = {
        'token': token_choice,
        'amount': float(amount)
    }

    # Check if there is enough balance
    for coin in spot_coins:
        if coin['asset'] == params['token']:
            available_balance = float(coin['free'])
            if available_balance >= params['amount']:
                MAX_RETRIES = 1
                retry_count = 0

                while retry_count < MAX_RETRIES:
                    try:
                        response = client.gift_card_create_code(**params)
                        save_to_csv([params['token'], params['amount'], response])
                        messagebox.showinfo("Success", f"Gift Card created: {response}")
                        break
                    except ClientError as e:
                        messagebox.showerror("Error", str(e))
                    except ServerError as e:
                        if retry_count < MAX_RETRIES - 1:
                            time.sleep(5)  # Wait for 5 seconds before retrying
                        else:
                            messagebox.showerror("Error", "An internal server error occurred. Please try again later.")
                    retry_count += 1
            else:
                messagebox.showerror("Error", "Insufficient balance")
            break

def get_api_keys():
    with open('keys.txt', 'r') as f:
        api_key = f.readline().strip()
        api_secret = f.readline().strip()
    return api_key, api_secret

def exit_program():
    root.quit()

def ask_exit():
    if messagebox.askyesno("Exit", "Are you sure you want to close the program?"):
        root.quit()

def get_margin_account_balances():
    margin_account_info = client.margin_account()
    margin_coins = [{'asset': asset['asset'], 'free': asset['free'], 'netAsset': asset['netAsset']} for asset in margin_account_info['userAssets'] if float(asset['netAsset']) > 0]
    return margin_coins

def display_balances():
    balances_listbox.delete(0, END)
    
    # Get spot balances
    spot_balances = client.account()['balances']
    spot_coins = [{'asset': asset['asset'], 'free': asset['free']} for asset in spot_balances if float(asset['free']) > 0]

    for coin in spot_coins:
        balances_listbox.insert(END, f"{coin['asset']}: Spot: {coin['free']}")

        
def get_funding_wallet_balances():
    try:
        funding_wallet = client.sapi_v1_account_snapshot(type='SPOT')['snapshotVos'][-1]['data']['balances']
        funding_coins = [{'asset': asset['asset'], 'free': asset['free']} for asset in funding_wallet if float(asset['free']) > 0]
    except Exception as e:
        print("Error getting funding wallet balances:", e)
        funding_coins = []
    return funding_coins

# initialize client
api_key, api_secret = get_api_keys()

client = Client(api_key, api_secret)

symbols = client.exchange_info()['symbols']
symbols_list = []
seen_base_assets = set()

for symbol in symbols:
    if symbol['status'] == 'TRADING' and symbol['quoteAsset'] == 'USDT':
        seen_base_assets.add(symbol['baseAsset'])

symbols_list = sorted(list(seen_base_assets))

# Get spot balances
spot_balances = client.account()['balances']
spot_coins = [{'asset': asset['asset'], 'free': asset['free']} for asset in spot_balances if float(asset['free']) > 0]

# Create the main window
root = Tk()
root.title("Binance Gift Card Creator")
root.geometry("800x600")
root.protocol("WM_DELETE_WINDOW", ask_exit)

# Configure grid weights
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)

# Token Label and Entry
token_label = Label(root, text="Token")
token_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

token_entry = ttk.Combobox(root, values=symbols_list)
token_entry.grid(row=0, column=1, padx=5, pady=5, sticky=EW)

# Amount Label and Entry
amount_label = Label(root, text="Amount")
amount_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

amount_entry = Entry(root)
amount_entry.grid(row=1, column=1, padx=5, pady=5, sticky=EW)

new_width = round(20 * 0.3)  # Reducing the width by 70%
create_gift_card_button = Button(root, text="Create Gift Card", command=create_gift_card, bg='green', width=new_width)
create_gift_card_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=EW)

# Balances Listbox
balances_listbox = Listbox(root)
balances_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=NSEW)

display_balances()

# Refresh Balances Button
refresh_balances_button = Button(root, text="Refresh Balances", command=display_balances, bg='green', width=new_width)
refresh_balances_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky=EW)
# Run the main loop
root.mainloop()
