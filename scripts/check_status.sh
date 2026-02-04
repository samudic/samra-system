#!/bin/bash
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] SAMRA SYSTEM: Opérationnel sur $(hostname)" >> logs/activity.log

# Si on est sur Termux, envoyer une notification
if command -v termux-notification &> /dev/null; then
    termux-notification -t "SAMRA STATUS" -c "Système Actif sur $(hostname)"
fi

echo "Statut mis à jour dans logs/activity.log"
