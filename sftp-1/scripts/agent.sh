#!/bin/bash

MONITOR_DIR="/home/sftp/uploads"
LOG_FILE="/home/sftp/logfile.log"

inotifywait -m -e create --format '%f %T' --timefmt '%Y-%m-%d %H:%M:%S' "$MONITOR_DIR" | while read FILENAME TIME
do
    # Get the file owner (user who created the file)
    USER=$(stat -c '%U' "$MONITOR_DIR/$FILENAME")

    # Log the date, file name (without path), and user who created it
    echo "$TIME - File created: $FILENAME by $USER" >> "$LOG_FILE"
done