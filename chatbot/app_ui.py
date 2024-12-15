import gradio as gr

def generate_article(keyword, keyword_difficulty, search_volume):
    """
    Generates an SEO-optimized article based on the given keyword, keyword difficulty, and search volume.
    Replace this placeholder logic with your article-generation model or API call.
    """
    if not keyword:
        return "Please enter a valid keyword."

    # Placeholder for article generation logic
    article = (
        f"<h1>{keyword}</h1>\n"
        f"<p>The keyword '{keyword}' has a difficulty score of {keyword_difficulty} and a search volume of {search_volume} per month. "
        "Here is an example of an SEO-optimized article written with the best practices for high search rankings."
        "</p>\n"
        f"<p>Introduction: The term '{keyword}' is increasingly searched by users who are keen to understand its importance and relevance in today's world."
        "</p>\n"
        f"<p>Content Body: Leveraging '{keyword}' can bring great value to individuals and businesses alike. "
        "Here are the top tips to optimize your strategy around this keyword, ensuring maximum engagement and visibility."
        "</p>\n"
        f"<p>Conclusion: In conclusion, '{keyword}' represents an important aspect of modern searches with a demand of {search_volume} monthly searches. "
        "Proper optimization around this keyword will ensure that your content ranks effectively on search engines."
        "</p>"
    )

    return article

# Define the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# SEO Article Generator")

    with gr.Row():
        keyword_input = gr.Textbox(label="Keyword", placeholder="Enter your target keyword", lines=1)

    with gr.Row():
        keyword_difficulty_input = gr.Slider(
            label="Keyword Difficulty", minimum=0, maximum=100, step=1, value=50
        )

    with gr.Row():
        search_volume_input = gr.Number(label="Search Volume", value=1000, precision=0)

    with gr.Row():
        generate_button = gr.Button("Generate")

    with gr.Row():
        article_output = gr.HTML(label="Generated Article")

    generate_button.click(
        generate_article,
        inputs=[keyword_input, keyword_difficulty_input, search_volume_input],
        outputs=article_output,
    )

# Launch the interface
demo.launch()


# from pytube import YouTube

# link = input("Enter the link : ")
# yt = YouTube(link)

# downloader = yt.streams.get_highest_resolution()
# print("Video downloading...")
# downloader.download(filename='Downloaded_Video.mp4')
# print("Video downloading finished...")