from tournament import Tournament
import logging

logging.basicConfig(format='%(message)s',level=logging.DEBUG)
logger = logging.getLogger()

if __name__ == "__main__":
    logger.info("Starting Tournament")
    tournament = Tournament()
    tournament.start()
    tournament.set_matches()
    tournament.print_matches()