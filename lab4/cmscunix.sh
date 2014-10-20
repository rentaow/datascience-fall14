#!/bin/bash


cat cmsc.txt | awk '/^CMSC/ {class = $0}
					/^0/ {print section; section = class", "$0}
					!/\n|^CMSC|^0/ {section = section", "$0}	
					END {print section}' |
			sed 's/Seats (Total://; s/Open: //; s/Waitlist: \([0-9]*\))/\1/; s/\(M*Tu*W*Th*F*\)/\1,/; s/CSI\|HBK\|AVW\|MTH\|JMP/\0,/; s/, $//'			

