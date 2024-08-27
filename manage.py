from app import create_app
import os
import sys
from config import BASE_DIR
import logging

app = create_app(os.environ.get("FLASK_CONFIG", "default"))


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    import coverage

    cov = coverage.Coverage()

    cov.erase()

    cov.start()

    tests = unittest.TestLoader().discover("tests")
    results = unittest.TextTestRunner(verbosity=2).run(tests)

    cov.stop()
    cov.save()

    cov.report()

    cov.html_report(directory="tests/coverage_html")

    total_coverage = cov.report()

    if not results.wasSuccessful():
        sys.exit(1)

    if total_coverage < 80:
        logging.error("Coverage is less than 90%")
        sys.exit(1)


@app.cli.command()
def install_hooks():
    import stat
    import platform
    import shutil
    
    """Register local repo github hooks"""

    files = os.listdir(os.path.join(BASE_DIR, "hooks"))

    file_permissions = (
        stat.S_IRUSR |
        stat.S_IWUSR |
        stat.S_IXUSR |
        stat.S_IRGRP |
        stat.S_IWGRP |
        stat.S_IXGRP
    )

    for file in files:
        symlink_path = os.path.join(BASE_DIR, f".git/hooks/{file}")
        file_path = os.path.join(BASE_DIR, f"hooks/{file}")

        if os.path.islink(symlink_path):

            logging.info(f"{file}: aready installed. skiping...")

            continue

        os.chmod(file_path,file_permissions)

        try:

            match platform.system().lower():

                case "linux":

                    if os.path.splitext(file_path)[-1] in (".bat",".ps1"):
                        continue

                    os.symlink(file_path, symlink_path)

                case "windows":

                    shutil.copy(file_path, symlink_path)

                case _:

                    logging.error(f"Unsupported platform: {platform.system()}")

        except OSError as error:

            logging.error(f"Failed to create symlink for {file}: {error}")

    logging.info("Hooks installed")


@app.cli.command()
def uninstall_hooks():

    import platform

    """Unregister local repo github hooks"""

    files = os.listdir(os.path.join(BASE_DIR, ".git/hooks"))

    for file in files:

        path = os.path.join(BASE_DIR, f".git/hooks/{file}")

        if os.path.splitext(path)[-1] in (".sample",):
            continue

        match platform.system().lower():

            case "linux":

                if os.path.islink(path):

                    try:

                        os.unlink(path)

                    except OSError as error:

                        logging.error(f"Failed to remove symlink for {file}: {error}")

                    logging.info(f"{file}: uninstalled")

            case "windows":

                os.remove(path)

            case _:

                logging.error(f"Unsupported platform: {platform.system()}")
