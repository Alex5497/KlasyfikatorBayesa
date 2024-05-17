# Car Evaluation Classifier

This repository contains a simple implementation of a Naive Bayes classifier for evaluating car data. The program reads a dataset, splits it into training and testing parts, and calculates the accuracy of the predictions.

## Dataset

The dataset used in this project is `car_evaluation.data`. It contains information about car evaluations based on various attributes. The last column of the dataset represents the classification labels.

## Installation

1. Clone the repository to your local machine.
2. Ensure you have Python installed (version 3.6 or higher).
3. Install the required packages by running:
   ```bash
   pip install pandas
   ```

## Usage

1. Place the `car_evaluation.data` file in the same directory as the script.
2. Run the script:
   ```bash
   python car_evaluation.py
   ```
3. The script will output the decision for each vector and the overall accuracy.

## Code Explanation

The script performs the following steps:

1. **Load the Dataset**:
   ```python
   file_name = "car_evaluation.data"
   df = pd.read_csv(file_name, header=None)
   ```

2. **Shuffle and Split the Data**:
   The data is shuffled and split into 5 parts for cross-validation.
   ```python
   number_of_parts = 5
   data_list = df.values.tolist()
   random.shuffle(data_list)
   part_size = round(len(data_list) / number_of_parts)
   parts = [data_list[i: i + part_size] for i in range(0, len(data_list), part_size)]
   ```

3. **Calculate Probability**:
   This function calculates the conditional probability for each class label given the input vector.
   ```python
   def calculateProbability(training_set, vector):
       probability_array = [1] * lables_array.size
       # Loop through conditions and cases to calculate probabilities
       ...
   ```

4. **Cross-Validation**:
   For each part, the script uses one part as the test set and the rest as the training set. It calculates the probabilities and makes predictions.
   ```python
   for i in range(0, len(parts)):
       test_set = parts[i]
       training_set = [item for sublist in parts[:i] + parts[i + 1:] for item in sublist]
       for vector in test_set:
           calculateProbability(training_set, vector)
   ```

5. **Accuracy Calculation**:
   The script calculates and prints the accuracy of the predictions.
   ```python
   for element in decision:
       if (element[0] == element[1]):
           good_predicted = good_predicted + 1
   print(f"accuracy: {good_predicted / df.shape[0] * 100:.2f}%")
   ```

## Example Output

The output will display the decision for each vector and the overall accuracy of the classifier:
```
Decision: unacc
Decision: acc
...
accuracy: 85.00%
```

## License

This project is licensed under the MIT License.

## Acknowledgements

This project uses the car evaluation dataset from the UCI Machine Learning Repository.

---

Feel free to modify the script and adapt it to your needs. Contributions and suggestions are welcome!
