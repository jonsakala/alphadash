# AlphaDash

AlphaDash is a simple Python program designed to synchronize your system's time with internet atomic clocks, ensuring accurate timekeeping on Windows systems.

## Features

- Retrieves current time from an NTP server (`pool.ntp.org`).
- Updates the system clock on Windows with the retrieved time.
- Ensures precise system time, which is crucial for time-sensitive applications and logging.

## Requirements

- Python 3.x
- ntplib library

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/AlphaDash.git
   cd AlphaDash
   ```

2. **Install the required Python package:**

   ```bash
   pip install ntplib
   ```

## Usage

Run the program using Python:

```bash
python AlphaDash.py
```

## Note

- AlphaDash is designed to work on Windows systems only. It uses PowerShell commands to set the system time, which might require administrative privileges.
- Ensure that your system has internet access to retrieve the time from the NTP server.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This software is provided "as-is" without any warranties. Use it at your own risk.