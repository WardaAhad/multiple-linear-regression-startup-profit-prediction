import streamlit as st
import requests

st.set_page_config(
    page_title="Startup Profit Prediction",
    page_icon="📈",
    layout="centered"
)

st.title("📈 Startup Profit Prediction")

st.write("Enter Startup Details")

rd = st.number_input("R&D Spend", min_value=0.0)

admin = st.number_input("Administration", min_value=0.0)

marketing = st.number_input("Marketing Spend", min_value=0.0)

state = st.selectbox(
    "Select State",
    ["California", "Florida", "New York"]
)

# Railway Backend API URL
API_URL = "https://multiple-linear-regression-startup-profit-predic-production.up.railway.app/predict"


if st.button("Predict Profit"):

    # One Hot Encoding (drop_first=True)
    if state == "Florida":
        state_florida = 1
        state_new_york = 0

    elif state == "New York":
        state_florida = 0
        state_new_york = 1

    else:  # California (baseline)
        state_florida = 0
        state_new_york = 0


    data = {
        "rd_spend": rd,
        "administration": admin,
        "marketing_spend": marketing,
        "state_florida": state_florida,
        "state_new_york": state_new_york
    }


    try:
        response = requests.post(
            API_URL,
            json=data
        )

        if response.status_code == 200:
            result = response.json()

            st.success(
                f"Predicted Profit: ${result['predicted_profit']:,.2f}"
            )

        else:
            st.error(f"Status Code: {response.status_code}")
            st.write("Response from Backend:")
            st.write(response.text)


    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the backend.")

    except Exception as e:
        st.error(f"❌ Error: {e}")