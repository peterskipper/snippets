import logging
import csv

#Set the log output file, and the log level
logging.basicConfig(filename="output.log",level=logging.DEBUG)

def put(name, snippet, filename):
    """
    Store a snippet with an associated name in the CSV file
    """
    logging.info("Writing {}:{} to {}").format(name, snippet, filename)
    logging.debug("Opening file")
    with open(filename, 'ab') as output:
        writer = csv.writer(output, delimiter=',')
        logging.debug("Writing snippet to file")
        writer.writerow([name,snippet])
    logging.debug("Write successful")
    return name, snippet

