import os
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

import streamlit as st # type: ignore
from dotenv import load_dotenv # type: ignore

from agents.planner import plan_task
from agents.executor import execute_plan
from agents.verifier import verify_and_format

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

st.set_page_config(page_title="AI Operations Assistant", layout="centered")

st.title("🤖 AI Operations Assistant")
st.write("Enter a natural-language task to be planned and executed using multiple AI agents.")

user_task = st.text_input("Enter your task")

if st.button("Run Task") and user_task:
    with st.spinner("Planning..."):
        plan = plan_task(user_task)

    with st.spinner("Executing..."):
        execution_results = execute_plan(plan)

    with st.spinner("Verifying..."):
        final_output = verify_and_format(user_task, execution_results)

    st.subheader("Final Result")
    st.markdown(final_output)
