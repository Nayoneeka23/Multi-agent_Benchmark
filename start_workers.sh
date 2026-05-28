#!/bin/bash
source ~/myenv/bin/activate
cd ~/multi_agent_benchmark/agents

echo "Starting all 10 workers..."

python worker.py worker_1 8001 &
python worker.py worker_2 8002 &
python worker.py worker_3 8003 &
python worker.py worker_4 8004 &
python worker.py worker_5 8005 &
python worker.py worker_6 8006 &
python worker.py worker_7 8007 &
python worker.py worker_8 8008 &
python worker.py worker_9 8009 &
python worker.py worker_10 8010 &

echo "All workers started!"
echo "To stop all workers run: pkill -f worker.py"
