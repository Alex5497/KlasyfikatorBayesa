import pandas as pd
import random

file_name = "car_evaluation.data"

df = pd.read_csv(file_name, header=None)
number_of_columns = df.shape[1]
last_index = number_of_columns - 1

number_of_parts = 5

data_list = df.values.tolist()
random.shuffle(data_list)
part_size = round(len(data_list) / number_of_parts)
parts = [data_list[i: i + part_size] for i in range(0, len(data_list), part_size)]

decision = []
good_predicted = 0

lables_array = df[number_of_columns - 1].unique()


def calculateProbability(training_set, vector):
    probability_array = [1] * lables_array.size

    # pętla odpowiadająca za warunek
    for condition in range(0, len(lables_array)):
        # pętla odpowiadająca za kolumnę
        for case in range(0, last_index):
            case_under_condition_sum = 0
            condition_sum = 0
            # pętla odpowiadająca za zliczanie
            for training_vector in training_set:
                if training_vector[last_index] == lables_array[condition]:
                    condition_sum += 1
                    if training_vector[case] == vector[case]:
                        case_under_condition_sum += 1
                # Wygładzanie
                if case_under_condition_sum == 0:
                    case_under_condition_sum = 1
                    condition_sum += df[case].nunique()

            # prawdopodobieństwo pod warunkiem
            probability = case_under_condition_sum / condition_sum
            # prawdopodobieństwo całości
            probability_array[condition] *= probability

    indeks_max = probability_array.index(max(probability_array))
    print("Decision:", lables_array[indeks_max])
    decision.append([lables_array[indeks_max], vector[last_index]])


for i in range(0, len(parts)):
    test_set = parts[i]
    training_set = [item for sublist in parts[:i] + parts[i + 1:] for item in sublist]

    for vector in test_set:
        calculateProbability(training_set, vector)

for element in decision:
    if (element[0] == element[1]):
        good_predicted = good_predicted + 1

print(f"accuracy: {good_predicted / df.shape[0] * 100:.2f}%")
