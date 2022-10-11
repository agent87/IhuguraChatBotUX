from urllib import response
import requests
import streamlit as st
import time
from lib.translate import translator
from lib.s2t import convert



SIDEBAR_OPTION_PROJECT_INFO = "Learn More about the Project"
SIDEBAR_OPTION_TRY = "Try our Demo!"
SIDEBAR_OPTION_MEET_TEAM = "Meet the Team"
SIDEBAR_OPTIONS = [SIDEBAR_OPTION_PROJECT_INFO, SIDEBAR_OPTION_TRY, SIDEBAR_OPTION_MEET_TEAM]


TRY_SIDEBAR_OPTION_TEXT_QUERY = "Type your Query"
TRY_SIDEBAR_OPTION_SPEECH_QUERY = "Voice Enabled Query"
TRY_SIDEBAR_OPTIONS = [TRY_SIDEBAR_OPTION_TEXT_QUERY, TRY_SIDEBAR_OPTION_SPEECH_QUERY]


TRY_SIDEBAR_OPTION_EN = "English"
TRY_SIDEBAR_OPTION_RW = "Kinyarwanda"
TRY_SIDEBAR_OPTIONS_LANG = [TRY_SIDEBAR_OPTION_EN, TRY_SIDEBAR_OPTION_RW]

#st.cache()
def startup_load():
    one = st.title('Ewawe Parking Managment System V.2.1')
    progress_bar = st.progress(0)
    status_text = st.empty()
    for i in range(100):
        # Update progress bar.
        progress_bar.progress(i + 1)
        # Update status text.
        status_text.text(
        'Starting up the system :{}%'.format(i) )
        # Pretend we're doing some computation that takes time.
        time.sleep(0.1)
    one.empty()
    progress_bar.empty() 
    status_text.empty()

class request_api:
    base_url = "http://109.74.203.113/"
    def text_query_en(self, query, mobile_num):
        response = requests.get(url=self.base_url+'query/text/en?query={0}&mobile={1}'.format(query,mobile_num))

    def text_query_rw(self, query, mobile_num):
        response = requests.get(url=self.base_url+'query/text/rw?query={0}&mobile={1}'.format(query,mobile_num))

    def speech_query_rw(self, audio_query, mobile_num):
        pass

class text_query:
    def __init__(self, lang):
        if lang == "EN":
            st.title("English Q&A")
            st.text("This is a text based Q&A inquiry")
            question = st.text_area("Type your question here!", value="", height=10, max_chars=100, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
            submit = st.button('Submit Inquiry')
        elif lang == "RW":
            st.title("Kinyarwanda Q&A")
            st.text("Baza ikibazo ukoresheje amagambo yanditse!")
            question = st.text_area("Andika ikibazo cyawe aha!", value="", height=10, max_chars=100, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
            submit = st.button('Ohereza Ikibazo Cyawe')
        else:
            pass


    

def main():
    st.sidebar.title("Navigation Bar")
    AppMode = st.sidebar.selectbox('Please select from the following',SIDEBAR_OPTIONS)
    trans = translator()

    if AppMode == SIDEBAR_OPTION_PROJECT_INFO:
        st.title("Ihugure Chatbot")
        st.write("""In a 2017 [survey](https://legalaidrwanda.org/IMG/pdf/845_final_narrative_report_2018_2021_.pdf) of 5500 citizens, it was discovered that 27% of respondents had to walk between 30 minutes and an hour to reach the nearest legal aid provider; 16% had to walk between one and three hours; 3% had to travel more than five hours, and only 4% of respondents rated their legal knowledge as "high." and in addition had to  wait to meet with an advocate in person, regardless of the nature of their case or the services they may require.""")
        st.write("""In addition,  the aspect of iliteracy was also found to be a significant factor in the decision to seek legal aid.""")
        st.subheader("Project Description")
        st.write("[Code of Criminal Procedure]()")
        st.write("")
    elif AppMode == SIDEBAR_OPTION_TRY:
        TryAppMode = st.sidebar.selectbox('Please select from the following',TRY_SIDEBAR_OPTIONS)
        if TryAppMode ==  TRY_SIDEBAR_OPTION_TEXT_QUERY:
            TEXT_QUERY_LANG_MODE = st.sidebar.selectbox('Choose a Language', TRY_SIDEBAR_OPTIONS_LANG)
            if TEXT_QUERY_LANG_MODE == 'English':
                text_query_ui = text_query('EN')
            elif TEXT_QUERY_LANG_MODE == 'Kinyarwanda':
                text_query_ui = text_query('RW')
            else:
                st.warning('Please choose a language to proceed!')
        elif TryAppMode ==  TRY_SIDEBAR_OPTION_TEXT_QUERY:
            text_query_ui = text_query('ENG')
        

        
    elif AppMode == SIDEBAR_OPTION_MEET_TEAM:
        st.title("Meet the team behind the system")
        st.success('Hope you had a great time :)')
        st.write('Please feel free to connect with us on Linkedin!')
        expandar_linkedin = st.beta_expander('Contact Information')
        expandar_linkedin.write('Arnaud: https://www.linkedin.com/in/arnaud-kayonga-5910a813a/')
        expandar_linkedin.write('Arlene: https://www.linkedin.com/in/arnaud-kayonga-5910a813a/')
        expandar_linkedin.write('Bella: https://www.linkedin.com/in/arnaud-kayonga-5910a813a/')




main()