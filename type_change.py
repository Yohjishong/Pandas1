import pandas as pd
from pdfminer.high_level import extract_text
import os
import subprocess


# 输入需要读取的文件夹和输出的文件名
def PDF_into_txt(input_catalot, output_txt):
    for file in os.listdir(input_catalot):
        # 检查文件是否是普通文件，而不是子目录或其他文件类型
        if os.path.isfile(os.path.join(input_catalot, file)):
            file = input_catalot + '\\' + file
            print(file)
            # 将单栏和双栏排版PDF文件转换为一行txt文档，它们都是一样的
            with open(output_txt, 'a', encoding='utf-8') as file_output:
                data = extract_text(file)  # 读入
                df = pd.DataFrame(data.split('\n'), columns=['text'])  # 形成一列的DF格式
                df['text'] = df['text'].apply(lambda x: x.strip())  # 删除空格
                file_output.write(''.join(df['text']))  # 最后粘贴在一起输出
                file_output.write('\n')


# 输入需要读取的文件夹和输出的文件名
def CAJ_into_txt(input_catalot, output_txt, PDF_catalog):
    os.chdir(PDF_catalog)
    for file in os.listdir(input_catalot):
        # 检查文件是否是普通文件，而不是子目录或其他文件类型
        if os.path.isfile(os.path.join(input_catalot, file)):
            hub = 'S:\\DeepLearning\\CAJ_PDF\\' + file[:-4] + '.pdf'
            file = input_catalot + '\\' + file
        subprocess.call(['python', 'caj2pdf', 'convert', file, '-o', hub])
        print(hub)
        with open(output_txt, 'a', encoding='utf-8') as file_output:
            data = extract_text(hub)  # 读入
            df = pd.DataFrame(data.split('\n'), columns=['text'])  # 形成一列的DF格式
            df['text'] = df['text'].apply(lambda x: x.strip())  # 删除空格
            file_output.write(''.join(df['text']))  # 最后粘贴在一起输出
            file_output.write('\n')


# PDF_into_txt(path, 'output.txt')  # 前一个参数为读入文件夹，后一个为读出txt文档'''

'''path = 'S:\\DeepLearning\\sample\\type3'
output = 'S:\\DeepLearning\\output.txt'
new = 'S:\\DeepLearning\\caj2pdf'
CAJ_into_txt(path, output, new)'''
'''with open('output1.txt', 'w', encoding='utf-8') as file_process:
    data = extract_text('C:\\Users\\15382\\Desktop\\1.pdf')  # 读入
    df = pd.DataFrame(data.split('\n'), columns=['text'])  # 形成一列的DF格式
    df['text'] = df['text'].apply(lambda x: x.strip())  # 删除空格
    file_process.write(''.join(df['text']))  # 最后粘贴在一起输出'''


'''# 打开PDF文件并提取所有文本
with open('C:\\Users\\15382\\Desktop\\1.pdf', 'rb') as pdf_file, StringIO() as text_buffer:
    extract_text_to_fp(pdf_file, text_buffer, laparams=LAParams())
    text = text_buffer.getvalue()
    print(pdf_file)
# 定义一个正则表达式匹配公式
formula_regex = r'\$$.*?\$$'
# 查找所有匹配公式的文本
formulas = re.findall(formula_regex, text)
# 将公式替换为标记
for i, formula in enumerate(formulas):
    text = text.replace(formula, f'FORMULA_{i}')
# 将文本和标记写入文本文件
with open('output1.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(text)
    # 写入公式
    for i, formula in enumerate(formulas):
        output_file.write(f'FORMULA_{i}: {formula}\n')'''







