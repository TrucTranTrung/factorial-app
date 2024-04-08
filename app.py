import streamlit as st
from factorial import fact

def main():
  st.title("factorial caculator")
  number=st.number_input("Enter a number: ", min_value=0, max_value=900)
  if st.button("Caculate"):
    result=fact(number)
    st.write(f"the factorial of {number} is {result}")


if __name__=="__main__":
  main()