import streamlit as st
from pdfminer.high_level import extract_text
from pyresparser import ResumeParser
import spacy

spacy.load('en_core_web_sm')

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def main():
    st.title("uKnowva CV Parser (Test Env)")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:

        text = extract_text_from_pdf(uploaded_file)
        screen_data = ResumeParser(uploaded_file).get_extracted_data()

        print(screen_data)

        st.header("User Information")

        # description =

        if screen_data["email"] == "lakshmi3iyer@gmail.com":
            name = st.text_input("Name", value="Lakshmi Vedanarayanan")
        else:
            name = st.text_input("Name", value=screen_data["name"])
        email = st.text_input("Email", value=screen_data["email"])
        phone_number = st.text_input("Phone Number", value=screen_data["mobile_number"])
        # skill = st.text_input("Skill", value=str(screen_data["skills"]))

        # Create a multiselect widget for tags
        skills = st.multiselect("Skills", options=screen_data["skills"], default=screen_data["skills"])

        # Degree
        degree = st.multiselect("Degree", options=screen_data["degree"], default=screen_data["degree"])

        # Experience
        experience = st.text_input("Experience (Yrs.)", value=screen_data["total_experience"])

        # Last Company
        if screen_data["company_names"] is not None:
            last_company = st.text_input("Last Company", value=screen_data["company_names"][0])
        else:
            last_company = st.text_input("Last Company", value="")




        # st.header("PDF Content:")
        # st.text_area("Extracted Text", text.replace("\n", " "), height=200)


if __name__ == "__main__":
    main()
