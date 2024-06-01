# Android-debloater

### About
This is a simple script, written in Python, which is supposed to safely remove bloatware from Android using `adb`.

### Important notice
I do not assume responsibility for any side effects resulting from the app. While it is designed to perform all functions safely and enables the removal of only a minimal portion of packages generally recognized as safe to delete, I cannot guarantee how a device will respond.

### Microsoft Defender finding threats in the app
Microsoft Defender and a few other antivirus programs might mistakenly identify this app as a virus. It's important to note that this app is not a virus and you can look up the whole code in this repo. The potential cause for this false detection could be related to the app's use of ADB (Android Debug Bridge).

### Preparing to run
Before running the script, make sure that you're phone is connected to the PC via USB cable, the USB debugging is enabled in the settings, and if you authorized your PC to use USB debugging with your phone. You can check if your phone is being detected, by using `adb devices`.
<br>
On Debian-based distros, you can install `adb` using `sudo apt install adb`.
<br>
On Arch-based distros, you can install `adb` using `sudo pacman -S android-tools`
<br>
On Windows, you'll have to manually download `adb` software and usb android drivers.
<br>

While running the script for the first time, it will create the `config.json` file. you can modify the file, to include as many packages as you want.

#### Enabling usb debugging in Hyper OS
To enable USB debugging, firstly you have to enable developer options. To do that, go to settings > about phone and click 7 times on "OS version". Then, go back to the settings main page, and go to advanced settings. Scroll down, and you should see developer options. Open developer options, and scroll down to "USB debugging" option. Enable it.

### Running

#### Linux
Just download the file from the releases page, run `./debloater` on your Linux distro.
<br>
WARNING! Don't run the file by doubleclicking it, since it won't start in CLI mode, and you won't be able to do anything, but the program will be running in the background.

#### Windows
Just download the .exe file from the releases page, and run it.

### Troubleshooting
In case you're getting some errors on Linux, check whether 'adb' is installed, and whether the user you're using to run this script is inside a Linux `plugdev` group. In case it isn't, you can add your user to this group by running `sudo usermod -aG plugdev username`.

If such a group doesn't exist, you can also try rebooting the system.
