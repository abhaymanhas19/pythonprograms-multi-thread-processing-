# import os
# import openai

# openai.api_key = "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"


# while True:
#     question = input("Enter your question: ")
#     if question.lower() == 'quit':
#         break
#     else:
#         response = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[{"role": "user", "content": f'Translate the following English text to French: {question}'}], temperature=0)
    
    


# variables = {
#     "Summarize": ["summary", "instruction"],
#     "Ask_a_specific_question": ["question", "instruction", "keywords"],
#     "Conduct_thematic_analysis": ["theme_type", "instruction"],
#     "Identidy_which_document_contain_a_certain_viewpoint": ["instruction"],
#     "Compare_viewpoints_across_documents": ["instruction", "question"]
# }  

# choices=['Summarize','Ask_a_specific_question','Conduct_thematic_analysis','Identidy_which_document_contain_a_certain_viewpoint','Compare_viewpoints_across_documents']

# choice=int(input("enter your choices"))
# for index , value in enumerate(choices):
#     print(index, value)

# if choice==0:
#     v=[i for i in variables[choices[0]]]
#     for i in v:
        
# if choice==1:
#     v=[i for i in variables[choices[1]]]
#     print(v)

# if choice==2:
#     v=[i for i in variables[choices[2]]]
#     print(v)

# if choice==3:
#     v=[i for i in variables[choices[3]]]
#     print(v)

# if choice==4:
#     v=[i for i in variables[choices[4]]]
#     print(v)

def api_endpoint_from_url(request_url):
    """Extract the API endpoint from the request URL."""
    return request_url.split("/")[-1]

print(api_endpoint_from_url("https://api.openai.com/v1/embeddings"))


