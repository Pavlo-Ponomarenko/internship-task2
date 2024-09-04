import configparser
from pymongo import MongoClient
from scripts.start_logs_pulling import start_logs_pulling
from scripts.VirtualMaschine import VirtualMaschine

def init_state():
    config = configparser.ConfigParser()
    config.read("config.properties")
    vms = (
        VirtualMaschine('sftp-1', config.get('virtual_maschines', 'port1')),
        VirtualMaschine('sftp-2', config.get('virtual_maschines', 'port2')),
        VirtualMaschine('sftp-3', config.get('virtual_maschines', 'port3'))
    )
    for vm in vms:
        start_logs_pulling(vm)
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    return db