import streamlit as st
from flow_runner import run_flow
import json
import os

st.title("ART Finder-Automated Research and Trigger Finder")
st.markdown(
    """
The objective of ART Finder is to streamline the research phase of ad creation by automating data gathering and analysis.

"""
)

endpoint = "9a873ff6-171c-493d-9210-bdf672effd96"
application_token = "AstraCS:JwZiZZHHjJPcbmjkCWFffxCR:3dd508c90822cee8036c64db4a1b1095ead1af4a666cc74e20e72f67d22b86d0"
output_type = "chat"
input_type = "chat"

message = st.text_area("Enter your message", placeholder="Type your message here...")

if st.button("Run Flow"):
    try:
        response = run_flow(
            message=message,
            endpoint=endpoint,
            output_type=output_type,
            input_type=input_type,
            application_token=application_token,
        )

        st.subheader("Response")
        if isinstance(response, dict):
            try:
                parsed_value = response["outputs"][0]["outputs"][0]["results"][
                    "message"
                ]["data"]["text"]
                st.write(parsed_value)

                if "visualization" in response["outputs"][0]["outputs"][0]["results"]:
                    visualization_data = response["outputs"][0]["outputs"][0][
                        "results"
                    ]["visualization"]
                    st.json(visualization_data)

            except KeyError:
                st.error("The expected key structure is missing in the response.")
        elif isinstance(response, str):
            st.write(response)
        else:
            st.error(
                "Unexpected response format. Check the API or tweaks configuration."
            )

    except json.JSONDecodeError:
        st.error("Invalid JSON in Tweaks")
    except Exception as e:
        st.error(f"Error: {e}")
