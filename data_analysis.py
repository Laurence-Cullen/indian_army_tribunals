import pandas as pd
from ydata_profiling import ProfileReport


def main():
    # Load structured_judgements/Chandigarh.csv into DataFrame
    chandigarh = pd.read_csv('structured_judgements/Chandigarh.csv')

    # Run PandasProfiling on the DataFrame
    profile = ProfileReport(chandigarh, title='Chandigarh Judgements')

    profile.to_file("Chandigarh_report.html")

    names = chandigarh['military_judge'].values

    # Remove duplicates
    names = list(set(names))

    # Save to txt file
    with open('military_judges.txt', 'w') as f:
        for name in names:
            f.write(name + '\n')

    # Civilian judges
    names = chandigarh['civilian_judge'].values

    # Remove duplicates
    names = list(set(names))

    # Save to txt file
    with open('civilian_judges.txt', 'w') as f:
        for name in names:
            f.write(name + '\n')


if __name__ == '__main__':
    main()
