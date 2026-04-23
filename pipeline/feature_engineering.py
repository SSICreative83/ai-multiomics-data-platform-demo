def generate_features(df):
    df["feature_scaled"] = (df["combined_feature"] - df["combined_feature"].mean()) / df["combined_feature"].std()
    return df
