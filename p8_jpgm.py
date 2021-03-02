import streamlit as st
import time
import numpy as np
import pandas as pd

nav=st.sidebar.radio("Navigation",["Members","Registration"])
#rad =st.sidebar.radio("Navigation",["Home","About Us"])
# if nav=="Home":
#     st.write("Welcome.....")
if nav=="Members":
    st.header("Jalpaiguri Mariners")
    showdata= pd.read_csv("members.csv")
    sd=st.radio("Show Data",["Show","Hide"])
    if sd=="Hide":
        st.write("")
    else:
        st.table(showdata)
#    copy=showdata
#     copy.to_csv("download.csv")
#     st.sidebar.markdown("""
#     [Download File]("download.csv")
#     """)
    # https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
    def filedownload(df):
    copy = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/copy;base64,{b64}" download="jpgm.csv">Download File</a>'
    return href

st.markdown(filedownload(showdata), unsafe_allow_html=True)
    
elif nav=="Registration":
    st.header("Jalpaiguri Mariners")
    st.write("Registration Form")
    first,last,mid=st.beta_columns(3)
    email,mob=st.beta_columns([2,1])
    user,pw,pw2=st.beta_columns(3)
    dob,blood,occ=st.beta_columns(3)
    #sub=st.beta_columns(1)

    first=first.text_input("First Name")
    last=last.text_input("Last Name")
    email=email.text_input("Email Name")
    mob=mob.text_input("Mobile Name")
    dob = dob.date_input("DOB")
    blood = blood.selectbox("Blood group",["A+","A-","B+","B-","AB+","AB-","O+","O-"])
    occ = occ.text_input("Occupation")
    add=st.text_area("Address")
    # user=user.text_input("UserId")
    # pw=pw.text_input("Password",type="password")
    # pw2=pw2.text_input("Confirm Password",type="password")

    ch=st.checkbox("I Agree",value=False)
    if ch==True:
        st.warning("""Hereby I agree to abide by the present and future rules of the
        Jalpaiguri Mariners and the only identity I have at the club premises, is "MOHUNBAGANI". """)

        if st.button("Submit Button"):
            to_add={"First":[first],"Last":[last],"Email":[email],"Mobile":[mob],"DOB":[dob],
            "Blood":[blood],"Occupation":[occ],"Address":[add]}
            to_add=pd.DataFrame(to_add)
            to_add.to_csv("members.csv",mode="a",header=False,index=True)
            st.success("Submitted")
            st.balloons()
