import tkinter as tk
from tkinter import filedialog
import re
import os

def search_in_text_file():
    root = tk.Tk()
    root.withdraw()

    # 获取当前程序所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 让用户选择txt小说文件
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not file_path:
        print("未选择文件，程序退出。")
        return

    search_term = input("请输入搜索词: ")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 按更灵活的章节标题格式分割内容
        chapters = re.split(r'第[\u4e00-\u9fa50-9]+章', content)

        matching_chapters = []
        search_term_pattern = re.compile(r'\b{}\b'.format(re.escape(search_term)))

        for i, chapter in enumerate(chapters):
            lines = chapter.split('\n')
            for j, line in enumerate(lines):
                if re.search(search_term_pattern, line):
                    matching_chapters.append(f"{len(matching_chapters) + 1}.{line.strip()}     第{i + 1}章")

        if not matching_chapters:
            print(f"未找到包含搜索词 '{search_term}' 的章节。")
        else:
            print("找到以下包含搜索词的句子及所在章节:")
            for chapter in matching_chapters:
                print(chapter)

    except FileNotFoundError:
        print("无法打开指定的文件.")

    input("\n按下回车键退出...")


if __name__ == "__main__":
    search_in_text_file()