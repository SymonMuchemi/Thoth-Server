#!/usr/bin/python3
import logging
import subprocess
import os
import platform

base_dir = os.path.abspath(os.path.dirname("app"))

logging.basicConfig(
    level=logging.DEBUG,
    format="[:] %(process)d - %(levelname)s - %(message)s"
)


def run_tests():

    logging.info("Running Application tests")

    if platform.system() == "Windows":
        subprocess.run(
            f"{base_dir}/env/Scripts/flask --app \
                {base_dir}/manage.py test".split(),
            check=True
        )
    else:
        subprocess.run(
            f"{base_dir}/env/bin/flask --app \
                {base_dir}/manage.py test".split(),
            check=True
        )


if __name__ == "__main__":

    run_tests()
