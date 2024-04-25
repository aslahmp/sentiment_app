import streamlit as st
import joblib 

sentiment_label = {0: 'Negative', 1: 'Positive'}
st.title('Sentiment Analysis')
user_input = st.text_area('Enter your text here:')


if st.button('Predict'):
    model = joblib.load('sentiment-model.pkl')
    prediction = model.predict([user_input])
    st.write(f'The sentiment of the text is: {sentiment_label[prediction[0]]}')
