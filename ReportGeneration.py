# -*- coding:utf-8 -*-
from TextDealer import read_text, write_text
from FigureDealer import deal_figure


def main():
    with open('template.md', 'r', encoding='utf-8') as f:
        template = f.read()
    text = read_text()
    figures = deal_figure()
    report = write_text(template,text,figures)
    with open('report.md', 'w', encoding='utf-8') as f:
        f.write(report)


if __name__ == '__main__':
    main()
