import time
import threading
from pymongo import MongoClient

def parse_logs(logs, server_name):
    result = []
    for line in logs.split('\n'):
        if line != '':
            record = dict()
            words = line.split(' ')
            record['file'] = words[5]
            record['time'] = words[0] + ' ' + words[1]
            if 'sftp-1' in  words[5]:
                record['sender'] = 'sftp-1'
            elif 'sftp-2' in  words[5]:
                record['sender'] = 'sftp-2'
            elif 'sftp-3' in  words[5]:
                record['sender'] = 'sftp-3'
            result.append(record)
    return result

def pulling_process(vm):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db[vm.name]
    while True:
        logs = vm.pull_logs()
        parsed_logs = parse_logs(logs, vm.name)
        if len(parsed_logs) != 0:
            collection.insert_many(parsed_logs)
        time.sleep(300)

def start_logs_pulling(vm):
    process = threading.Thread(target=pulling_process, args=[vm])
    process.start()