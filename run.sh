#!/bin/bash
select exec in "backend" "frontend"
do 
	case $exec in
		"backend")
		       	bash scripts/install_gradio.sh
			break
			;;	
		"frontend")
			bash scripts/build_frontend.sh		
			break
			;;
		*)
			echo "wrong choice"
			break
	esac
done
