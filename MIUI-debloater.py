from subprocess import run
from sys import exit

package_names = {
    "com.miui.player": "Mi Music",
    "com.miui.videoplayer": "Mi Video",
    "com.mi.globalbrowser": "Mi Browser",
    "com.xiaomi.glgm": "Xiaomi Game Center",
    "com.android.mms": "Xiaomi SMS app"
}

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
        response = input(f"Do you wanna uninstall {package_name}? [Y/n] ")
        if response == '' or response.lower() == 'y':
            print(f"Uninstalling {package_name}...")
            run(['adb', 'shell', 'pm', 'uninstall', '--user', '0', package_id])
            break
        elif response.lower() == 'n':
            print("Skipping...")
            break
        else:
            print("Invalid input")

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
