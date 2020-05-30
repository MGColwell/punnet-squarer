#Pipe the output of the punnet squarer into this if all you want is the unique combos possible

echo "Unique combinations possible:"
IFS= read line
while IFS= read line; do
  echo ${line} | tr -d '|'
done
