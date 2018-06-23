INPUTDIR=../data/illuminations
OUTPUTDIR=../data/proposals_edgeboxes

mkdir -p "$OUTPUTDIR"

ls "$INPUTDUR" | parallel -j10 python3 proposals.py --method edgeboxes -i "$INPUTDIR/{}" -o "$OUTPUTDIR/{}.txt" --threads 1
