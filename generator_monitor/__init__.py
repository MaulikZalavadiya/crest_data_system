from .generator import *
from .monitor import *
import argparse

parser = argparse.ArgumentParser(
                    description='monitor parser'
)
parser.add_argument('-i', '--interval', default=5)

parser_args = parser.parse_args()


def run():
    thread1 = threading.Thread(target=write_to_file, args=("output1.txt",))
    thread2 = threading.Thread(target=write_to_file, args=("output2.txt",))

    thread1.start()
    thread2.start()

    file_paths = ["output1.txt", "output2.txt"]
    monitor_files(file_paths, "CDS", int(parser_args.interval))
