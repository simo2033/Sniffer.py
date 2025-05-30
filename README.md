## Network Sniffer in Python

Un semplice sniffer di rete creato con "scapy", utile per analizzare traffico TCP, UDP e ICMP in tempo reale.

## Funzionalità
- Cattura pacchetti IP in tempo reale
- Supporta TCP, UDP, ICMP
- Mostra IP sorgente/destinazione e porte
- Interfaccia a riga di comando

## Requisiti
- Python 3.7+
- scapy

Installa le dipendenze con:

## bash
pip install -r requirements.txt

## Esecuzione

sudo python sniffer.py

## Esempio di output

[12:35:17] TCP 192.168.1.5:54321 -> 172.217.22.14:443
[12:35:18] UDP 192.168.1.5:5353 -> 224.0.0.251:5353

