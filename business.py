import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')

    #print(df['states'].tolist())

    Countries        = df['Countries'].tolist()

    Companies         = df['Companies'].tolist()

    list_of_tuples = [tuple(row) for row in df.values]
  
    print(list_of_tuples)

    result_dict = {
        'Countries '            : Countries ,
        'Companies'             : Companies,
        'data_list'             : list_of_tuples
    }

    #print(result_dict)

    return result_dict

def add_row(Countries, Companies):

    df = pd.read_csv('data.csv') 

    new_row = {
    
        'Countries'        : Countries, 
        'Companies'        : Companies
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('data.csv')

if __name__ == "__main__":
     get_data()
