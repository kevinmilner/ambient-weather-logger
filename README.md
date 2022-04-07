# ambient-weather-logger

Python script to log data from an ambient weather personal weather station to CSV files. Requires that [ambient_api](https://github.com/avryhof/ambient_api) is installed and applicable environmental variables are set. The output will append a CSV file for each sensor in the given output directory with the most recent reading, and will not filter out duplicates.

Usage: `ambient-weather-logger.py <output-dir>`

