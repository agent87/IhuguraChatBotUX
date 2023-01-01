import streamlit as st 
from lib import haystack



class getResponse:
    def __init__(self, query, advancedSettings):
        query = query
        advancedSettings = advancedSettings
        self.response = self.getResponse()

    


class SpeechQueryUI:
    def __init__(self):
        self.description = st.title("Kinyarwanda Q&A")
        self.description = st.text("This is a Speech based Q&A inquiry")
        self.record = st.file_uploader("Upload your record file here!", accept_multiple_files=False, type=['mp3', 'wav'], key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
        self.AdvancedSettings = self.AdvancedSettings()
        self.submit = st.button('Submit Inquiry')

        if self.submit:
            st.text('Play your record!')
            self.playbackRecord()

    def AdvancedSettings(self):
        with st.expander("Advanced Parameters"):
            NumberofDocumentstoSearch : int = st.number_input("Number of Documents to Search", min_value=1, max_value=100, value=10, step=1)
            NumberofResults : int = st.number_input("Number of Results", min_value=1, max_value=100, value=10, step=1) 
            ConfidenceThreshold : int = st.slider("Confidence Threshold(Filter answers with higher confidence score!)", min_value=0, max_value=100, value=80, step=1, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

        return NumberofDocumentstoSearch, NumberofResults, ConfidenceThreshold

    def playbackRecord(self):
        playback = st.audio(self.record)


class TextQueryUI:
    def __init__(self):
        self.description = st.title("Kinyarwanda Q&A")
        self.description = st.text("This is a text based Q&A inquiry")
        self.question = st.text_area("Type your question here!", value="", height=10, max_chars=100, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
        self.AdvancedSettings = self.AdvancedSettings()
        self.submit = st.button('Submit Inquiry')

        if self.submit:
            st.text('Your question is: ' + self.question)
            

    def AdvancedSettings(self):
        with st.expander("Advanced Parameters"):
            NumberofDocumentstoSearch : int = st.number_input("Number of Documents to Search", min_value=1, max_value=100, value=10, step=1)
            NumberofResults : int = st.number_input("Number of Results", min_value=1, max_value=100, value=10, step=1) 
            ConfidenceThreshold : int = st.slider("Confidence Threshold(Filter answers with higher confidence score!)", min_value=0, max_value=100, value=80, step=1, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
        
        return NumberofDocumentstoSearch, NumberofResults, ConfidenceThreshold


class Sidebar:
    #Primary Options
    SIDEBAR_OPTION_PRIMARY = ["Documentation","Try the Chatbot!"]
    SIDEBAR_OPTION_QUERY_MODE = ["Text","Speech/Voice"]
    NAVBAR_MODE_PRIMARY = None
    NAVBAR_MODE_QUERY = None

    def __init__(self):
        self.SideBarTitle = st.sidebar.title("Navigation Bar")
        self.PRIMARY_OPTONS = st.sidebar.selectbox('Please select from the following', self.SIDEBAR_OPTION_PRIMARY)

        if self.PRIMARY_OPTONS == "Documentation":
            self.NAVBAR_MODE_PRIMARY = "Documentation"
        elif self.PRIMARY_OPTONS == "Try the Chatbot!":
            self.NAVBAR_MODE_PRIMARY = "Chatbot"
            self.QUERY_MODE = st.sidebar.selectbox('Select a mode!', self.SIDEBAR_OPTION_QUERY_MODE)
            if self.QUERY_MODE == "Text":
                self.NAVBAR_MODE_QUERY = "Text"
                TextQuery = TextQueryUI()
            elif self.QUERY_MODE == "Speech/Voice":
                self.NAVBAR_MODE_QUERY = "Speech/Voice"
                SpeechQuery = SpeechQueryUI()
            else:
                pass

        self.Contact = self.ContactBanner()
        self.Support = self.SupportBanner()

    
    def ContactBanner(self):
        st.sidebar.title('Contact')
        st.sidebar.info('You can contact me at: arnauldkayonga1@gmail.com')

    def SupportBanner(self):
        st.sidebar.title('Support')
        st.sidebar.info("If you want to reward my work, I'd love a cup of coffee [google.com] from you. Thanks!")



def main():
    st.set_page_config(page_title="Ihugura Chatbot")
    #Initiate the sidebar
    sidebar = Sidebar()



if __name__ == "__main__":
    main()