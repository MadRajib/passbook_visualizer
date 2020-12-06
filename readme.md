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
Will generate Report about all months from Jan to Dec **if present**

To get report a specific month
```bas$ 
python3 main.py -i path/to/passbook.pdf -m AUG
```

Result:
```bash
Expenses for the month of (AUG)
--------------------------------------
Food Expenses: 1500.0
+----+---------------------+----------------------------------------------------+--------+--------+----------+
|    |        Date         |                      Details                       | Debit  | Credit | Balance  |
+----+---------------------+----------------------------------------------------+--------+--------+----------+
| 85 | 2020-08-30 00:00:00 | - atm cash 6144 garchuk tinali2nd cd goreswar (pt) | 5555.0 |        | 47314.38 |
+----+---------------------+----------------------------------------------------+--------+--------+----------+


Shopping Expenses: 1840.0
+----+---------------------+----------------------------------+-------+--------+----------+
|    |        Date         |             Details              | Debit | Credit | Balance  |
+----+---------------------+----------------------------------+-------+--------+----------+
| 86 | 2020-08-27 00:00:00 |  amazon/utib/amazon@apl/you are  | 949.0 |        | 48809.38 |
| 91 | 2020-08-16 00:00:00 |  flipkart/yesb/fkrt@ybl/payment  | 266.0 |        | 50702.38 |
| 94 | 2020-08-11 00:00:00 | - sbipg su9103329939amazonmumbai | 625.0 |        | 51387.38 |
+----+---------------------+----------------------------------+-------+--------+----------+


Other Expenses: 1373.0
+----+---------------------+-------------------------------+-------+--------+----------+
|    |        Date         |            Details            | Debit | Credit | Balance  |
+----+---------------------+-------------------------------+-------+--------+----------+
| 87 | 2020-08-26 00:00:00 | billdesk/icic/billdesk.v/upi  | 47.0  |        | 49758.38 |
| 88 | 2020-08-26 00:00:00 | googlepay/utib/googlepay@/sol | 199.0 |        | 49805.38 |
| 89 | 2020-08-25 00:00:00 |  olacabs/utib/olacabs1@a/upi  | 203.0 |        | 50004.38 |
| 90 | 2020-08-22 00:00:00 |  kaushik/sbin/ksaikia40@/upi  | 500.0 |        | 50207.38 |
| 92 | 2020-08-16 00:00:00 | cashfree/yesb/cashfree@y/dona | 175.0 |        | 50963.38 |
| 93 | 2020-08-15 00:00:00 | euronetg/icic/euronetgpa/upi  | 249.0 |        | 51138.38 |
+----+---------------------+-------------------------------+-------+--------+----------+


---------------------------------------------------------------------------------
Food expenses: 1500.0 
Shopping expenses: 1840.0 
Other expenses: 1373.0
---------------------------------
Total expenses: 4713.0
```
## 1.3. Other Arguments
```bash
$ python3 main.py --help
usage: main.py [-h] [--input INPUT] [--month {JAN,FEB,MAR,APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DEC}]

Genrate Visualizations of Expenses

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        input path of the passbook
  --month {JAN,FEB,MAR,APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DEC}, -m {JAN,FEB,MAR,APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DEC}
                        Get desired month expenses
```
