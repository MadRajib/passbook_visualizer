from os import path
import re
from tika import parser
from tqdm import tqdm
import datetime
import pandas as pd
from tabulate import tabulate


MONTHS = {"JAN":[1,31],"FEB":[2,28],"MAR":[3,31],"APR":[4,30],"MAY":[5,31],"JUN":[6,30],"JUL":[7,31],"AUG":[8,31],"SEP":[9,30],"OCT":[10,31],"NOV":[11,30],"DEC":[12,31]}
SHOPPING_SERIES = pd.Series(['amazon','flipkart','myntra'])

# Regex to extract debit and credit transcations
debit_re = r"^(\d+\.\d{2})\s-?(\d+\s[A-Z]{3}\s\d{4})[\r\n]((.*?[\r\n])+?(?=(\d+\.\d+)))"
credit_re = r"^- (\d+\.\d{2})(\d+\s[A-Z]{3}\s[0-9]{4})[\r\n]((.*?[\r\n])+?(?=(\d+\.\d+)))"


# filter transcation details
RE_1 = r"^transfer\sto\s\d+\s-?[a-z]*\/[a-z*]*\/\d+\/(.*)"
RE_2 = r"^.*pos\d+([a-z]*\s\w+).*"

def parse_pdf_file(filename):
    if not path.exists(filename):
        raise FileNotFoundError()

    parsedPDF = parser.from_file("decrypted.pdf")


    # pre process data
    pdf = parsedPDF["content"]
    pdf = pdf.replace('\n\n', '\n')

    return pdf

# parse the data and extract the debit transaction 
def extract_debit_transactions(data):
    if data == "" or data == None:
        raise Exception("Empty Data")

    matches = re.finditer(debit_re, data, re.MULTILINE)


    debit_transactions = []
    print("Parsing Debit Transactions ...")
    for matchNum, match in tqdm(enumerate(matches, start=1)):
        
        groups = match.groups()
        data = {
            "Date":None,
            "Details":None,
            "Debit":None,
            "Credit":None,
            "Balance":None        
        }
        

        data["Date"] = datetime.datetime.strptime(groups[1].strip(), '%d %b %Y').strftime('%Y-%m-%d')

        
        data["Details"] = groups[2].replace('\n','').strip().lower()

        # Extract details of transaction having Transfer Words
        result = re.search(RE_1, data["Details"])
        if result:
            data["Details"] = result.group(1).strip()

        #Extract details of transactions having Pos word
        result = re.search(RE_2, data["Details"])
        if result:
            data["Details"] = result.group(1).strip()

        data["Debit"] = float(groups[0].strip())
        data["Balance"] = float(groups[-1].strip())

        debit_transactions.append(data)
    print("Successfully parsed Debit Transactions")

    return debit_transactions


# parse the data and extract the credit transaction 
def extract_credit_transactions(data):
    if data == "" or data == None:
        raise Exception("Empty Data")

    matches = re.finditer(credit_re, data, re.MULTILINE)


    credit_transactions = []
    print("Parsing Credit Transactions ...")
    for matchNum, match in tqdm(enumerate(matches, start=1)):
        
        groups = match.groups()
        data = {
            "Date":None,
            "Details":None,
            "Debit":None,
            "Credit":None,
            "Balance":None        
        }


        # data["Date"] = groups[1].strip()

        data["Date"] = datetime.datetime.strptime(groups[1].strip(), '%d %b %Y').strftime('%Y-%m-%d')

        data["Details"] = groups[2].strip().lower()
        data["Credit"] = float(groups[0].strip())
        data["Balance"] = float(groups[-1].strip())

        credit_transactions.append(data)
    print("Successfully parsed Credit Transactions")

    return credit_transactions

def get_dataFrame(json_data):
    df = pd.DataFrame(json_data)
    df['Date'] = pd.to_datetime(df["Date"])
    return df



def get_data_from(df,start_date,end_date):
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    return df.loc[mask]


# get expenseses from start to end date
def get_expenses(df,start_date,end_date):
    df = get_data_from(df,start_date,end_date)
    
    total_amount = df['Debit'].sum() 

    shoping_df = df[df['Details'].str.contains('amazon|flipkart|myntra|mmtcpamp')== True]
    shoping_amount =shoping_df['Debit'].sum() 


    food_df = df[df['Details'].str.contains('swiggy|zomato|atm|wine|dhaba')== True]
    food_amount = food_df['Debit'].sum()
    

    other_df = df[df["Details"].str.contains('amazon|flipkart|myntra|mmtcpamp|swiggy|zomato|atm|wine|dhaba') == False]
    other_amount = other_df['Debit'].sum()


    
    print(f"Food Expenses: {food_amount}")
    print(tabulate(food_df,headers = 'keys', tablefmt = 'pretty'))
    print("\n")
    

    print(f"Shopping Expenses: {shoping_amount}")
    print(tabulate(shoping_df,headers = 'keys', tablefmt = 'pretty'))
    print("\n")
    

    print(f"Other Expenses: {other_amount}")
    print(tabulate(other_df,headers = 'keys', tablefmt = 'pretty'))
    
    print("\n")
    
    print("---------------------------------------------------------------------------------")
    print(f"Food expenses: {food_amount} \nShopping expenses: {shoping_amount} \nOther expenses: {other_amount}")

    print("---------------------------------")
    print(f"Total expenses: {total_amount}")
    return total_amount

# get month expenses
def get_month_expenses(df,month,year=datetime.datetime.now().year):
    month = month.upper()
    if month not in MONTHS:
        print("Type Valid Month ex. January -> JAN")
        return
    detail = MONTHS[month]
    start_date = datetime.datetime(year,detail[0],1)
    end_date = datetime.datetime(year,detail[0],detail[1])

    print(f"Expenses for the month of ({month})")
    print("--------------------------------------")
    amount = get_expenses(df,start_date,end_date)
    
    return amount

def get_all_expenses(df):
    for m in MONTHS:
        get_month_expenses(df,m)