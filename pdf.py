from PyPDF2 import PdfFileReader, PdfFileWriter


def reverse_pdf(input_file, output_file):
    """逆序一个pdf

    :param input_file: 输入文件名
    :param output_file: 输出文件名
    :return:
    """
    pdf_output = PdfFileWriter()
    input_f = open(input_file, 'rb')
    pdf_content = PdfFileReader(input_f)

    for i in range(pdf_content.getNumPages() - 1, -1, -1):
        pdf_output.addPage(pdf_content.getPage(i))

    with open(output_file, 'wb') as f:
        pdf_output.write(f)

    input_f.close()
    return output_file


def merge_pdf_between(input_file_1, input_file_2, output_file):
    """合并两个pdf，先是第一个文件的第一页，之后是第二个文件的第一页，以此类推

    :param input_file_1: 第一个文件名
    :param input_file_2: 第二个文件名
    :param output_file: 输出文件名
    :return:
    """
    pdf_output = PdfFileWriter()

    input_f_1 = open(input_file_1, 'rb')
    input_1 = PdfFileReader(input_f_1)

    input_f_2 = open(input_file_2, 'rb')
    input_2 = PdfFileReader(input_f_2)

    for i in range(max(input_1.getNumPages(), input_2.getNumPages())):
        try:
            pdf_output.addPage(input_1.getPage(i))
        except IndexError:
            pass
        try:
            pdf_output.addPage(input_2.getPage(i))
        except IndexError:
            pass

    with open(output_file, 'wb') as f:
        pdf_output.write(f)

    input_f_1.close()
    input_f_2.close()

    return output_file


def merge_pdf(input_file_list, output_file):
    """合并pdf

    :param input_file_list:
    :param output_file:
    :return:
    """
    pdf_output = PdfFileWriter()
    for input_file in input_file_list:
        with open(input_file, 'rb') as f:
            pdf_input = PdfFileReader(f)
            # 获取 pdf 共用多少页
            page_count = pdf_input.getNumPages()
            print(page_count)

            for i in range(page_count):
                pdf_output.addPage(pdf_input.getPage(i))

    with open(output_file, 'wb') as f:
        pdf_output.write(f)


if __name__ == '__main__':
    # reverse_pdf('奇数页.pdf', 'aaaaa.pdf')
    merge_pdf_between('合并版.pdf', '偶数页.pdf', 'aaa.pdf')
