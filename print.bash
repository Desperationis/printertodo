python3 gen.py
if xelatex output.tex 
then
    lp output.pdf
else
    echo "Error in build"
    exit 1
fi
