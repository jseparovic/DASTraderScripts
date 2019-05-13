
PYTHON=venv/Scripts/python
for direction in buy sell
do
    for mode in bid mid ask
    do
        for util in t p
        do
            cmd="${PYTHON} dasscript.py -s ${direction}_${mode}_with_risk_on_stop -${util}"
            echo
            echo Running: ${cmd}
            echo
            $cmd
            echo
        done
    done
done

echo
