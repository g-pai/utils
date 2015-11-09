:
inp=shift
echo "converting epoch $inp"
perl -e "print scalar(localtime($inp))"
