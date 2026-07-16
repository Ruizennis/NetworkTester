import argparse
import sys
import shutil
import logging
import subprocess
from importlib.metadata import version, PackageNotFoundError

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
    parser = argparse.ArgumentParser(
        description="Basic Network tester in cli tool form."
    )
    config_flags = parser.add_argument_group("Configuration")
    misc_flags = parser.add_argument_group("Miscellaneous flags")
    misc_flags.add_argument(
        "-V",
        "--version",
        action="store_true",
        help=("Shows installed NetworkTestCli package version and exits"),
    )
    config_flags.add_argument(
        "-I",
        "--ip",
        action="store",
        help=("Used to set a custom ip to use instead of the default 1.1.1.1"),
    )
    config_flags.add_argument(
        "-P",
        "--force-ping",
        action="store_true",
        help=("Forces ping to be used instead of checking automatically"),
    )
    config_flags.add_argument(
        "-N",
        "--gping-noclear",
        action="store_true",
        help=("Removes the clear flag when using gping.")
    )
    args = parser.parse_args()

    if args.version:
        try:
            package_version = version("NetworkTestCli")
            print(package_version)
            sys.exit(0)
        except PackageNotFoundError:
            logger.error(
                "Error: Pip package not found. To resolve this error, "
                "please install the package from PyPI with: "
                "pip install NetworkTestCli"
            )
            sys.exit(1)
    if args.force_ping:
        ping_type = "ping"
    else:
        if shutil.which("gping"):
            ping_type = f"gping"
        else:
            ping_type = "ping"
    command = [ping_type]
    if ping_type == "gping" and not args.gping_noclear:
        command.append("--clear")
    if not args.ip:
        ping_ip = "1.1.1.1"
    else:
        ping_ip = args.ip
    command.append(ping_ip)
    
    # end of flag checking logic

    
    try:
        subprocess.run(command, check=True)
    except FileNotFoundError:
        print(f"{ping_type} not installed.")
    except subprocess.CalledProcessError:
        print("Check your connection.")
    except KeyboardInterrupt:
        print('Exiting..')
    if not len(sys.argv) > 1:
        print('Tip: If you wanted to see flags use the -h flag.')

if __name__ == "__main__":
    main()