from pathlib import Path
from docling.document_converter import DocumentConverter
import re
from collections import Counter
from pathlib import Path
from langchain_text_splitters import MarkdownHeaderTextSplitter

def export_one_file(output_file_path,path_file):
    converter = DocumentConverter()
    if output_file_path.exists():
        pass
    else:
        file_handled = converter.convert(path_file)
        file_exported = file_handled.document.export_to_markdown()
        output_file_path.write_text(file_exported,encoding='utf-8')
    return output_file_path
    
def export_many_files(input_path,output_path):
    processed_file = []
    for path_file in input_path.glob('*.pdf'):
        output_file_name = path_file.stem + '.md'
        output_file_path = Path(output_path/output_file_name)
        output_file = export_one_file(output_file_path,path_file)
        processed_file.append(output_file)
    return processed_file

def fast_clean(text_content, common_garbage_list):
    text_content = re.sub(r'', '', text_content)
    text_content = re.sub(r'/s/ [\w\s.]+', '', text_content)
    text_content = re.sub(r'Page \d+ of \d+', '', text_content)
    blacklist = [t for t, c in common_garbage_list]
    
    for junk in blacklist:
        text_content = re.sub(f'^{re.escape(junk)}$', '', text_content, flags=re.M)
        
    text_content = re.sub(r'\n{3,}', '\n\n', text_content)
    return text_content.strip()

def extract_chunk(output_path):
    headers_to_split_on = [
    ('#','Header_1'),
    ('##','Header_2'),
    ('###','Header_3'),]

    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    all_chunks = []
    for f_path in output_path:
        raw_text = f_path.read_text(encoding='utf-8')
        lines = raw_text.splitlines()
        short_sentences = [l.strip() for l in lines if 0<len(l.strip())<30]
        common_garbage = Counter(short_sentences).most_common(15)
        clean_text = fast_clean(raw_text,common_garbage)
        chunks = markdown_splitter.split_text(clean_text)
        for chunk in chunks:
            chunk.metadata['source'] = f_path.name
            all_chunks.append(chunk)
    return all_chunks