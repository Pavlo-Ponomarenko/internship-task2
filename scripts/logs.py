def split_records(records, sender1, sender2):
    result1 = []
    result2 = []
    for record in records:
        if record['sender'] == sender1:
            result1.append({'file': record['file'], 'time': record['time']})
        elif record['sender'] == sender2:
            result2.append({'file': record['file'], 'time': record['time']})
    return result1, result2