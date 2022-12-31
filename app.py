import streamlit as st
import json



class Sidebar:
    #Primary Options
    SIDEBAR_OPTION_PRIMARY = ["Documentation","Try the Chatbot!"]
    SIDEBAR_OPTION_QUERY_MODE = ["Speech/Voice","Text"]
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
            if self.QUERY_MODE == "Speech/Voice":
                self.NAVBAR_MODE_QUERY = "Speech/Voice"
            elif self.QUERY_MODE == "Text":
                self.NAVBAR_MODE_QUERY = "Text"
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


class Documentation:
    def __init__(self):
        st.title("Documentation")
        st.text("This is the project info page")


class Chatbot:
    def __init__(self):
        st.title("Ihugura Chatbot")
        st.text("This is the trial chatbot page")

    def VoiceQueryUI(self, lang, title, description, sample, button):
        st.title("Voice Query")
        st.text("This is the voice query page")
        record = st.file_uploader("Voice Query", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

    def TextQueryUI(self, lang, title, description, placeholder, button):
        st.title(title)
        st.text(description)
        question = st.text_area(placeholder, value="", height=10, max_chars=100, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
        submit = st.button('Ohereza Ikibazo Cyawe')

        if submit:
            st.text(question)
            st.text("This is the text query page")

    def fetchResponse(self, question, lang):
        st.text("This is the text query page")

    def fetchVoice2Text(self, lang, record):
        st.text("This is the text query page")


class Main:
    def __init__(self):
        self.title = "Main"
        self.SidebarNav = Sidebar()

        if self.SidebarNav.NAVBAR_MODE_PRIMARY == "Documentation":
            DocumentationMode = Documentation()
        elif self.SidebarNav.NAVBAR_MODE_PRIMARY == "Try the Chatbot!":
            print('I am here')
            ChatbotMode = Chatbot()
            if self.SidebarNav.NAVBAR_MODE_QUERY  == "Speech/Voice":
                VoiceQueryUI  = ChatbotMode.VoiceQueryUI(lang="en", title="Voice Query", description="This is the voice query page", sample="Sample", button="Ohereza Ik")
            elif self.SidebarNav.NAVBAR_MODE_QUERY == "Text":
                TextQueryUI = ChatbotMode.TextQueryUI(lang="en", title="Text Query", description="This is the text query page", placeholder="Enter your question here", button="Ohereza Ik")
            else:
                pass
        else:
            pass


if __name__ == "__main__":
    main = Main()