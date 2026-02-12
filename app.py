import streamlit as st
import pandas as pd
import numpy as np

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(layout="wide")
st.title("🏎️ F1 Win Probability & Championship Predictor")


# ===============================
# LOAD DATA
# ===============================
@st.cache_data
def load_data():
    return pd.read_csv(
        "C:/Users/DELL/OneDrive/Desktop/projects/F1 Championship Model/data/final_model_data.csv"
    )

df = load_data()


# ===============================
# SIDEBAR
# ===============================
st.sidebar.header("Controls")


num_sims = st.sidebar.slider(
    "Monte Carlo simulations",
    1000, 20000, 5000, step=1000
)


# ===============================
# CREATE PROBABILITIES (NO MODEL)
# ===============================
race_df = df.copy()

race_df["win_probability"] = (
    race_df["championship_score"] /
    race_df["championship_score"].sum()
)

race_df = race_df.sort_values("win_probability", ascending=False)


# ===============================
# TABLE
# ===============================
st.subheader("🏁 Win Probabilities")

st.dataframe(
    race_df[["driver_id", "win_probability"]]
    .set_index("driver_id")
    .style.format("{:.2%}")
)


# ===============================
# BAR CHART
# ===============================
st.subheader("Probability Chart")

st.bar_chart(
    
    race_df.set_index("driver_id")["win_probability"]
)


# ===============================
# MONTE CARLO SIMULATION
# ===============================
st.subheader("🏆 Championship Simulation")


def simulate_season(probabilities, drivers, n=5000):
    wins = {d: 0 for d in drivers}

    for _ in range(n):
        winner = np.random.choice(
            drivers,
            p=probabilities / probabilities.sum()
        )
        wins[winner] += 1

    for k in wins:
        wins[k] /= n

    return pd.Series(wins)


if st.button("Run Simulation"):
    sim_probs = simulate_season(
        race_df["win_probability"].values,
        race_df["driver_id"].values,
        num_sims
    )

    st.bar_chart(sim_probs.sort_values(ascending=False))
