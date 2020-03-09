import sys
import os

here = os.path.abspath(__file__)
sys.path.insert(0, os.path.dirname(os.path.dirname(here)))

from lof.examples import pred_ntf_oil


def main(*argv):
    for code in ["SH501018", "SZ160216", "SZ162411"]:
        pred_ntf_oil(code, token=argv[1])


if __name__ == "__main__":
    main(*sys.argv)
