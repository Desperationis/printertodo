import sys

def make_tex_document(content_lines):
    template = r"""\documentclass[letterpaper]{article}
\usepackage[margin=1in]{geometry}
\usepackage{verbatim}
\usepackage{fontspec}
\usepackage{fancyvrb}
\usepackage{nopageno}
\begin{document}

\makeatletter
\renewcommand\verbatim@font{\normalfont\fontspec{AtkynsonMono Nerd Font Mono}\fontsize{10pt}{10pt}\selectfont}
\makeatother

\begin{verbatim}
{content}
\end{verbatim}

\end{document}
"""
    content = '\n'.join(content_lines)
    return template.replace('{content}', content)

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 insert_txt.py \"your text\" line_number")
        sys.exit(1)

    insert_text = sys.argv[1]
    line_number = int(sys.argv[2])

    # Calculate the actual line in the verbatim (every other line is blank)
    # So physical line = (line_number - 1) * 2
    total_lines = (line_number - 1) * 2 + 1  # at least this many lines

    content_lines = []
    for i in range(total_lines):
        if i % 2 == 0:
            # Even index: possible text line
            if (i // 2) + 1 == line_number:
                content_lines.append(f' {insert_text}')
            else:
                content_lines.append('')
        else:
            # Odd index: always blank
            content_lines.append('')

    tex_content = make_tex_document(content_lines)
    with open('output.tex', 'w', encoding='utf-8') as f:
        f.write(tex_content)
    print(f"Inserted '> {insert_text}' at logical line {line_number} in output.tex.")

if __name__ == '__main__':
    main()
