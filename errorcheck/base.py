import sqlite3

connection = sqlite3.connect('network_data.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS network_stats
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  machine_name TEXT,
                  network_configuration TEXT,
                  rx_errors INTEGER,
                  tx_errors INTEGER)''')

def insert_network_stats(machine_name, network_configuration, rx_errors, tx_errors):
    cursor.execute("INSERT INTO network_stats (machine_name, network_configuration, rx_errors, tx_errors) VALUES (?, ?, ?, ?)",
                   (machine_name, network_configuration, rx_errors, tx_errors))
    connection.commit()