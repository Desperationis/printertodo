# save this as txt_to_tex.py

def process_lines(lines):
    output = []
    for line in lines:
        line = line.rstrip('\n')
        if line.strip().startswith('*'):
            # Replace leading '* ' with '> '
            content = line.strip()[1:].strip()
            output.append(f' {content}')
        elif line.strip() == '':
            continue  # skip blank lines in input
        else:
            output.append(line)
        output.append('')  # add blank line after every line
    return output

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
    # Join content lines with newlines
    content = '\n'.join(content_lines)
    return template.replace('{content}', content)

def main():
    input_filename = 'input.txt'
    output_filename = 'output.tex'
    with open(input_filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    processed = process_lines(lines)
    tex_content = make_tex_document(processed)
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(tex_content)
    print(f"Converted '{input_filename}' to '{output_filename}'.")

if __name__ == '__main__':
    main()

