import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
from sktime.transformations.panel.rocket import Rocket
from sklearn.linear_model import RidgeClassifier

st.title("Salinity Classifier (ROCKET + Ridge)")

# Upload and clean dataset
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Show data preview
    st.subheader("Preview of Uploaded Data")
    st.write(df.head())

    # Clean dataset (basic filtering)
    if 'EC' not in df.columns:
        st.error("Dataset must contain 'EC' column.")
    else:
        df_cleaned = df[['EC']].dropna()
        X = df_cleaned[['EC']].values
        y = np.where(df_cleaned['EC'] > 600, 1, 0)

        # Split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )

        # ROCKET transformation
        rocket = Rocket()
        X_train_transformed = rocket.fit_transform(X_train.reshape(-1, 1, 1))
        X_test_transformed = rocket.transform(X_test.reshape(-1, 1, 1))

        # RidgeClassifier
        model = RidgeClassifier()
        model.fit(X_train_transformed, y_train)
        y_scores = model.decision_function(X_test)

        # ROC Curve
        fpr, tpr, _ = roc_curve(y_test, y_scores)
        roc_auc = auc(fpr, tpr)

        # Plot using matplotlib
        st.subheader("ROC Curve")
        fig, ax = plt.subplots()
        ax.plot(fpr, tpr, color='orange', label=f'ROCKET AUC = {roc_auc:.2f}')
        ax.plot([0, 1], [0, 1], 'k--')
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.set_title('ROC Curve')
        ax.legend()
        st.pyplot(fig)

        # Add citation
        st.caption("Source: Thorslund & van Vliet (2020) — DOI: 10.1594/PANGAEA.913939")
