import streamlit as st
import numpy as np
import pickle
model=pickle.load(open('model.pkl','rb'))
# st.write("hello world")
# st.file_uploader(label="upload")
# st.text_input("enter the year")
# with st.form("my_form"):
#     st.write("Inside the form")
#     st.text_input("enter the year")
#     st.text_input("enter the year")
#     slider_val = st.slider("Form slider")
#     checkbox_val = st.checkbox("Form checkbox")

#     # Every form must have a submit button.
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         st.write("slider", slider_val, "checkbox", checkbox_val)

# st.write("Outside the form")4


d={'Afghanistan': 2,
 'Albania': 3,
 'Algeria': 4,
 'Angola': 5,
 'Argentina': 6,
 'Australia': 7,
 'Austria': 8,
 'Bahrain': 9,
 'Bangladesh': 10,
 'Belgium': 11,
 'Benin': 12,
 'Bolivia': 13,
 'Bosnia and Herzegovina': 14,
 'Botswana': 15,
 'Brazil': 16,
 'Bulgaria': 17,
 'Burkina Faso': 18,
 'Burundi': 19,
 'Cambodia': 20,
 'Cameroon': 21,
 'Canada': 22,
 'Central African Republic': 23,
 'Chad': 24,
 'Chile': 25,
 'China': 26,
 'Colombia': 27,
 'Comoros': 28,
 'Congo, Dem. Rep.': 29,
 'Congo, Rep.': 30,
 'Costa Rica': 31,
 "Cote d'Ivoire": 32,
 'Croatia': 33,
 'Cuba': 34,
 'Czech Republic': 35,
 'Denmark': 36,
 'Djibouti': 37,
 'Dominican Republic': 38,
 'Ecuador': 39,
 'El Salvador': 40,
 'Equatorial Guinea': 41,
 'Eritrea': 42,
 'Ethiopia': 43,
 'Finland': 44,
 'France': 45,
 'Gabon': 46,
 'Germany': 47,
 'Ghana': 48,
 'Greece': 49,
 'Guatemala': 50,
 'Guinea': 51,
 'Guinea-Bissau': 52,
 'Haiti': 53,
 'Honduras': 54,
 'Hungary': 55,
 'Iceland': 56,
 'India': 57,
 'Indonesia': 58,
 'Iraq': 59,
 'Ireland': 60,
 'Israel': 61,
 'Italy': 62,
 'Jamaica': 63,
 'Japan': 64,
 'Jordan': 65,
 'Kenya': 66,
 'Korea, Rep.': 67,
 'Kuwait': 68,
 'Lebanon': 69,
 'Lesotho': 70,
 'Liberia': 71,
 'Libya': 72,
 'Madagascar': 73,
 'Malawi': 74,
 'Malaysia': 75,
 'Mali': 76,
 'Mauritania': 77,
 'Mauritius': 78,
 'Mexico': 79,
 'Mongolia': 80,
 'Montenegro': 81,
 'Morocco': 82,
 'Mozambique': 83,
 'Myanmar': 84,
 'Namibia': 85,
 'Nepal': 86,
 'Netherlands': 87,
 'New Zealand': 88,
 'Nicaragua': 89,
 'Niger': 90,
 'Nigeria': 91,
 'Norway': 92,
 'Oman': 93,
 'Pakistan': 94,
 'Panama': 95,
 'Paraguay': 96,
 'Peru': 97,
 'Philippines': 98,
 'Poland': 99,
 'Portugal': 100,
 'Puerto Rico': 101,
 'Romania': 102,
 'Rwanda': 103,
 'Sao Tome and Principe': 104,
 'Saudi Arabia': 105,
 'Senegal': 106,
 'Serbia': 107,
 'Sierra Leone': 108,
 'Singapore': 109,
 'Slovak Republic': 110,
 'Slovenia': 111,
 'Somalia': 112,
 'South Africa': 113,
 'Spain': 114,
 'Sri Lanka': 115,
 'Sudan': 116,
 'Swaziland': 117,
 'Sweden': 118,
 'Switzerland': 119,
 'Tanzania': 120,
 'Thailand': 121,
 'Togo': 122,
 'Trinidad and Tobago': 123,
 'Tunisia': 124,
 'Turkey': 125,
 'Uganda': 126,
 'United Kingdom': 127,
 'United States': 128,
 'Uruguay': 129,
 'Vietnam': 130,
 'West Bank and GazaYemen, Rep.': 131,
 'Zambia': 132,
 'Zimbabwe': 133}


def input_prep(country,year):
    a=[0]*135
    a[0]=year
    a[1]=year
    a[d[country]]=1
    a=np.array(a)
    a=a.reshape(1, -1)
    return a
def predict(model,country,year):
    year=int(year)
    a=input_prep(country,year)
    pred=model.predict(a)
    st.write("According to our model the population is/will be ")
    st.write(pred)


st.title("POPULATION ESTIMATION OF DIFFERENT COUNTRIES")

def main():
    with st.form("form2",clear_on_submit=False):
        country=st.text_input("Enter The Country (First letter should be Capital)",key='bb')
        year=st.text_input("Enter The Year (should be an integer)",key='aa')
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Calculating results...")
            predict(model,country,year)

if __name__ == "__main__":
    main()
# if __name__=="__main__":
#     app.run(debug=True)