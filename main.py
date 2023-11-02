import pandas as pd

file_name = "car_evaluation.data"

df = pd.read_csv(file_name, header=None)

def calculateProbability(case, condition, number_of_column):
    case_under_condition_sum = 0
    condition_sum = 0

    for element in df.itertuples():
        if element[7] == condition:
            condition_sum += 1
            if element[number_of_column+1] == case:
                case_under_condition_sum += 1

    if case_under_condition_sum == 0:
        case_under_condition_sum = 1
        condition_sum += df[number_of_column+1].nunique()

    return case_under_condition_sum / condition_sum

while True:
    try:
        input_message = input("Input values (comma-separated): ")
        values = input_message.split(',')

        vector = [values[0], values[1], values[2], values[3], values[4], values[5]]

        lables_array = df[6].unique()
        print(lables_array)
        probability_array = [1] * lables_array.size

        for x in range(lables_array.size):
            for i in range(6):
                probability_array[x] *= calculateProbability(vector[i], lables_array[x], i)

        indeks_max = probability_array.index(max(probability_array))
        print("Decision:", lables_array[indeks_max])

    except Exception as e:
        print(f"Error: {e}")
