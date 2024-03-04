#!/usr/bin/env python3
import sqlite3
import serial
from serial.tools import list_ports
from datetime import datetime


PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.1

# Database setup

# Establish a connection with the sqlite database at database.db this is nothing more than a file
con = sqlite3.connect("database.db")

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS water_intake(timestamp DATE PRIMARY KEY, waterconsumed int);""")

def find_comport(pid, vid, baud):
	# A simple function to find the port the microbit is running on if none is found it will return None.
	ser_port = serial.Serial(timeout=0.1)
	ser_port.baudrate = baud
	ports = list(list_ports.comports())
	
	for p in ports
		if p.pid == pid and p.vid == vid:
			print(f"Found target device: \n\tport: {p.device}")
			ser_port.port = str(p.device)
			return ser_port

	return None


def main():
	while (ser_micro := find_comport(PID_MICROBIT, VID_MICROBIT, 115200)) is None: pass; # keep looking for a microbit
	ser_micro.open()
	while True:
		inp = ser_micro.readline().decode('utf-8')
		match inp:
			case "":
				continue
			case _:
				cur.execute("REPLACE INTO water_intake VALUES (?, ?)", [datetime.utcnow().date().isoformat(), int(inp.strip().split(',')[1])])
				con.commit()

	


if __name__ == '__main__':
	main()





