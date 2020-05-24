import pandas as pd
import random
from datetime import datetime,timedelta
'''
datetime
object
class
midx,midy
robot alloted
Pickup_time
'''
waste_categories = ['Aluminium_cans','plastic_wrappers','Cardboard','Paper','PET','PVC','LDPE','HDPE']
df = pd.read_csv('./robot_waste_categories.csv')
'''
print(df)

working_robots = (df.columns[df.isin( ['{0}'.format()] ).any()])
'''
def assign_robot_to_detected_waste(waste_type):
    working_robots = (df.columns[df.isin( ['{0}'.format(waste_type)] ).any()])
    total_robots = len(working_robots)
    select_robot = random.randint(1,total_robots)
    robot_name = working_robots[select_robot-1]
    return robot_name

def create_date_time_list(day,current_datetime):
    random_sec_inc = random.randint(1,59)
    current_datetime = current_datetime + timedelta(seconds=random_sec_inc)
    return current_datetime

def main():
    data_time_col = []
    waste_object_col = []
    robot_col = []
    date_list = ['day_bf_yest','yesterday','today']
    now = datetime.now()
    yesterday = now - timedelta( days=1 )
    dbf_yesterday = now - timedelta( days=2 )
    for i in range(1000):
        if i<=333:
            if i==0:
                date = create_date_time_list(date_list[0],dbf_yesterday)
                data_time_col.append(date)
            else:
                date = create_date_time_list( date_list[0], date )
                data_time_col.append( date )
        elif 333<i<=666:
            if i==334:
                date = create_date_time_list(date_list[1],yesterday)
                data_time_col.append(date)
            else:
                date = create_date_time_list( date_list[1], date )
                data_time_col.append( date )
        elif 666<i<=1000:
            if i==667:
                date = create_date_time_list(date_list[2],now)
                data_time_col.append(date)
            else:
                date = create_date_time_list( date_list[2], date )
                data_time_col.append( date )

    for i in range( 1000 ):
        random_waste_category = random.randint( 0, 7 )
        waste_name = waste_categories[random_waste_category]
        waste_object_col.append(waste_categories[random_waste_category])
        robot_name = assign_robot_to_detected_waste(waste_name)
        robot_col.append(robot_name)

    wi_robot_table = {
        'date_time':data_time_col,
        'waste_type':waste_object_col,
        'robot_name':robot_col
    }
    df = pd.DataFrame(wi_robot_table)
    df.to_csv('wi_robot_table_v1.csv')
if __name__ == '__main__':
    main()