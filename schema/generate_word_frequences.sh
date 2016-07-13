
# define the function

function hackityhackhack() { 
    cat models/*.schema.json | tr '"' '\n' | tr -cd '[:alnum:]\n' | grep . | sort | uniq -c | while read count word; do
        echo -ne "$word\t$count\n";
    done
}


# call the function

hackityhackhack > word_frequencies.tsv
