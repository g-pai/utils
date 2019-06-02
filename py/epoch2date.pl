:
inp=$1
echo "converting epoch $inp"
perl -e "print scalar(localtime($inp))"
