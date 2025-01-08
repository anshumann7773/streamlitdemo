import streamlit as st
import requests

def generate_strong_password(length=20, exclude_numbers=False, exclude_special_chars=False):
    url = "https://api.api-ninjas.com/v1/passwordgenerator"
    headers = {"X-Api-Key": "ywT0cjINTPWXfaXYF0h8FA==rULJGQLhnCjjDpPw"}  # Replace with your actual API key
    params = {
        "length": length,
        "exclude_numbers": exclude_numbers,
        "exclude_special_chars": exclude_special_chars,
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        password = data.get("random_password")  # Adjust key based on API documentation
        if not password:
            raise ValueError("Password key not found in response.")
        return password
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while making the request: {e}")
        return None
    except ValueError as e:
        st.error(f"An error occurred: {e}")
        return None

st.set_page_config(page_title="Strong Password Generator", page_icon="🔒")

st.title("Strong Password Generator")

password_length = st.slider("Password Length", min_value=8, max_value=32, value=20)
include_numbers = st.checkbox("Include Numbers", value=True)
include_special_chars = st.checkbox("Include Special Characters", value=True)

if st.button("Generate Password"):
    if not include_numbers and not include_special_chars:
        st.warning("At least one of 'Include Numbers' or 'Include Special Characters' should be selected.")
    else:
        password = generate_strong_password(
            length=password_length,
            exclude_numbers=not include_numbers,
            exclude_special_chars=not include_special_chars,
        )
        if password:
            st.success("Generated Password:")
            st.code(password, language="text")
