import re

def remove_meta_data(chat_file_path):
    datetime_pattern = r"(\d+\/\d+\/\d+,\s\d+:\d+)" 
    dash_white_space = r"\s-\s"
    username_pattern = r"([\w\s]+)"
    meta_data_end = r":\s"
    pattern = datetime_pattern + dash_white_space + username_pattern + meta_data_end 
    
    try:
        with open(chat_file_path, "r", encoding="utf-8") as corpus_file:
            content = corpus_file.read()
            clean_corpus = re.sub(pattern, "", content)
            return clean_corpus.split("\n")
    except FileNotFoundError:
        print(f"Error: File '{chat_file_path}' not found.")
        return []

def remove_non_message_text(exported_text_lines):
    filter_out_msg = ("<Media omitted>")
    return [msg for msg in exported_text_lines[1:-1] if msg != filter_out_msg]

def clean_corpus(chat_file_path):
    message_corpus = remove_meta_data(chat_file_path)
    cleaned_corpus = remove_non_message_text(message_corpus)
    return cleaned_corpus  # Corrected the return variable name
