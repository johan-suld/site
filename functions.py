from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date, timedelta


def sql(sql_post):

    engine = create_engine('mssql+pyodbc://DESKTOP-L2L3JIS/JS?driver=SQL+Server+Native+Client+11.0')

    res = engine.execute(sql_post)

    res_list = []

    for i in res:
        string = str(i)
        string = string.replace("'", "").replace("(", "").replace(")", "")
        res_list.append(string.rsplit(', ', 1))

        res_list2 = [['a', '1'], ['b', '10'], ['c', '100'], ['d', '1000'], ['e', '10000'], ['f', '100000'], ['g', '1000000']]

# tusenavgränsare
        for j in res_list:
            if j[1] != 'None' and len(j[1]) > 3:
                y = len(j[1]) % 3
                x = j[1][:y] + " " + j[1][y:y+3] + " " + j[1][y+3:y+6] + " " + j[1][y+6:y+9] if y != 0 else \
                    j[1][y:y+3] + " " + j[1][y+3:y+6] + " " + j[1][y+6:y+9]
                #print(x)
            else:
                pass

    return res_list


#sql_list = sql("SELECT Title, Pageviews FROM WIKI WHERE DATE = '2021-05-01' ORDER BY Pageviews")
#print(sql_list)


def sql_log(timestamp, date_input, result):
    engine = create_engine('mssql+pyodbc://DESKTOP-L2L3JIS/JS?driver=SQL+Server+Native+Client+11.0')
    engine.execute("INSERT INTO WIKI_LOG(Timestamp, Date_input, Result) VALUES('" + timestamp + "', '" + date_input +
                   "', " + str(result) + ")")

