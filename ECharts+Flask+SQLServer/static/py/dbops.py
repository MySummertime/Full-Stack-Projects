
import pyodbc
import pandas as pd
import os


# path of info file
dir = os.path.dirname(__file__)
dir = os.path.join(dir, 'db_info.txt')


# Read from .txt to pandas.DataFrame
df = pd.read_csv(dir, encoding = 'utf-8', engine = 'python', header = None, sep = '\t')
# print(df)
# print(df.info())
# print(df.loc[0])

driver = 'SQL Server'
server = df.loc[0][0].strip()
database = df.loc[0][1].strip()
username = df.loc[0][2].strip()
password = df.loc[0][3].strip()


c = 'DRIVER={' + driver + '};SERVER=' + server + ';DATABASE=' + database + \
    ';UID=' + username + ';PWD=' + password
q = "a query statement"

def fetchData():
    conn = pyodbc.connect(c)

    cursor = conn.cursor()
    cursor.execute(q)

    # Read res into List
    ans = []
    for i in cursor:
        ans.append(i)
    #print(ans)

    '''
    # Read res into pandas DataFrame
    df = pd.read_sql_query(q, conn)
    print(df)
    print(type(df))
    '''

    conn.close()
    return ans




