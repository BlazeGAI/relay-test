import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Streamlit App
def main():
    st.title("Email Sender App")
    
    st.write("Send an email through a relay server with this simple interface.")
    
    # Form inputs
    with st.form(key="email_form"):
        sender_email = st.text_input("Sender Email")
        sender_password = st.text_input("Sender Password", type="password")
        recipient_email = st.text_input("Recipient Email")
        subject = st.text_input("Subject")
        message_body = st.text_area("Message")
        relay_server = st.text_input("Relay Server (e.g., smtp.gmail.com)")
        relay_port = st.number_input("Relay Port", min_value=1, max_value=65535, value=587)
        submit_button = st.form_submit_button(label="Send Email")
    
    if submit_button:
        if sender_email and sender_password and recipient_email and message_body and relay_server:
            try:
                # Create the email
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = recipient_email
                msg['Subject'] = subject
                msg.attach(MIMEText(message_body, 'plain'))
                
                # Connect to relay server and send email
                with smtplib.SMTP(relay_server, relay_port) as server:
                    server.starttls()  # Secure the connection
                    server.login(sender_email, sender_password)
                    server.sendmail(sender_email, recipient_email, msg.as_string())
                
                st.success("Email sent successfully!")
            except Exception as e:
                st.error(f"Failed to send email. Error: {e}")
        else:
            st.warning("Please fill in all fields!")

if __name__ == "__main__":
    main()
