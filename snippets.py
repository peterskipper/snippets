import logging
import csv
import argparse
import sys

#Set the log output file, and the log level
logging.basicConfig(filename="output.log",level=logging.DEBUG)

def put(name, snippet, filename):
    """Store a snippet with an associated name in the CSV file"""
    logging.info("Writing {!r}:{!r} to {!r}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, 'a') as output:
        writer = csv.writer(output)
        logging.debug("Writing snippet to file")
        writer.writerow([name,snippet])
    logging.debug("Write successful")
    return name, snippet

def get(name, filename):
    """Retrieve snippet text from name and file"""
    logging.info("Reading {!r} from {!r}".format(name, filename))
    logging.debug("Opening file")
    with open(filename, 'r') as input:
        reader = csv.DictReader(input,fieldnames=["name","snippet"])
        found = False
        logging.debug("Reading file")
        for line in reader:
            if line["name"] == name:
                found = True
                return line["snippet"]
        if not found:
            print "The snippet {} cannot be found in the file {}.".format(name, filename)
            return "nothing."        


def make_parser():
    """Construct the command line parser"""
    logging.info("Constructing parser")
    description = "Store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description=description)

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    #Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of a snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    put_parser.add_argument("filename", default="snippets.csv", nargs="?", help="File where snippets are stored")

    #Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    get_parser.add_argument("name", help="The name of a snippet")
    get_parser.add_argument("filename", default="snippets.csv", nargs="?", help="File where snippets are stored")

    return parser

def main():
    """Main function"""
    logging.info("Starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print "Stored {!r} as {!r}". format(snippet, name)

    if command == "get":
        snippet = get(**arguments)
        print "Retrieved: " + snippet

if __name__ == '__main__':
    main()