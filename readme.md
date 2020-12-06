- [1. Passbook Visualizer](#1-passbook-visualizer)
  - [1.1. Install the required packages](#11-install-the-required-packages)
  - [1.2. Run the Program](#12-run-the-program)
  - [1.3. Other Arguments](#13-other-arguments)

# 1. Passbook Visualizer

## 1.1. Install the required packages

[Optional]Create a Virtual Environment 
```bash
$ python3 -m virutalenv venv 
```
Install the Required Packages
```
$pip3 install -r requirements.txt
```

## 1.2. Run the Program
```bash
$ python3 main.py -i path/to/passbook.pdf 
```
## 1.3. Other Arguments
```bash
$ python3 main.py --help
usage: main.py [-h] [--input INPUT] [--month MONTH]

Genrated Visualizations of Expenses

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        input path of the passbook
  --month MONTH, -m MONTH
                        Get desired month expenses
```
