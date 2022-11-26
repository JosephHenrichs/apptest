
with st.form(key='my_form_to_submit'):    
    company_name = st.text_input("Company Name: ", "Google")
    role = st.text_input("What role are you applying for? ", "Machine Learning Engineer")
    contact_person = st.text_input("Who are you emailing? ", "Technical Hiring Manager")
    your_name = st.text_input("What is your name? ", "Amber Teng")
    personal_exp = st.text_input("I have experience in...", "natural language processing, fraud detection, statistical modeling, and machine learning algorithms. ")
    job_desc = st.text_input("I am excited about the job because...", "this role will allow me to work on technically challenging problems and create impactful solutions while working with an innovative team. " )
    passion = st.text_input("I am passionate about...", "solving problems at the intersection of technology and social good.")
    submit_button = st.form_submit_button(label='Submit')

prompt = ("Write a cover letter to " + contact_person + " from " + your_name +" for a " + role + " job at " + company_name +"." + " I have experience in " +personal_exp + " I am excited about the job because " +job_desc + " I am passionate about "+ passion)
