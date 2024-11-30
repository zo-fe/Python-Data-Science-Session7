import pandas as pd

# Exercise 1: Create a new column called `professor_initials`
data = {
    'professor': ['Ludmila Kuncheva', 'Antonio Torralba', 'Manuel Gonzalez', 'Bastian Leibe'],
    'department': ['Computer Science', 'Computer Vision', 'AI & Robotics', 'Autonomous Systems'],
    'age': [45, 50, 47, 38]
}

df = pd.DataFrame(data)

# Create the `professor_initials` column
df['professor_initials'] = df['professor'].apply(lambda x: ''.join([name[0] for name in x.split()]))
print("Exercise 1 Result:")
print(df)

# Exercise 2: Use `join` to combine this new DataFrame with the original one
courses_data = {
    'professor': ['Ludmila Kuncheva', 'Antonio Torralba', 'Manuel Gonzalez', 'Bastian Leibe'],
    'courses': ['Machine Learning', 'Computer Vision', 'AI Programming', 'Self-Driving Cars']
}
df_courses = pd.DataFrame(courses_data)

# Joining based on the professor column
df.set_index('professor', inplace=True)
df_courses.set_index('professor', inplace=True)
df = df.join(df_courses)
print("\nExercise 2 Result:")
print(df)

# Exercise 3: Combine `df` and `df_courses`
data = {
    'professor': ['Ludmila Kuncheva', 'Antonio Torralba', 'Manuel Gonzalez', 'Bastian Leibe'],
    'department': ['Computer Science', 'Computer Vision', 'AI & Robotics', 'Autonomous Systems'],
    'age': [45, 50, 47, 38]
}

df = pd.DataFrame(data)

courses_data = {
    'professor': ['Ludmila Kuncheva', 'Antonio Torralba', 'Manuel Gonzalez', 'Bastian Leibe'],
    'courses': ['Machine Learning', 'Computer Vision', 'AI Programming', 'Self-Driving Cars']
}
df_courses = pd.DataFrame(courses_data)

# Merge dataframes
merged_df = pd.merge(df, df_courses, on='professor')
print("\nExercise 3 Result:")
print(merged_df)

# Exercise 4: Extract last name of each professor
df['professor_last_name'] = df['professor'].apply(lambda x: x.split()[-1])
print("\nExercise 4 Result:")
print(df)
