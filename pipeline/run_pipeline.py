from ingest import load_data
from process import clean_data
from integrate import integrate_data
from feature_engineering import generate_features

def run():
    df = load_data("../data/sample_data.csv")
    df = clean_data(df)
    df = integrate_data(df)
    df = generate_features(df)
    df.to_csv("../output/processed_data.csv", index=False)

if __name__ == "__main__":
    run()
