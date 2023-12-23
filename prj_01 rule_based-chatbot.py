import gradio as gr
import re

def healthcare_chatbot(user_input):
    rules = {
        r'hey': 'Hello! How can I help you?',
        r'how are you': 'I am just a computer program, but I am doing well. How about you?',
        r'your name': 'I am a chatbot, you can call me ChatGPT.',
        r'bye|goodbye': 'Goodbye! Have a great day!',
        r'(\b(?:thanks?|thank you)\b)': 'You\'re welcome!',
        r'.*\bnausea\b.*': 'I\'m sorry to hear about your nausea. It could be due to various reasons. Make sure to stay hydrated and consider eating light, bland foods. If symptoms persist, consult with a healthcare professional.',
        r'.*\ballerg(y|ies)\b.*': 'Allergies can be triggered by various factors, such as pollen or dust. Try to identify the cause and minimize exposure. Over-the-counter antihistamines may provide relief. Consult a doctor if symptoms persist.',
        r'.*\bfever\b.*': 'A fever could be a sign of an infection. Make sure to get plenty of rest and stay hydrated. If the fever persists or worsens, consult with a healthcare professional.',
        r'.*\bcough\b.*': 'If you have a persistent cough, it could be due to a variety of reasons, such as a cold or flu. Stay hydrated, use a humidifier, and consider over-the-counter cough medicine. Consult with a doctor if the cough persists.',
        r'.*\bflu\b.*': 'If you suspect you have the flu, it\'s essential to get plenty of rest and stay hydrated. Over-the-counter medications may help alleviate symptoms. Consult with a healthcare professional for personalized advice.',
        r'.*\bheadache\b.*': 'Headaches can have various causes. Ensure you are well-hydrated and consider taking a break if you\'ve been staring at screens for a long time. Over-the-counter pain relievers may help. If headaches persist, consult with a doctor.',
        r'.*\bstomachache\b.*': 'Stomachaches can be caused by various factors, including indigestion or a viral infection. Consider avoiding heavy or spicy foods and stay hydrated. If the pain persists, consult with a healthcare professional.',
        r'.*': 'I\'m sorry, I didn\'t understand that. Can you please rephrase or ask another question?'
    }

    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    
    return 'I\'m sorry, I didn\'t understand that. Can you please rephrase or ask another question?'

def chatbot_interface(user_input):
    response = healthcare_chatbot(user_input)
    return response

# Create Gradio Interface
iface = gr.Interface(
    fn=chatbot_interface,
    inputs=gr.Textbox(),
    outputs=gr.Textbox(),
    live=True,
    title="Healthcare Chatbot",
    description="Ask about symptoms, and the chatbot will provide health recommendations based on predefined rules."
)

# Launch the Gradio Interface
iface.launch()
