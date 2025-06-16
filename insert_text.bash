if [[ $# -ne 2 ]]
then
    echo "insert_text.bash [text] [line]"
    exit 1
fi

python3 insert_text.py $1 $2
xelatex output.tex && okular output.pdf
