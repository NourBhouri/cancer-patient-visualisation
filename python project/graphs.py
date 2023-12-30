import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

#FOR THE LUNG DISEASE 
def generate_lung(user_input_level): 
    df=pd.read_csv("cancer_patient.csv")
    # Get unique levels from the DataFrame
    unique_levels = df['Level'].unique()
    # Get user input for the level (you can replace this with reading from another source)
    #user_input_level = input(f"Enter a level ({', '.join(unique_levels)}): ") 
    # Filter the DataFrame based on the user input level
    filtered_df = df[df['Level'] == user_input_level] 
    # Count the occurrences of chronic lung disease for the selected level
    lung_disease_counts = filtered_df['chronic Lung Disease'].value_counts()
    # Plotting a bar chart
    lung_disease_counts.plot(kind='bar', color='lightcoral')
    # Set labels and title
    plt.xlabel('Chronic Lung Disease')
    plt.ylabel('Count')
    plt.title(f'Distribution of chronic Lung Disease for Level {user_input_level}')
    plt.xticks(rotation=30) 
    plt.legend() 
    #save the image as png mode
    plt.savefig("Lung Disease high level.png") 
    plt.show() 

def generate_blood(user_input_level): 
    df=pd.read_csv("cancer_patient.csv")
    # Get unique levels from the DataFrame
    unique_levels = df['Level'].unique()
    # Get user input for the level (you can replace this with reading from another source)
    #user_input_level = input(f"Enter a level ({', '.join(unique_levels)}): ") 
    # Filter the DataFrame based on the user input level
    filtered_df = df[df['Level'] == user_input_level]   
    # Count the occurrences of Coughing Blood for the selected level
    Coughing_Blood_counts = filtered_df['Coughing of Blood'].value_counts()
    # Plotting a bar chart
    Coughing_Blood_counts.plot(kind='line', color='skyblue')
    # Set labels and title
    plt.xlabel('Coughing of Blood')
    plt.ylabel('Count')
    plt.title(f'Distribution of Coughing Blood for Level {user_input_level}')
    #plt.xticks(rotation=30) 
    plt.legend() 
    #save the image as png mode
    plt.savefig("Coughing Blood high level.png") 
    # Display the plot
    plt.show() 

def generate_breath(user_input_level):
    df=pd.read_csv("cancer_patient.csv")
    # Get unique levels from the DataFrame
    unique_levels = df['Level'].unique()
    # Get user input for the level (you can replace this with reading from another source)
    #user_input_level = input(f"Enter a level ({', '.join(unique_levels)}): ") 
    # Filter the DataFrame based on the user input level
    filtered_df = df[df['Level'] == user_input_level] 
    # Count the occurrences of breath shortness for the selected level
    breath_shortness_counts = filtered_df['Shortness of Breath'].value_counts()
    # Plotting a scatter plot with the lightgreen color 
    breath_shortness_counts.plot(kind='bar', color='lightgreen')
    # Set labels and title
    plt.xlabel('Breath Shortness')
    plt.ylabel('Count')
    plt.title(f'Distribution of Breath Shortness for Level {user_input_level}')
    # Display the plot
    plt.xticks(rotation=30)
    plt.legend()
    #save the image as png mode
    plt.savefig("Breath shortness high level.png") 
    plt.show()

def generate_chest(user_input_level):
    df=pd.read_csv("cancer_patient.csv")
    # Get unique levels from the DataFrame
    unique_levels = df['Level'].unique()
    # Get user input for the level (you can replace this with reading from another source)
    #user_input_level = input(f"Enter a level ({', '.join(unique_levels)}): ") 
    # Filter the DataFrame based on the user input level
    filtered_df = df[df['Level'] == user_input_level] 
    # Count the occurrences of Chest Pain for the selected level
    Chest_Pain_counts = filtered_df['Chest Pain'].value_counts()
    # Plotting a scatter plot with the lightgreen color 
    Chest_Pain_counts.plot(kind='line', color='blue') 
    # Set labels and title
    plt.xlabel('Chest Pain')
    plt.ylabel('Count')
    plt.title(f'Distribution of Chest Pain for Level {user_input_level}')
    plt.legend() 
    #save the image as png mode
    plt.savefig("chest pain high level.png") 
    # Display the plot
    plt.show() 

def generate_obesity(user_input_level):
    df=pd.read_csv("cancer_patient.csv")
    # Get unique levels from the DataFrame
    unique_levels = df['Level'].unique()
    # Get user input for the level (you can replace this with reading from another source)
    #user_input_level = input(f"Enter a level ({', '.join(unique_levels)}): ") 
    # Filter the DataFrame based on the user input level
    filtered_df = df[df['Level'] == user_input_level] 
    # Count the occurrences of Obesity for the selected level
    Obesity_counts = filtered_df['Obesity'].value_counts()
    # Plotting a bar chart
    Obesity_counts.plot(kind='bar', color='purple')
    # Set labels and title
    plt.xlabel('obesity')
    plt.ylabel('Count')
    plt.title(f'Distribution of Obesity for Level {user_input_level}')
    plt.xticks(rotation=30) 
    plt.legend() 
    #save the image as png mode
    plt.savefig("Obesity high level.png") 
    # Display the plot
    plt.show() 