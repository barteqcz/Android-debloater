from subprocess import run
from sys import exit
import json
import os

def load_package_names_from_config():
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
            return config['package_names']
    except json.JSONDecodeError as e:
        print(f"Error loading config.json: {e}")
        exit()

def create_default_config():
    default_config = {
        "package_names": {
            "com.android.chrome": "Google Chrome",
            "com.google.android.youtube": "YouTube",
            "com.google.android.apps.subscriptions.red": "Google One",
            "com.google.android.apps.tachyon": "Google Duo",
            "com.google.android.gm": "Gmail",
            "com.google.android.apps.photos": "Google Photos",
            "com.google.android.apps.maps": "Google Maps"
        }
    }
    with open('config.json', 'w') as config_file:
        json.dump(default_config, config_file, indent=4)
    print("Default config file 'config.json' created. Edit it to adjust it to your needs.")
    input("Press Enter to exit...")
    exit()

def setup_config():
    package_names = load_package_names_from_config()
    return package_names

def check_adb_exists():
    try:
        result = run(['adb', 'version'], capture_output=True, text=True)
        return True
    except FileNotFoundError:
        return False

def check_devices_connected():
    result = run(['adb', 'devices'], capture_output=True, text=True)
    output = result.stdout.strip().split('\n')[1:]
    devices = [line.split('\t')[0] for line in output if line.strip()]
    
    if 'unauthorized' in result.stdout.lower():
        print("Connected device is not authorized. Please accept the USB debugging authorization on the device.\n")
    
    return bool(devices)

def uninstall_app(package_id):
    package_name = package_names.get(package_id, package_id)
    while True:
        response = input(f"Do you want to uninstall {package_name}? [Y/n] ")
        if response == '' or response.lower() == 'y':
            print(f"Uninstalling {package_name}...")
            run(['adb', 'shell', 'pm', 'uninstall', '--user', '0', package_id])
            break
        elif response.lower() == 'n':
            print("Skipping...")
            break
        else:
            print("Invalid input")

if not os.path.exists('config.json'):
    create_default_config()

package_names = setup_config()

try:
    if not check_adb_exists():
        print("ADB is not installed or not accessible. Please make sure ADB is installed and added to the system's PATH.")
        input("Press Enter to exit...")
        exit()

    if not check_devices_connected():
        print("No devices found. Please connect a device and try again.")
        input("Press Enter to exit...")
        exit()    

    for package_id in package_names:
        uninstall_app(package_id)

    input("Finished! Press Enter to exit...")
    exit()

except KeyboardInterrupt:
    exit()
