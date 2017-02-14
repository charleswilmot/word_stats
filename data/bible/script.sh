for F in ./*/*.zip
do
   FILE="${./*/F%}"
   cd "$F"
   echo "$FILE"
   unzip "$FILE"
   cd ..
done
