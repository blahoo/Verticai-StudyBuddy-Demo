import streamlit as st
import modules 
from streamlit_extras.app_logo import add_logo

add_logo(".\\assets\\logo_reverse.png")

st.markdown("""
<style>
.big-font {
    font-size:100px !important;
    text-align: center
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font"> Getting Started</p>', unsafe_allow_html=True)
st.markdown("""
<style>
.big-font {
    font-size:50px !important;
    text-align: center
}
.medium-font {
    font-size:35px !important;
    text-align: center
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="medium-font"> Learn how to use verticai in your daily life!</p>', unsafe_allow_html=True)

st.text("\n\n\n") # adds space


all_topics = ["Math", "Science","Chemistry", "Biology", "Physics", "Economics", "English", "History", "Geography", "Spanish", "French"]
all_grades = ["9", "10", "11", "12"]
all_countries = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua &amp; Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia &amp; Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kuwait","Kyrgyz Republic","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Namibia","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre &amp; Miquelon","Samoa","San Marino","Satellite","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","South Africa","South Korea","Spain","Sri Lanka","St Kitts &amp; Nevis","St Lucia","St Vincent","St. Lucia","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad &amp; Tobago","Tunisia","Turkey","Turkmenistan","Turks &amp; Caicos","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]

placeholder = st.empty()
with placeholder.form(key='my_form', clear_on_submit=True):
    try:
        subject = st.selectbox('Subject', placeholder="Select Subject", options=all_topics)
    except KeyError:
        pass
    try:
        grade = st.selectbox('Grade', options=all_grades, placeholder="Select Grade")
    except KeyError:
        pass
    try:
        location = st.selectbox('Location', placeholder="Country:", options=all_countries)
    except KeyError:
        pass
    
    location = str(location)
    grade = str(grade)
    subject = str(subject)

    if st.form_submit_button() == True:
        modules.context = []
        prompt = modules.chatSetUp(subject, grade, location)
        modules.context.append({"role": "user", "content": prompt})
        st.header("Setup Complete")
        st.text("Move On To The Next Steps (Go to Demo)!")







        
    
