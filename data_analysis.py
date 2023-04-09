import pandas as pd
from ydata_profiling import ProfileReport


def main():
    # Load structured_judgements/Chandigarh.csv into DataFrame
    chandigarh = pd.read_csv('structured_judgements/Chandigarh.csv')

    # Run PandasProfiling on the DataFrame
    profile = ProfileReport(chandigarh, title='Chandigarh Judgements')

    profile.to_file("Chandigarh_report.html")


if __name__ == '__main__':
    main()
