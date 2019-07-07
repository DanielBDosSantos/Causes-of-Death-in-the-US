import csv
import matplotlib.pyplot as plt

def get_type_of_death():
    with open('/usr/Desktop/causeOfDeath/NCHS_-_Leading_Causes_of_Death__United_States.csv', 'r') as f:
        kidney_disease_count = 0
        influenza_pne_count = 0
        diabetes_count = 0
        suicide_count = 0
        alzheimer_count = 0
        uninj_count = 0
        clrd_count = 0
        stroke_count = 0
        cancer_count = 0
        heart_disease_count = 0

        find_names = []

        for row in csv.DictReader(f):
            if row['Cause Name'] not in find_names:
                find_names.append(row['Cause Name'])

            if row['Cause Name'] == 'Kidney disease':
                kidney_disease_count += int(row['Deaths'])
            elif row['Cause Name'] == 'Influenza and pneumonia':
                influenza_pne_count += int(row['Deaths'])
            elif row['Cause Name'] == 'Diabetes':
                diabetes_count += int(row['Deaths'])
            elif row['Cause Name'] == 'Suicide':
                suicide_count += int(row['Deaths'])
            elif row['Cause Name'] == 'Alzheimer\'s disease':
                alzheimer_count += int(row['Deaths'])
            elif row['Cause Name'] == 'Unintentional injuries':
                uninj_count += int(row['Deaths'])
            elif row['Cause Name'] == 'CLRD':
                clrd_count += int(row['Deaths'])
            elif row['Cause Name'] == 'Stroke':
                stroke_count += int(row['Deaths'])
            elif row['Cause Name'] == 'Cancer':
                cancer_count += int(row['Deaths'])
            elif row['Cause Name'] == 'Heart disease':
                heart_disease_count += int(row['Deaths'])

        print(str(kidney_disease_count) + ' deaths in the US are from kidney disease.')
        print(str(influenza_pne_count) + ' deaths in the US are from Influenza and pneumonia.')
        print(str(diabetes_count) + ' deaths in the US are from diabetes.')
        print(str(suicide_count) + ' deaths in the US are from suicide.')
        print(str(alzheimer_count) + ' deaths in the US are from Alzheimer\'s disease.')
        print(str(uninj_count) + ' deaths in the US are from unintentional injuries.')
        print(str(clrd_count) + ' deaths in the US are from chronic lower respiratory diseases.')
        print(str(stroke_count) + ' deaths in the US are from a stroke.')
        print(str(cancer_count) + ' deaths in the US are from cancer.')
        print(str(heart_disease_count) + ' deaths in the US are from heart disease.')

        print(find_names)

        plt.bar(0, (kidney_disease_count / 1000000.), align='center', label='kidney disease', color='red')
        plt.bar(1, (influenza_pne_count / 1000000.), align='center', label='Influenza and pneumonia', color='green')
        plt.bar(2, (diabetes_count / 1000000.), align='center', label='diabetes', color='blue')
        plt.bar(3, (suicide_count / 1000000.), align='center', label='suicide', color='yellow')
        plt.bar(4, (alzheimer_count / 1000000.), align='center', label='Alzheimer\'s disease', color='orange')
        plt.bar(5, (uninj_count / 1000000.), align='center', label='unintentional injuries', color='purple')
        plt.bar(6, (clrd_count / 1000000.), align='center', label='chronic lower respiratory diseases', color='cyan')
        plt.bar(7, (stroke_count / 1000000.), align='center', label='stroke', color='black')
        plt.bar(8, (cancer_count / 1000000.), align='center', label='cancer', color='brown')
        plt.bar(9, (heart_disease_count / 1000000.), align='center', label='heart disease', color='lightgreen')
        plt.xlabel('Leading Causes of Death in the US')
        plt.ylabel('Number of Deaths from 1999 - 2016\n(per million)')
        plt.margins(0.2)
        plt.legend()
        plt.show()

if __name__=="__main__":
    get_type_of_death()
