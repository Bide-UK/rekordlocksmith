
# RekordLocksmith
![Logo](images/logo.png)

This tool was developed with the ethos that users should have unfettered access to their own music libraries. If you're looking to make changes to your Rekordbox library, you shouldn't have to navigate through intentionally placed barriers such as encrypted databases and obfuscated keys. 


## Prerequisites

Before using RekordLocksmith, ensure that you meet the following requirements:

- **LLDB**: The LLVM Debugger must be installed on your system. LLDB is part of the LLVM suite and is usually included with Xcode on macOS.
- **Rekordbox**: The Rekordbox application should be installed on your system. This tool is tested with specific versions of Rekordbox, so compatibility may vary across different versions.
- **Disable SIP (System Integrity Protection)**: On macOS, System Integrity Protection must be disabled to allow RekordLocksmith to interact with Rekordbox's process memory. Disabling SIP can pose a security risk, so proceed with caution and re-enable SIP after using the tool.

## Usage

To use RekordLocksmith, run the script with the path to the Rekordbox binary as an argument. Here's an example command:

```bash
python3 rekordlocksmith.py /Applications/rekordbox\ 6/rekordbox.app/Contents/MacOS/rekordbox
```

## Getting Started

Follow these steps to set up RekordLocksmith:

1. **Install LLDB**:
   - LLDB can be installed with Xcode on macOS via the App Store or xcode-cli-commands.
   - Ensure LLDB is accessible from the terminal by running `lldb` in the terminal.

2. **Disable SIP**:
   - Restart your Mac and hold down `Command-R` as it boots to enter Recovery Mode.
   - Open the Terminal from the Utilities menu.
   - Type `csrutil disable` and press Enter.
   - Restart your Mac.

3. **Download RekordLocksmith**:
   - Clone or download the RekordLocksmith repository from GitHub.

4. **Run RekordLocksmith**:
   - Use the terminal to navigate to the folder containing `rekordlocksmith.py`.
   - Run the script using the command shown in the Usage section above.

## Output

The tool will output the database key to the terminal and save it to a file named `rekordbox_db_pass.txt` in the current directory.

## Disclaimer

The use of RekordLocksmith is solely at the end user's risk. The author assumes no liability for any potential issues or damages that may arise. 

## Contributing

Contributions to RekordLocksmith are welcome. Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
