import gradio as gr
import os
# import openai

# Function to generate the essay
def generate_essay(project_info, accessibility_info):
    # Define the prompt
    prompt = f"""
    Write a well-organized and insightful essay using high school vocabulary. The essay should be about the user's interest in web design, using the information provided below:
    
    1. The user describes their experience with designing something: "{project_info}".
    2. The user shares an experience with someone they know who has a disability that makes using computers challenging: "{accessibility_info}".

    The essay should show how these experiences inspire the user to learn more about web design, especially focusing on accessibility and inclusivity.
    """

    # (You will need to set up the OpenAI API key and uncomment this section.)
    # response = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt=prompt,
    #     max_tokens=300
    # )

    # For now, returning a placeholder response
    return "This is a placeholder essay. Replace this with the actual response from GPT-4 once the API key is set up."

# Gradio app layout
def main():
    with gr.Blocks() as app:
        gr.Markdown("## Enter some information to make this essay yours!")
        
        # Input fields
        with gr.Row():
            project_info = gr.Textbox(
                label="Tell about something you built or did on a computer or phone that you are proud of. "
                      "This should show that you like designing things."
            )
            accessibility_info = gr.Textbox(
                label="Please tell about someone you know personally who has a disability that makes it harder for them to do things on the computer. "
                      "This could be anything related to vision, hearing, physical limitations, problems with reading or attention deficits."
            )
        
        # Output area
        output = gr.Textbox(label="Generated Essay")
        
        # Submit button
        submit_button = gr.Button("Generate Essay")
        submit_button.click(
            fn=generate_essay,
            inputs=[project_info, accessibility_info],
            outputs=output
        )
    
    return app

# Run the Gradio app
if __name__ == "__main__":
    app = main()
    app.launch()
