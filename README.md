# Python-Data-Science-Session7

This project contains a Python script that demonstrates various data manipulation and transformation tasks using pandas. The exercises focus on creating new columns, joining and merging dataframes, and applying string operations.

## Exercises

### 1. Create a New Column: `professor_initials`
- **Description**: Adds a new column to the dataframe with the initials of each professor's first and last name.
- **Data**: 
  - Columns: `professor`, `department`, `age`
  - Example Output:
    professor_initials
    LK
    AT
    MG
    BL

---

### 2. Use `join` to Combine DataFrames
- **Description**: Combines two dataframes, `df` and `df_courses`, based on the `professor` column using the `join` method.
- **Data**:
  - `df`: Contains professor details.
  - `df_courses`: Contains courses taught by each professor.
- **Output**:
  The resulting dataframe includes details about professors and their courses.

---

### 3. Merge DataFrames
- **Description**: Merges the `df` and `df_courses` dataframes using the `merge` function, based on the `professor` column.
- **Output**:
  A combined dataframe with professor details and their respective courses.

---

### 4. Extract Last Names
- **Description**: Adds a new column, `professor_last_name`, by extracting the last name of each professor from the `professor` column using string operations.
- **Output**:
  professor_last_name
  Kuncheva
  Torralba
  Gonzalez
  Leibe

---

## File Structure

- `pandas_exercises.py`: The main Python script containing all the exercises.
- `README.md`: This file, explaining the purpose of the script and how to use it.

## How to Run

1. Clone the repository:
   git clone https://github.com/zo-fe/Python-Data-Science-Session7.git
2. Navigate to the project directory:
   cd Python-Data-Science-Session7
3. Run the script:
   python pandas_exercises.py

## Output

The script prints the results of each exercise to the console, showing how the data is transformed step-by-step.
