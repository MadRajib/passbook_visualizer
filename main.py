from decypt import decrypt
import parser as pr
import json
import os
import argparse as arg


def main():
    argparser = arg.ArgumentParser(description="Genrate Visualizations of Expenses")
    argparser.add_argument("--input","-i",help="input path of the passbook")
    argparser.add_argument("--month","-m",choices=pr.MONTHS,help="Get desired month expenses")



    args = argparser.parse_args()
    if not args.input:
        print("Provide a Input File!")
        return
    
    password = str(input("Enter passbook password :"))
    
    decrypt(args.input,password)
    pdf_data = pr.parse_pdf_file("decrypted.pdf")

    os.remove("decrypted.pdf")

    debit_transactions =  pr.extract_debit_transactions(pdf_data)

    df = pr.get_dataFrame(debit_transactions)
    
    if args.month:
        pr.get_month_expenses(df,args.month)
    else:
        pr.get_all_expenses(df)



if __name__ == "__main__":
    main()