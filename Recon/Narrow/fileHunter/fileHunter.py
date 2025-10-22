import json
import argparse
import datetime
from datetime import timedelta

#Argparse configs
project_root="/home/mehranowsky/Public/Tools/Customs/JimmyNeutron/Recon/Narrow/fileHunter/"
parser = argparse.ArgumentParser()
parser.add_argument("-d",required=True, type=str,default=None, help="The target domain name")
parser.add_argument("-dm", action="store_true", help="Date mode")
parser.add_argument("-w",required=True, type=str, help="Wordlist")
args = parser.parse_args()

# Domains
full_domain = args.d
domain_name = full_domain.rsplit('.', 2)[-2]
subdomain = full_domain.rsplit('.', 2)[0]

# Load the extensions and wordlist
with open(f'{project_root}configs/exts.json', 'r') as file:
    exts = json.load(file)['exts']    
with open(f'{project_root}{args.w}','r') as file:
    wordlist = json.load(file)['word']
 
# Appending to the list
bkFileList = []
def listAppend(w):
    bkFileList.append(w)

# Generating the list
def gen_list():
    for word in wordlist:
        listAppend(f".{word}")    
        for ext in exts:
            listAppend(f".{word}.{ext}")
            listAppend(f".{domain_name}.{ext}")
            listAppend(f"{word}.{ext}")
            listAppend(f"{domain_name}.{ext}")
            listAppend(f"{full_domain}.{ext}")
            listAppend(f"{subdomain}.{ext}")
            for num in range(0,10):            
                listAppend(f"{word}.{ext}.{num}")
                listAppend(f".{word}.{ext}.{num}")
                listAppend(f"{word}.{num}.{ext}")
                listAppend(f"{domain_name}.{num}.{ext}")
                listAppend(f"{full_domain}.{num}.{ext}")
                listAppend(f"{subdomain}.{num}.{ext}")
                listAppend(f"{domain_name}{num}.{ext}")
        for num in range(0,10):
            listAppend(f"{word}.{num}")
            listAppend(f".{word}.{num}")

# Generate the date mode wordlist
def gen_date():
    today = datetime.date.today()
    date_format = [
        "%y%m%d",
        "%y-%m-%d"
    ]
    # Iterate over the last 6 months
    for i in range(30):  # Approximately 6 months (30 days * 6)
        date = today - timedelta(days=i)
        for pattern in date_format:
            formatted_date = date.strftime(pattern)
            for ext in exts:
                listAppend(f"{domain_name}.{formatted_date}.{ext}")
                listAppend(f"{subdomain}.{formatted_date}.{ext}")
                for word in wordlist :
                    listAppend(f"{word}.{formatted_date}.{ext}")

# Print the list
def show_list() :
    for word in bkFileList:
        print(word)

gen_list()
if args.dm:
    gen_date()
show_list()