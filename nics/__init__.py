import argparse


def main():

    parser = argparse.ArgumentParser(
        # prog=SOFTWARE_DIST_NAME,
        usage=(
            '\n'
            '├─ %(prog)s run                play around\n'
            '├─ %(prog)s train              train and watch the network\n'
            '├─ %(prog)s edit               view, create, or delete datasets\n'
            '├─ %(prog)s settings           open app\'s settings\n'
            '├─ %(prog)s download datasets  download the latest datasets from the app\'s repo\n'
            '├─ %(prog)s download network   download the trained network from the app\'s repo\n'
        ),
        formatter_class=argparse.RawTextHelpFormatter  # to use line breaks (\n) in the help message
    )

    args = parser.parse_args()