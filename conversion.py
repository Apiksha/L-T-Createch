import pandas as pd

def extract_data_from_anl(file_path):
    # Initialize a dictionary to hold the extracted data
    data = {
        'Node': [],
        'Displacement_X': [],
        'Displacement_Y': [],
        'Displacement_Z': [],
        'Max_Stress': [],
        'Min_Stress': [],
        'Member_ID': [],
        'Axial_Force': [],
        'Shear_Force': [],
        'Bending_Moment': []
    }
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        # Example parsing logic
        for line in lines:
            # Extract node displacement data
            if "DISPLACEMENT" in line:
                parts = line.split()
                data['Node'].append(parts[1])  # Assuming node number is in the second position
                data['Displacement_X'].append(float(parts[2]))
                data['Displacement_Y'].append(float(parts[3]))
                data['Displacement_Z'].append(float(parts[4]))
            
            # Extract stress data
            elif "STRESS" in line:
                parts = line.split()
                data['Max_Stress'].append(float(parts[1]))
                data['Min_Stress'].append(float(parts[2]))
            
            # Extract member forces
            elif "FORCE" in line:
                parts = line.split()
                data['Member_ID'].append(parts[1])  # Assuming member ID is in the second position
                data['Axial_Force'].append(float(parts[2]))
                data['Shear_Force'].append(float(parts[3]))
                data['Bending_Moment'].append(float(parts[4]))
    
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    return df

# Example usage
anl_file_path = 'path_to_your_file.anl'
data_df = extract_data_from_anl(anl_file_path)

# Save to CSV
data_df.to_csv('extracted_data.csv', index=False)